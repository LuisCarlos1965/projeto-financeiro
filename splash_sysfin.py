#!/usr/bin/env python3

import argparse
import os
import sys
from typing import Optional, Tuple

try:
	from PIL import Image, ImageDraw, ImageFont, ImageFilter
except Exception as exc:  # Pillow not installed
	print("[erro] Pillow não está instalado. Rode: python3 -m pip install pillow", file=sys.stderr)
	raise


def detect_screen_size() -> Tuple[int, int]:
	"""Best-effort screen size detection. Falls back to env or 1920x1080."""
	# Try Tkinter when available and a display exists
	try:
		import tkinter as tk  # type: ignore
		root = tk.Tk()
		root.withdraw()
		width = root.winfo_screenwidth()
		height = root.winfo_screenheight()
		root.destroy()
		if width and height:
			return int(width), int(height)
	except Exception:
		pass

	# Fallbacks
	width = int(os.environ.get("SCREEN_WIDTH", "1920"))
	height = int(os.environ.get("SCREEN_HEIGHT", "1080"))
	return width, height


def clamp_int(value: int, min_value: int, max_value: int) -> int:
	return max(min_value, min(value, max_value))


def find_default_bold_font() -> Optional[str]:
	"""Try to find a common bold font in typical OS locations."""
	candidates = [
		"/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
		"/usr/share/fonts/truetype/DejaVu/DejaVuSans-Bold.ttf",
		"/usr/share/fonts/truetype/freefont/FreeSansBold.ttf",
		"/usr/share/fonts/truetype/liberation2/LiberationSans-Bold.ttf",
		"/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf",
		"/System/Library/Fonts/Supplemental/Arial Bold.ttf",
		"/Library/Fonts/Arial Bold.ttf",
		"C:\\Windows\\Fonts\\arialbd.ttf",
	]
	for path in candidates:
		if os.path.exists(path):
			return path
	return None


def create_vertical_gradient(size: Tuple[int, int], top_rgb: Tuple[int, int, int], bottom_rgb: Tuple[int, int, int]) -> Image.Image:
	width, height = size
	img = Image.new("RGB", (width, height), top_rgb)
	draw = ImageDraw.Draw(img)
	tr, tg, tb = top_rgb
	br, bg, bb = bottom_rgb
	for y in range(height):
		ratio = y / (height - 1) if height > 1 else 0
		r = int(tr + (br - tr) * ratio)
		g = int(tg + (bg - tg) * ratio)
		b = int(tb + (bb - tb) * ratio)
		draw.line([(0, y), (width, y)], fill=(r, g, b))
	return img


def add_card_with_shadow(base_img: Image.Image, rect_margin_ratio: float = 0.06, corner_radius_px: int = 40) -> Tuple[Image.Image, Tuple[int, int, int, int]]:
	"""Draw a rounded-rectangle 'card' with drop shadow over base_img. Returns (composited_img, card_rect)."""
	width, height = base_img.size
	margin_x = int(width * rect_margin_ratio)
	margin_y = int(height * rect_margin_ratio)
	rect = (margin_x, margin_y, width - margin_x, height - margin_y)

	shadow_offset = (int(width * 0.01), int(height * 0.015))
	shadow_blur = int(min(width, height) * 0.03)
	shadow_alpha = 180

	work = base_img.convert("RGBA")
	shadow = Image.new("RGBA", work.size, (0, 0, 0, 0))
	shadow_draw = ImageDraw.Draw(shadow)
	shadow_rect = (
		rect[0] + shadow_offset[0],
		rect[1] + shadow_offset[1],
		rect[2] + shadow_offset[0],
		rect[3] + shadow_offset[1],
	)
	shadow_draw.rounded_rectangle(shadow_rect, radius=corner_radius_px, fill=(0, 0, 0, shadow_alpha))
	shadow = shadow.filter(ImageFilter.GaussianBlur(radius=shadow_blur))
	work.alpha_composite(shadow)

	card = Image.new("RGBA", work.size, (0, 0, 0, 0))
	card_draw = ImageDraw.Draw(card)
	card_draw.rounded_rectangle(rect, radius=corner_radius_px, fill=(245, 248, 250, 255), outline=(255, 255, 255, 180), width=2)
	work.alpha_composite(card)
	return work, rect


