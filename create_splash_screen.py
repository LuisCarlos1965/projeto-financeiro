#!/usr/bin/env python3
"""
SYSFIN Splash Screen Generator
Creates a futuristic 3D-style splash screen for SYSFIN v1.0
"""

import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance
import math
import os

def create_gradient_background(width, height):
    """Create a cyberpunk gradient background"""
    # Create base gradient from dark blue to purple to black
    image = Image.new('RGB', (width, height))
    draw = ImageDraw.Draw(image)
    
    # Create multiple gradient layers for depth
    for y in range(height):
        # Primary gradient
        ratio = y / height
        
        # Cyberpunk color palette
        if ratio < 0.3:
            # Dark blue to cyan
            r = int(0 + ratio * 100)
            g = int(20 + ratio * 200)
            b = int(40 + ratio * 150)
        elif ratio < 0.7:
            # Cyan to purple
            r = int(30 + (ratio - 0.3) * 150)
            g = int(60 + (ratio - 0.3) * 50)
            b = int(190 - (ratio - 0.3) * 100)
        else:
            # Purple to black
            r = int(180 * (1 - ratio))
            g = int(110 * (1 - ratio))
            b = int(90 * (1 - ratio))
        
        # Add some noise for texture
        noise = int(np.random.normal(0, 5))
        r = max(0, min(255, r + noise))
        g = max(0, min(255, g + noise))
        b = max(0, min(255, b + noise))
        
        color = (r, g, b)
        draw.line([(0, y), (width, y)], fill=color)
    
    return image

def add_grid_pattern(image):
    """Add futuristic grid pattern overlay"""
    width, height = image.size
    overlay = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)
    
    # Grid parameters
    grid_size = 50
    line_color = (0, 255, 255, 30)  # Cyan with transparency
    
    # Vertical lines
    for x in range(0, width, grid_size):
        draw.line([(x, 0), (x, height)], fill=line_color, width=1)
    
    # Horizontal lines
    for y in range(0, height, grid_size):
        draw.line([(0, y), (width, y)], fill=line_color, width=1)
    
    # Convert to RGB and blend
    overlay_rgb = Image.new('RGB', (width, height))
    overlay_rgb.paste(overlay, (0, 0))
    
    return Image.blend(image, overlay_rgb, 0.1)

def create_3d_text_effect(image, text, font_size, position):
    """Create 3D text effect with glow"""
    width, height = image.size
    text_layer = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(text_layer)
    
    try:
        # Try to use a bold font
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", font_size)
    except:
        # Fallback to default font
        font = ImageFont.load_default()
    
    x, y = position
    
    # Create 3D depth effect by drawing multiple layers
    depth_layers = 8
    for i in range(depth_layers, 0, -1):
        offset_x = x + i * 2
        offset_y = y + i * 2
        
        # Shadow color - darker for deeper layers
        shadow_intensity = int(255 * (1 - i / depth_layers) * 0.3)
        shadow_color = (shadow_intensity, shadow_intensity, shadow_intensity, 200)
        
        draw.text((offset_x, offset_y), text, font=font, fill=shadow_color)
    
    # Main text with bright cyan
    main_color = (0, 255, 255, 255)
    draw.text((x, y), text, font=font, fill=main_color)
    
    # Add glow effect
    glow_layer = text_layer.copy()
    glow_layer = glow_layer.filter(ImageFilter.GaussianBlur(radius=3))
    
    # Combine layers
    final_text = Image.alpha_composite(glow_layer, text_layer)
    
    # Convert to RGB for blending
    text_rgb = Image.new('RGB', (width, height), (0, 0, 0))
    text_rgb.paste(final_text, (0, 0), final_text)
    
    return Image.blend(image, text_rgb, 0.8)

def add_geometric_elements(image):
    """Add futuristic geometric elements"""
    width, height = image.size
    overlay = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)
    
    # Add some geometric shapes
    center_x, center_y = width // 2, height // 2
    
    # Outer ring
    ring_radius = min(width, height) // 4
    ring_color = (255, 0, 255, 100)  # Magenta with transparency
    draw.ellipse([center_x - ring_radius, center_y - ring_radius,
                  center_x + ring_radius, center_y + ring_radius],
                 outline=ring_color, width=3)
    
    # Inner ring
    inner_radius = ring_radius // 2
    inner_color = (0, 255, 255, 100)  # Cyan with transparency
    draw.ellipse([center_x - inner_radius, center_y - inner_radius,
                  center_x + inner_radius, center_y + inner_radius],
                 outline=inner_color, width=2)
    
    # Add some lines radiating from center
    for angle in range(0, 360, 45):
        rad = math.radians(angle)
        start_x = center_x + int(inner_radius * math.cos(rad))
        start_y = center_y + int(inner_radius * math.sin(rad))
        end_x = center_x + int(ring_radius * math.cos(rad))
        end_y = center_y + int(ring_radius * math.sin(rad))
        
        draw.line([(start_x, start_y), (end_x, end_y)],
                  fill=(255, 255, 255, 80), width=1)
    
    # Convert to RGB and blend
    overlay_rgb = Image.new('RGB', (width, height))
    overlay_rgb.paste(overlay, (0, 0))
    
    return Image.blend(image, overlay_rgb, 0.3)

def create_splash_screen(width=1920, height=1080):
    """Create the complete splash screen"""
    print("Creating SYSFIN splash screen...")
    
    # Create base gradient background
    image = create_gradient_background(width, height)
    
    # Add grid pattern
    image = add_grid_pattern(image)
    
    # Add geometric elements
    image = add_geometric_elements(image)
    
    # Add main title
    title_font_size = width // 15
    title_position = (width // 2 - title_font_size * 3, height // 2 - title_font_size)
    image = create_3d_text_effect(image, "SYSFIN", title_font_size, title_position)
    
    # Add version text
    version_font_size = width // 30
    version_position = (width // 2 - version_font_size * 2, height // 2 + title_font_size // 2)
    image = create_3d_text_effect(image, "VERSÃO 1.0", version_font_size, version_position)
    
    # Add loading text at bottom
    loading_font_size = width // 40
    loading_position = (width // 2 - loading_font_size * 2, height - height // 8)
    image = create_3d_text_effect(image, "CARREGANDO...", loading_font_size, loading_position)
    
    # Enhance colors for more vibrant look
    enhancer = ImageEnhance.Color(image)
    image = enhancer.enhance(1.3)
    
    # Enhance contrast
    enhancer = ImageEnhance.Contrast(image)
    image = enhancer.enhance(1.2)
    
    return image

def main():
    """Main function to create and save the splash screen"""
    # Create splash screen
    splash = create_splash_screen(1920, 1080)
    
    # Save as JPG
    output_path = "/workspace/sysfin_splash.jpg"
    splash.save(output_path, "JPEG", quality=95)
    print(f"Splash screen saved as: {output_path}")
    
    return output_path

if __name__ == "__main__":
    main()