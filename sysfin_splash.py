import tkinter as tk
from tkinter import ttk, messagebox
import math
import time
import threading
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageTk
import os

class SysfinSplash:
    def __init__(self):
        self.root = tk.Tk()
        self.setup_window()
        self.animation_running = True
        self.progress = 0
        self.angle = 0
        
        # Create the splash content
        self.create_splash_screen()
        
        # Start animations
        self.start_animations()
        
    def setup_window(self):
        """Configure the main window to 90% of screen size"""
        # Get screen dimensions
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        
        # Calculate 90% of screen size
        self.width = int(screen_width * 0.9)
        self.height = int(screen_height * 0.9)
        
        # Center the window
        x = (screen_width - self.width) // 2
        y = (screen_height - self.height) // 2
        
        # Configure window
        self.root.geometry(f"{self.width}x{self.height}+{x}+{y}")
        self.root.title("SYSFIN - Sistema Financeiro")
        self.root.configure(bg='#0a0a0a')
        self.root.resizable(False, False)
        self.root.overrideredirect(True)  # Remove window decorations for splash effect
        
        # Make window stay on top
        self.root.attributes('-topmost', True)
        
    def create_gradient_background(self):
        """Create a modern gradient background"""
        # Create PIL image for gradient
        img = Image.new('RGB', (self.width, self.height), '#000000')
        draw = ImageDraw.Draw(img)
        
        # Create gradient from dark blue to purple to dark
        for y in range(self.height):
            # Calculate color interpolation
            ratio = y / self.height
            
            if ratio < 0.3:
                # Dark blue to blue
                r = int(10 + (30 * ratio / 0.3))
                g = int(15 + (50 * ratio / 0.3))
                b = int(40 + (100 * ratio / 0.3))
            elif ratio < 0.7:
                # Blue to purple
                local_ratio = (ratio - 0.3) / 0.4
                r = int(40 + (80 * local_ratio))
                g = int(65 + (-20 * local_ratio))
                b = int(140 + (40 * local_ratio))
            else:
                # Purple to dark
                local_ratio = (ratio - 0.7) / 0.3
                r = int(120 - (110 * local_ratio))
                g = int(45 - (35 * local_ratio))
                b = int(180 - (170 * local_ratio))
            
            color = f'#{r:02x}{g:02x}{b:02x}'
            draw.line([(0, y), (self.width, y)], fill=color)
        
        return img
        
    def create_3d_text_effect(self, text, font_size, x, y, color='#ffffff'):
        """Create 3D text effect with shadows and depth"""
        try:
            font = ImageFont.truetype("/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf", font_size)
        except:
            try:
                font = ImageFont.truetype("arial.ttf", font_size)
            except:
                font = ImageFont.load_default()
        
        # Create text image
        text_img = Image.new('RGBA', (self.width, self.height), (0, 0, 0, 0))
        draw = ImageDraw.Draw(text_img)
        
        # Get text size
        bbox = draw.textbbox((0, 0), text, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
        
        # Center text
        text_x = x - text_width // 2
        text_y = y - text_height // 2
        
        # Draw shadow layers for 3D effect
        shadow_colors = ['#000000', '#1a1a1a', '#333333', '#4d4d4d']
        for i, shadow_color in enumerate(shadow_colors):
            offset = len(shadow_colors) - i
            draw.text((text_x + offset, text_y + offset), text, 
                     fill=shadow_color, font=font)
        
        # Draw main text
        draw.text((text_x, text_y), text, fill=color, font=font)
        
        return text_img
        
    def create_animated_particles(self, base_img):
        """Add animated particles for dynamic effect"""
        particle_img = base_img.copy()
        draw = ImageDraw.Draw(particle_img)
        
        # Create floating particles
        import random
        for _ in range(50):
            x = random.randint(0, self.width)
            y = random.randint(0, self.height)
            size = random.randint(1, 3)
            
            # Animated position based on time
            offset_x = int(math.sin(time.time() + x * 0.01) * 20)
            offset_y = int(math.cos(time.time() + y * 0.01) * 10)
            
            alpha = int(128 + 127 * math.sin(time.time() + x * 0.02))
            color = f'#{alpha//4:02x}{alpha//2:02x}{alpha:02x}'
            
            particle_x = (x + offset_x) % self.width
            particle_y = (y + offset_y) % self.height
            
            draw.ellipse([particle_x, particle_y, 
                         particle_x + size, particle_y + size], 
                        fill=color)
        
        return particle_img
        
    def create_splash_screen(self):
        """Create the main splash screen content"""
        # Create canvas for the splash
        self.canvas = tk.Canvas(self.root, width=self.width, height=self.height,
                               highlightthickness=0, bg='#000000')
        self.canvas.pack(fill='both', expand=True)
        
        # Create progress bar
        self.progress_var = tk.DoubleVar()
        self.progress_bar = ttk.Progressbar(
            self.root,
            variable=self.progress_var,
            maximum=100,
            length=400,
            style='Custom.Horizontal.TProgressbar'
        )
        
        # Style the progress bar
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('Custom.Horizontal.TProgressbar',
                       troughcolor='#333333',
                       background='#00ff88',
                       lightcolor='#00ff88',
                       darkcolor='#00aa55')
        
        # Position progress bar
        progress_y = self.height - 100
        self.progress_bar.place(x=self.width//2 - 200, y=progress_y, width=400, height=20)
        
        # Create loading label
        self.loading_label = tk.Label(
            self.root,
            text="Carregando SYSFIN...",
            font=('Arial', 12, 'bold'),
            fg='#00ff88',
            bg='#000000'
        )
        self.loading_label.place(x=self.width//2 - 80, y=progress_y + 30)
        
        # Update splash content
        self.update_splash_content()
        
    def update_splash_content(self):
        """Update the splash screen with animated content"""
        if not self.animation_running:
            return
            
        # Clear canvas
        self.canvas.delete("all")
        
        # Create gradient background
        bg_img = self.create_gradient_background()
        
        # Add animated particles
        bg_img = self.create_animated_particles(bg_img)
        
        # Create main title
        title_img = self.create_3d_text_effect(
            "SYSFIN", 72, self.width//2, self.height//3,
            color='#00ff88'
        )
        
        # Create subtitle
        subtitle_img = self.create_3d_text_effect(
            "SISTEMA FINANCEIRO", 24, self.width//2, self.height//3 + 100,
            color='#88ffaa'
        )
        
        # Create version
        version_img = self.create_3d_text_effect(
            "VERSÃO 1.0", 18, self.width//2, self.height//3 + 140,
            color='#aaffcc'
        )
        
        # Combine all images
        combined_img = bg_img.copy()
        combined_img.paste(title_img, (0, 0), title_img)
        combined_img.paste(subtitle_img, (0, 0), subtitle_img)
        combined_img.paste(version_img, (0, 0), version_img)
        
        # Add rotating 3D effect
        self.angle += 2
        if self.angle >= 360:
            self.angle = 0
            
        # Convert to PhotoImage and display
        self.bg_photo = ImageTk.PhotoImage(combined_img)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.bg_photo)
        
        # Add animated elements
        self.add_animated_elements()
        
        # Schedule next update
        self.root.after(50, self.update_splash_content)
        
    def add_animated_elements(self):
        """Add animated UI elements"""
        # Animated border
        border_color = f'#{int(128 + 127 * math.sin(time.time())):02x}ff88'
        self.canvas.create_rectangle(10, 10, self.width-10, self.height-10,
                                   outline=border_color, width=3)
        
        # Animated corners
        corner_size = 30
        corner_color = '#00ff88'
        
        # Top-left corner
        self.canvas.create_line(10, 10, 10 + corner_size, 10, 
                               fill=corner_color, width=4)
        self.canvas.create_line(10, 10, 10, 10 + corner_size, 
                               fill=corner_color, width=4)
        
        # Top-right corner
        self.canvas.create_line(self.width-10, 10, self.width-10-corner_size, 10, 
                               fill=corner_color, width=4)
        self.canvas.create_line(self.width-10, 10, self.width-10, 10 + corner_size, 
                               fill=corner_color, width=4)
        
        # Bottom-left corner
        self.canvas.create_line(10, self.height-10, 10 + corner_size, self.height-10, 
                               fill=corner_color, width=4)
        self.canvas.create_line(10, self.height-10, 10, self.height-10-corner_size, 
                               fill=corner_color, width=4)
        
        # Bottom-right corner
        self.canvas.create_line(self.width-10, self.height-10, self.width-10-corner_size, self.height-10, 
                               fill=corner_color, width=4)
        self.canvas.create_line(self.width-10, self.height-10, self.width-10, self.height-10-corner_size, 
                               fill=corner_color, width=4)
        
    def start_animations(self):
        """Start the loading animation"""
        def animate_progress():
            while self.animation_running and self.progress < 100:
                self.progress += 1
                self.progress_var.set(self.progress)
                
                # Update loading text
                loading_texts = [
                    "Iniciando sistema...",
                    "Carregando módulos...",
                    "Verificando licença...",
                    "Conectando ao banco...",
                    "Preparando interface...",
                    "Finalizando..."
                ]
                
                text_index = min(self.progress // 17, len(loading_texts) - 1)
                self.loading_label.config(text=loading_texts[text_index])
                
                time.sleep(0.1)
            
            if self.animation_running:
                self.loading_label.config(text="Sistema pronto!")
                time.sleep(2)
                self.close_splash()
        
        # Start progress animation in separate thread
        progress_thread = threading.Thread(target=animate_progress)
        progress_thread.daemon = True
        progress_thread.start()
        
    def save_as_jpg(self):
        """Save the current splash screen as JPG"""
        try:
            # Create the final image
            bg_img = self.create_gradient_background()
            bg_img = self.create_animated_particles(bg_img)
            
            # Add text elements
            title_img = self.create_3d_text_effect(
                "SYSFIN", 72, self.width//2, self.height//3,
                color='#00ff88'
            )
            subtitle_img = self.create_3d_text_effect(
                "SISTEMA FINANCEIRO", 24, self.width//2, self.height//3 + 100,
                color='#88ffaa'
            )
            version_img = self.create_3d_text_effect(
                "VERSÃO 1.0", 18, self.width//2, self.height//3 + 140,
                color='#aaffcc'
            )
            
            # Combine images
            final_img = bg_img.copy()
            final_img.paste(title_img, (0, 0), title_img)
            final_img.paste(subtitle_img, (0, 0), subtitle_img)
            final_img.paste(version_img, (0, 0), version_img)
            
            # Convert to RGB for JPG
            final_img = final_img.convert('RGB')
            
            # Save as JPG
            output_path = "/workspace/sysfin_splash_screen.jpg"
            final_img.save(output_path, "JPEG", quality=95)
            
            print(f"Splash screen salva como: {output_path}")
            return output_path
            
        except Exception as e:
            print(f"Erro ao salvar imagem: {e}")
            return None
            
    def close_splash(self):
        """Close the splash screen"""
        self.animation_running = False
        
        # Save as JPG before closing
        saved_path = self.save_as_jpg()
        if saved_path:
            messagebox.showinfo("Sucesso", f"Tela de abertura salva em:\n{saved_path}")
        
        self.root.quit()
        
    def run(self):
        """Run the splash screen"""
        # Bind escape key to close
        self.root.bind('<Escape>', lambda e: self.close_splash())
        self.root.bind('<Button-1>', lambda e: self.close_splash())
        
        # Center and show
        self.root.mainloop()

def main():
    """Main function to run the SYSFIN splash screen"""
    print("Iniciando SYSFIN Splash Screen...")
    print("Pressione ESC ou clique para fechar")
    
    splash = SysfinSplash()
    splash.run()

if __name__ == "__main__":
    main()