def measure_text(draw: ImageDraw.ImageDraw, text: str, font: ImageFont.FreeTypeFont) -> Tuple[int, int]:
	bbox = draw.textbbox((0, 0), text, font=font)
	return bbox[2] - bbox[0], bbox[3] - bbox[1]


def fit_font_size(text: str, font_path: str, target_width: int, max_px: int) -> ImageFont.FreeTypeFont:
	"""Find a font size that fits text within target_width, up to max_px."""
	low, high = 8, max_px
	best = low
	img = Image.new("RGB", (target_width, max_px), (0, 0, 0))
	draw = ImageDraw.Draw(img)
	while low <= high:
		mid = (low + high) // 2
		font = ImageFont.truetype(font_path, mid)
		w, _ = measure_text(draw, text, font)
		if w <= target_width:
			best = mid
			low = mid + 1
		else:
			high = mid - 1
	return ImageFont.truetype(font_path, best)


def draw_text_stroke_layer(base: Image.Image, position_xy: Tuple[int, int], text: str, font: ImageFont.FreeTypeFont, stroke_width: int, stroke_rgba: Tuple[int, int, int, int]) -> None:
	layer = Image.new("RGBA", base.size, (0, 0, 0, 0))
	d = ImageDraw.Draw(layer)
	# Use fill=stroke_rgba so interior will be covered by gradient later
	d.text(position_xy, text, font=font, fill=stroke_rgba, stroke_width=stroke_width, stroke_fill=stroke_rgba)
	base.alpha_composite(layer)


def draw_gradient_text_fill(base: Image.Image, position_xy: Tuple[int, int], text: str, font: ImageFont.FreeTypeFont, top_rgb: Tuple[int, int, int], bottom_rgb: Tuple[int, int, int]) -> None:
	width, height = base.size
	# Build text mask
	mask = Image.new("L", base.size, 0)
	mask_draw = ImageDraw.Draw(mask)
	mask_draw.text(position_xy, text, font=font, fill=255)
	# Build vertical gradient for entire canvas (simpler)
	grad = create_vertical_gradient((width, height), top_rgb, bottom_rgb)
	colored = Image.composite(grad, Image.new("RGB", (width, height), (0, 0, 0)), mask)
	base.paste(colored, (0, 0), mask)


