#!/usr/bin/env python3
"""
SYSFIN Splash Screen Display
Displays the SYSFIN splash screen at 90% of screen size
"""

import tkinter as tk
from PIL import Image, ImageTk
import os
import threading
import time

class SysfinSplashScreen:
    def __init__(self):
        self.root = tk.Tk()
        self.setup_window()
        self.load_splash_image()
        
    def setup_window(self):
        """Configure the splash screen window"""
        self.root.title("SYSFIN v1.0")
        
        # Get screen dimensions
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        
        # Calculate 90% of screen size
        self.window_width = int(screen_width * 0.9)
        self.window_height = int(screen_height * 0.9)
        
        # Center the window
        x = (screen_width - self.window_width) // 2
        y = (screen_height - self.window_height) // 2
        
        # Set window geometry
        self.root.geometry(f"{self.window_width}x{self.window_height}+{x}+{y}")
        
        # Remove window decorations for splash screen effect
        self.root.overrideredirect(True)
        
        # Make window stay on top
        self.root.attributes('-topmost', True)
        
        # Set background color
        self.root.configure(bg='black')
        
    def load_splash_image(self):
        """Load and display the splash screen image"""
        splash_image_path = "/workspace/sysfin_splash.jpg"
        
        # Check if splash image exists, create it if not
        if not os.path.exists(splash_image_path):
            print("Splash image not found. Creating it now...")
            from create_splash_screen import main as create_splash
            create_splash()
        
        try:
            # Load and resize image to fit window
            image = Image.open(splash_image_path)
            image = image.resize((self.window_width, self.window_height), Image.Resampling.LANCZOS)
            
            # Convert to PhotoImage for tkinter
            self.photo = ImageTk.PhotoImage(image)
            
            # Create label to display image
            self.image_label = tk.Label(self.root, image=self.photo, bg='black')
            self.image_label.pack(fill=tk.BOTH, expand=True)
            
            # Add loading progress bar
            self.create_progress_bar()
            
        except Exception as e:
            print(f"Error loading splash image: {e}")
            # Fallback to text-only splash
            self.create_text_splash()
    
    def create_progress_bar(self):
        """Create a progress bar at the bottom of the splash screen"""
        # Progress bar frame
        progress_frame = tk.Frame(self.root, bg='black', height=50)
        progress_frame.pack(side=tk.BOTTOM, fill=tk.X, padx=50, pady=30)
        progress_frame.pack_propagate(False)
        
        # Progress bar background
        self.progress_bg = tk.Frame(progress_frame, bg='#001122', height=20)
        self.progress_bg.pack(fill=tk.X, pady=10)
        
        # Progress bar fill
        self.progress_fill = tk.Frame(self.progress_bg, bg='#00FFFF', height=20)
        self.progress_fill.pack(side=tk.LEFT, fill=tk.Y)
        
        # Status text
        self.status_label = tk.Label(progress_frame, text="Inicializando SYSFIN...", 
                                   fg='#00FFFF', bg='black', 
                                   font=('Arial', 12, 'bold'))
        self.status_label.pack(pady=5)
        
    def create_text_splash(self):
        """Create a text-only splash screen as fallback"""
        # Main title
        title_label = tk.Label(self.root, text="SYSFIN", 
                              fg='#00FFFF', bg='black',
                              font=('Arial', 48, 'bold'))
        title_label.pack(expand=True)
        
        # Version
        version_label = tk.Label(self.root, text="VERSÃO 1.0", 
                                fg='#FF00FF', bg='black',
                                font=('Arial', 24))
        version_label.pack()
        
        # Loading text
        loading_label = tk.Label(self.root, text="CARREGANDO...", 
                                fg='#FFFFFF', bg='black',
                                font=('Arial', 16))
        loading_label.pack(pady=20)
        
        # Create simple progress bar
        self.create_progress_bar()
    
    def update_progress(self, progress, status_text):
        """Update the progress bar"""
        try:
            # Update progress bar width
            total_width = self.progress_bg.winfo_width()
            if total_width > 1:  # Ensure window is rendered
                fill_width = int(total_width * progress / 100)
                self.progress_fill.configure(width=fill_width)
            
            # Update status text
            self.status_label.configure(text=status_text)
            
            # Update display
            self.root.update()
        except:
            pass  # Handle case where widgets are destroyed
    
    def simulate_loading(self):
        """Simulate loading process with progress updates"""
        loading_steps = [
            (10, "Carregando módulos..."),
            (25, "Inicializando banco de dados..."),
            (40, "Configurando interface..."),
            (60, "Carregando configurações..."),
            (80, "Preparando sistema..."),
            (95, "Finalizando..."),
            (100, "Sistema pronto!")
        ]
        
        for progress, status in loading_steps:
            self.update_progress(progress, status)
            time.sleep(0.8)  # Simulate loading time
        
        # Keep splash visible for a moment
        time.sleep(1.5)
        
        # Close splash screen
        self.root.quit()
    
    def start_loading_simulation(self):
        """Start loading simulation in a separate thread"""
        loading_thread = threading.Thread(target=self.simulate_loading)
        loading_thread.daemon = True
        loading_thread.start()
    
    def show(self, duration=None):
        """Display the splash screen"""
        # Bind escape key to close
        self.root.bind('<Escape>', lambda e: self.root.quit())
        
        # Bind click to close
        self.root.bind('<Button-1>', lambda e: self.root.quit())
        
        if duration:
            # Auto-close after duration
            self.root.after(duration * 1000, self.root.quit)
        else:
            # Start loading simulation
            self.root.after(500, self.start_loading_simulation)
        
        # Show the window
        self.root.mainloop()
        self.root.destroy()

def main():
    """Main function to display the splash screen"""
    print("Starting SYSFIN Splash Screen...")
    
    try:
        splash = SysfinSplashScreen()
        splash.show()  # Will auto-close after loading simulation
        print("Splash screen closed.")
    except KeyboardInterrupt:
        print("\nSplash screen interrupted.")
    except Exception as e:
        print(f"Error displaying splash screen: {e}")

if __name__ == "__main__":
    main()