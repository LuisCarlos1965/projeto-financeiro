#!/usr/bin/env python3
"""
SYSFIN Splash Screen JPG Generator
Creates a professional 3D splash screen for SYSFIN V1.0 and saves as JPG
Works without GUI dependencies - generates image directly
"""

import math
import time
import random
try:
    from PIL import Image, ImageDraw, ImageFont, ImageFilter
    PIL_AVAILABLE = True
except ImportError:
    PIL_AVAILABLE = False
    print("Warning: PIL not available. Installing...")

def install_pil():
    """Try to install PIL if not available"""
    import subprocess
    import sys
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "Pillow", "--break-system-packages", "--user"])
        global PIL_AVAILABLE
        import importlib
        importlib.invalidate_caches()
        try:
            from PIL import Image, ImageDraw, ImageFont, ImageFilter
            PIL_AVAILABLE = True
            return True
        except ImportError:
            return False
    except:
        try:
            # Try importing in case it was already installed
            from PIL import Image, ImageDraw, ImageFont, ImageFilter
            PIL_AVAILABLE = True
            return True
        except ImportError:
            return False

class SysfinSplashGenerator:
    def __init__(self, width=1920, height=1080):
        """Initialize the splash screen generator with specified dimensions"""
        # Default to 90% of a typical screen (1920x1080)
        self.width = int(width * 0.9) if width > 100 else width
        self.height = int(height * 0.9) if height > 100 else height
        
        # If dimensions are too small, use defaults
        if self.width < 800:
            self.width = 1728  # 90% of 1920
        if self.height < 600:
            self.height = 972   # 90% of 1080
            
        print(f"Gerando splash screen: {self.width}x{self.height} pixels")
        
    def create_gradient_background(self):
        """Create a modern gradient background with 3D effect"""
        img = Image.new('RGB', (self.width, self.height), '#000000')
        draw = ImageDraw.Draw(img)
        
        # Create multi-layer gradient for depth
        for y in range(self.height):
            ratio = y / self.height
            
            # Layer 1: Deep blue to purple gradient
            if ratio < 0.3:
                # Dark blue to bright blue
                r = int(5 + (45 * ratio / 0.3))
                g = int(10 + (60 * ratio / 0.3))
                b = int(30 + (120 * ratio / 0.3))
            elif ratio < 0.7:
                # Blue to purple
                local_ratio = (ratio - 0.3) / 0.4
                r = int(50 + (90 * local_ratio))
                g = int(70 + (-30 * local_ratio))
                b = int(150 + (50 * local_ratio))
            else:
                # Purple to dark with highlight
                local_ratio = (ratio - 0.7) / 0.3
                r = int(140 - (130 * local_ratio))
                g = int(40 - (30 * local_ratio))
                b = int(200 - (190 * local_ratio))
            
            # Add some horizontal gradient for 3D effect
            for x in range(self.width):
                x_ratio = x / self.width
                # Slight side gradients for 3D depth
                r_final = max(0, min(255, r + int(20 * math.sin(x_ratio * math.pi))))
                g_final = max(0, min(255, g + int(15 * math.sin(x_ratio * math.pi))))
                b_final = max(0, min(255, b + int(25 * math.sin(x_ratio * math.pi))))
                
                color = (r_final, g_final, b_final)
                draw.point((x, y), fill=color)
        
        return img
        
    def add_3d_lighting_effects(self, img):
        """Add lighting effects for 3D appearance"""
        lighting_img = img.copy()
        draw = ImageDraw.Draw(lighting_img, 'RGBA')
        
        # Add radial light source from top-left
        center_x, center_y = self.width // 4, self.height // 4
        max_radius = min(self.width, self.height)
        
        for radius in range(0, max_radius // 3, 20):
            alpha = max(0, 50 - radius // 10)
            draw.ellipse([
                center_x - radius, center_y - radius,
                center_x + radius, center_y + radius
            ], fill=(255, 255, 255, alpha))
        
        # Add subtle corner shadows
        shadow_size = min(self.width, self.height) // 6
        for corner in [(0, 0), (self.width - shadow_size, 0), 
                      (0, self.height - shadow_size), 
                      (self.width - shadow_size, self.height - shadow_size)]:
            draw.rectangle([corner[0], corner[1], 
                          corner[0] + shadow_size, corner[1] + shadow_size],
                         fill=(0, 0, 0, 30))
        
        return lighting_img
        
    def create_3d_text_effect(self, text, font_size, x, y, color=(0, 255, 136)):
        """Create 3D text effect with multiple shadow layers"""
        # Try to load a bold font
        try:
            font_paths = [
                "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf",
                "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
                "/System/Library/Fonts/Helvetica.ttc",
                "arial.ttf"
            ]
            font = None
            for font_path in font_paths:
                try:
                    font = ImageFont.truetype(font_path, font_size)
                    break
                except:
                    continue
            if font is None:
                font = ImageFont.load_default()
        except:
            font = ImageFont.load_default()
        
        # Create transparent image for text
        text_img = Image.new('RGBA', (self.width, self.height), (0, 0, 0, 0))
        draw = ImageDraw.Draw(text_img)
        
        # Get text dimensions
        bbox = draw.textbbox((0, 0), text, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
        
        # Center the text
        text_x = x - text_width // 2
        text_y = y - text_height // 2
        
        # Create 3D effect with multiple shadow layers
        shadow_layers = [
            ((0, 0, 0, 180), 8),      # Deep shadow
            ((0, 0, 0, 120), 6),      # Medium shadow
            ((0, 0, 0, 80), 4),       # Light shadow
            ((50, 50, 50, 100), 2),   # Close shadow
        ]
        
        # Draw shadow layers
        for (shadow_color, offset) in shadow_layers:
            draw.text((text_x + offset, text_y + offset), text, 
                     fill=shadow_color, font=font)
        
        # Draw main text with gradient effect
        main_color = color + (255,)  # Add alpha
        draw.text((text_x, text_y), text, fill=main_color, font=font)
        
        # Add highlight
        highlight_color = tuple(min(255, c + 50) for c in color) + (150,)
        draw.text((text_x - 1, text_y - 1), text, fill=highlight_color, font=font)
        
        return text_img
        
    def add_animated_particles(self, img, seed=None):
        """Add floating particles for dynamic effect"""
        if seed:
            random.seed(seed)
            
        particle_img = img.copy()
        draw = ImageDraw.Draw(particle_img, 'RGBA')
        
        # Create different types of particles
        num_particles = 80
        
        for i in range(num_particles):
            x = random.randint(0, self.width)
            y = random.randint(0, self.height)
            size = random.randint(1, 4)
            
            # Create floating motion effect
            offset_x = int(math.sin(i * 0.1) * 30)
            offset_y = int(math.cos(i * 0.1) * 20)
            
            particle_x = (x + offset_x) % self.width
            particle_y = (y + offset_y) % self.height
            
            # Vary particle colors
            if i % 3 == 0:
                color = (0, 255, 136, 150)  # Green
            elif i % 3 == 1:
                color = (136, 255, 170, 100)  # Light green
            else:
                color = (170, 255, 204, 80)   # Very light green
            
            # Draw particle with glow effect
            for glow in range(size, 0, -1):
                alpha = max(20, 150 - (size - glow) * 30)
                glow_color = color[:3] + (alpha,)
                draw.ellipse([
                    particle_x - glow, particle_y - glow,
                    particle_x + glow, particle_y + glow
                ], fill=glow_color)
        
        return particle_img
        
    def add_border_effects(self, img):
        """Add animated border and corner effects"""
        border_img = img.copy()
        draw = ImageDraw.Draw(border_img, 'RGBA')
        
        # Main border
        border_color = (0, 255, 136, 200)
        border_width = 4
        
        # Draw outer border
        draw.rectangle([0, 0, self.width - 1, self.height - 1], 
                      outline=border_color, width=border_width)
        
        # Draw inner border for depth
        inner_border = (136, 255, 170, 150)
        draw.rectangle([border_width, border_width, 
                       self.width - border_width - 1, 
                       self.height - border_width - 1], 
                      outline=inner_border, width=2)
        
        # Add corner decorations
        corner_size = 40
        corner_color = (0, 255, 136, 255)
        
        corners = [
            (border_width, border_width),  # Top-left
            (self.width - corner_size - border_width, border_width),  # Top-right
            (border_width, self.height - corner_size - border_width),  # Bottom-left
            (self.width - corner_size - border_width, 
             self.height - corner_size - border_width)  # Bottom-right
        ]
        
        for corner_x, corner_y in corners:
            # Corner lines
            draw.line([corner_x, corner_y, corner_x + corner_size, corner_y], 
                     fill=corner_color, width=6)
            draw.line([corner_x, corner_y, corner_x, corner_y + corner_size], 
                     fill=corner_color, width=6)
        
        return border_img
        
    def create_logo_symbol(self):
        """Create a stylized logo symbol for SYSFIN"""
        symbol_size = min(self.width, self.height) // 8
        symbol_img = Image.new('RGBA', (symbol_size, symbol_size), (0, 0, 0, 0))
        draw = ImageDraw.Draw(symbol_img)
        
        # Create a modern financial symbol (stylized S + F)
        center = symbol_size // 2
        
        # Draw stylized 'S' curve
        points_s = []
        for i in range(100):
            angle = (i / 100) * math.pi * 2
            x = center + int((symbol_size // 3) * math.sin(angle))
            y = center + int((symbol_size // 4) * math.cos(angle * 2))
            points_s.append((x, y))
        
        # Draw the S shape
        for i in range(len(points_s) - 1):
            draw.line([points_s[i], points_s[i + 1]], 
                     fill=(0, 255, 136, 200), width=3)
        
        # Add geometric elements
        draw.rectangle([center - 10, center - 10, center + 10, center + 10],
                      outline=(136, 255, 170, 255), width=2)
        
        return symbol_img
        
    def generate_splash_screen(self, output_path="/workspace/sysfin_splash_screen.jpg"):
        """Generate the complete splash screen"""
        print("Gerando fundo gradiente...")
        # Create base gradient background
        base_img = self.create_gradient_background()
        
        print("Adicionando efeitos de iluminação 3D...")
        # Add 3D lighting effects
        base_img = self.add_3d_lighting_effects(base_img)
        
        print("Criando partículas animadas...")
        # Add animated particles
        base_img = self.add_animated_particles(base_img, seed=42)
        
        print("Gerando texto principal...")
        # Create main title
        title_img = self.create_3d_text_effect(
            "SYSFIN", 
            font_size=min(self.width, self.height) // 15,
            x=self.width // 2, 
            y=self.height // 3,
            color=(0, 255, 136)
        )
        
        print("Gerando subtítulo...")
        # Create subtitle
        subtitle_img = self.create_3d_text_effect(
            "SISTEMA FINANCEIRO", 
            font_size=min(self.width, self.height) // 25,
            x=self.width // 2, 
            y=self.height // 3 + min(self.width, self.height) // 12,
            color=(136, 255, 170)
        )
        
        print("Gerando versão...")
        # Create version text
        version_img = self.create_3d_text_effect(
            "VERSÃO 1.0", 
            font_size=min(self.width, self.height) // 35,
            x=self.width // 2, 
            y=self.height // 3 + min(self.width, self.height) // 8,
            color=(170, 255, 204)
        )
        
        print("Criando símbolo do logo...")
        # Create logo symbol
        logo_symbol = self.create_logo_symbol()
        
        print("Combinando elementos...")
        # Combine all elements
        final_img = base_img.copy()
        final_img.paste(title_img, (0, 0), title_img)
        final_img.paste(subtitle_img, (0, 0), subtitle_img)
        final_img.paste(version_img, (0, 0), version_img)
        
        # Position logo symbol
        logo_x = self.width // 2 - logo_symbol.width // 2
        logo_y = self.height // 3 - min(self.width, self.height) // 6
        final_img.paste(logo_symbol, (logo_x, logo_y), logo_symbol)
        
        print("Adicionando bordas e efeitos finais...")
        # Add border effects
        final_img = self.add_border_effects(final_img)
        
        print("Salvando imagem JPG...")
        # Convert to RGB for JPG and save
        final_img = final_img.convert('RGB')
        final_img.save(output_path, "JPEG", quality=95, optimize=True)
        
        print(f"✓ Splash screen salva com sucesso: {output_path}")
        print(f"  Dimensões: {self.width}x{self.height} pixels")
        print(f"  Tamanho do arquivo: {self.get_file_size(output_path)}")
        
        return output_path
        
    def get_file_size(self, filepath):
        """Get human readable file size"""
        try:
            import os
            size_bytes = os.path.getsize(filepath)
            if size_bytes < 1024:
                return f"{size_bytes} bytes"
            elif size_bytes < 1024**2:
                return f"{size_bytes/1024:.1f} KB"
            else:
                return f"{size_bytes/(1024**2):.1f} MB"
        except:
            return "unknown"

def main():
    """Main function to generate SYSFIN splash screen"""
    print("=" * 60)
    print("    SYSFIN SPLASH SCREEN GENERATOR V1.0")
    print("=" * 60)
    print()
    
    # Check if PIL is available
    if not PIL_AVAILABLE:
        print("Tentando instalar PIL...")
        if not install_pil():
            print("❌ Erro: Não foi possível instalar PIL/Pillow")
            print("Execute: pip install Pillow")
            return
    
    try:
        # Create generator with default 90% screen size
        generator = SysfinSplashGenerator(1920, 1080)
        
        # Generate the splash screen
        output_path = generator.generate_splash_screen()
        
        print()
        print("=" * 60)
        print("✓ SPLASH SCREEN GERADA COM SUCESSO!")
        print("=" * 60)
        print(f"Arquivo: {output_path}")
        print()
        print("Características:")
        print("- Design 3D moderno com efeitos de iluminação")
        print("- Gradiente azul-roxo profissional")
        print("- Partículas animadas (efeito congelado na imagem)")
        print("- Texto com efeito 3D e sombras")
        print("- Bordas decorativas")
        print("- Dimensões: 90% da tela (padrão 1728x972)")
        print("- Formato: JPG de alta qualidade")
        
    except Exception as e:
        print(f"❌ Erro ao gerar splash screen: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()