def draw_extruded_text(base: Image.Image, center_xy: Tuple[int, int], text: str, font: ImageFont.FreeTypeFont, depth_px: int = 10) -> None:
	"""Draw extruded 3D text: shadow/extrusion, stroke, then gradient face."""
	draw = ImageDraw.Draw(base)
	# Measure
	w, h = measure_text(draw, text, font)
	x = int(center_xy[0] - w / 2)
	y = int(center_xy[1] - h / 2)
	pos = (x, y)
	# 1) Extrusion (back layers)
	for offset in range(depth_px, 0, -1):
		draw.text((pos[0] + offset, pos[1] + offset), text, font=font, fill=(0, 0, 0, 255))
	# 2) Stroke layer
	draw_text_stroke_layer(base, pos, text, font, stroke_width=max(1, depth_px // 3), stroke_rgba=(255, 255, 255, 200))
	# 3) Gradient face
	draw_gradient_text_fill(base, pos, text, font, top_rgb=(30, 85, 170), bottom_rgb=(15, 50, 120))


def create_sysfin_splash(target_width: int, target_height: int, output_path: str) -> str:
	"""Create the SYSFIN splash JPG sized to target_width/target_height."""
	# Background gradient
	bg = create_vertical_gradient((target_width, target_height), top_rgb=(12, 30, 64), bottom_rgb=(26, 110, 176))
	# Card + shadow
	canvas, card_rect = add_card_with_shadow(bg, rect_margin_ratio=0.06, corner_radius_px=int(min(target_width, target_height) * 0.04))

	# Font selection
	font_path = find_default_bold_font()
	if not font_path:
		# Fallback to default PIL font (not ideal, but avoids crash)
		font = ImageFont.load_default()
	else:
		# Fit main title
		card_inner_width = card_rect[2] - card_rect[0]
		font = fit_font_size("SYSFIN – VERSÃO 1.0", font_path, int(card_inner_width * 0.9), max_px=int(target_height * 0.16))

	# Draw title centered in upper half of card
	card_center_x = (card_rect[0] + card_rect[2]) // 2
	card_center_y = (card_rect[1] + card_rect[3]) // 2
	center_y_title = int(card_rect[1] + (card_rect[3] - card_rect[1]) * 0.40)
	text = "SYSFIN – VERSÃO 1.0"
	# Convert to RGBA for compositing
	canvas = canvas.convert("RGBA")
	draw_extruded_text(canvas, (card_center_x, center_y_title), text, font, depth_px=max(6, int(min(target_width, target_height) * 0.012)))

	# Optional subtitle (light)
	sub_font: ImageFont.ImageFont
	if isinstance(font, ImageFont.FreeTypeFont):
		try:
			sub_font = ImageFont.truetype(font.path, max(10, int(font.size * 0.35)))
		except Exception:
			sub_font = font
	else:
		sub_font = font

	sub_text = "Carregando..."
	d = ImageDraw.Draw(canvas)
	w_sub, h_sub = measure_text(d, sub_text, sub_font)
	sub_x = card_center_x - w_sub // 2
	sub_y = int(card_rect[1] + (card_rect[3] - card_rect[1]) * 0.68)
	# Subtle shadow then text
	d.text((sub_x + 2, sub_y + 2), sub_text, font=sub_font, fill=(0, 0, 0, 160))
	d.text((sub_x, sub_y), sub_text, font=sub_font, fill=(40, 60, 90, 255))

	# Save as JPG
	final_img = canvas.convert("RGB")
	final_img.save(output_path, format="JPEG", quality=95, subsampling=1, optimize=True)
	return output_path


def show_splash_window(image_path: str, window_width: int, window_height: int, duration_ms: int = 3000) -> None:
	"""Display a borderless centered window showing the splash image for duration_ms."""
	try:
		import tkinter as tk  # type: ignore
		from PIL import ImageTk
		root = tk.Tk()
		root.overrideredirect(True)
		root.attributes("-topmost", True)
		# Center window
		screen_w = root.winfo_screenwidth()
		screen_h = root.winfo_screenheight()
		x = (screen_w - window_width) // 2
		y = (screen_h - window_height) // 2
		root.geometry(f"{window_width}x{window_height}+{x}+{y}")

		img = Image.open(image_path)
		# Ensure the image matches the requested size
		if img.size != (window_width, window_height):
			img = img.resize((window_width, window_height), Image.LANCZOS)
		photo = ImageTk.PhotoImage(img)
		label = tk.Label(root, image=photo, borderwidth=0, highlightthickness=0)
		label.pack(fill="both", expand=True)
		root.after(max(500, duration_ms), root.destroy)
		root.mainloop()
	except Exception as exc:
		print(f"[aviso] Não foi possível exibir a janela de splash automaticamente: {exc}")
		print(f"A imagem foi gerada em: {image_path}")


def parse_args(argv: Optional[list] = None) -> argparse.Namespace:
	parser = argparse.ArgumentParser(description="Gerar e exibir uma tela de abertura SYSFIN – VERSÃO 1.0 em JPG.")
	parser.add_argument("--percent", type=int, default=90, help="Percentual da tela a ser ocupado (10-100). Default: 90")
	parser.add_argument("--duration", type=int, default=3000, help="Duração da exibição em ms. Default: 3000")
	parser.add_argument("--output", type=str, default=os.path.abspath("/workspace/sysfin_splash.jpg"), help="Caminho do arquivo JPG de saída.")
	parser.add_argument("--generate-only", action="store_true", help="Apenas gerar a imagem sem exibir a janela.")
	return parser.parse_args(argv)


def main(argv: Optional[list] = None) -> int:
	args = parse_args(argv)
	percent = clamp_int(args.percent, 10, 100)

	screen_w, screen_h = detect_screen_size()
	target_w = max(100, int(screen_w * (percent / 100.0)))
	target_h = max(100, int(screen_h * (percent / 100.0)))

	# Preserve aspect ratio of screen to avoid distortion
	screen_ratio = screen_w / screen_h if screen_h else 16 / 9
	if abs((target_w / target_h) - screen_ratio) > 0.02:
		# Recompute height from width using screen_ratio
		target_h = int(target_w / screen_ratio)

	os.makedirs(os.path.dirname(args.output), exist_ok=True)
	output_path = create_sysfin_splash(target_w, target_h, args.output)
	print(f"[ok] Imagem gerada: {output_path} ({target_w}x{target_h})")

	if not args.generate_only:
		show_splash_window(output_path, target_w, target_h, duration_ms=args.duration)
	return 0


if __name__ == "__main__":
	sys.exit(main())