#!/usr/bin/env python3
"""
Simple SYSFIN Splash Screen Generator
Creates a text-based representation that can be converted to image
"""

def generate_ascii_splash():
    """Generate ASCII art splash screen for SYSFIN"""
    
    width = 80
    height = 30
    
    # ASCII art for SYSFIN
    logo = [
        "  ██████  ██    ██ ███████ ███████ ██ ███    ██ ",
        " ██       ██    ██ ██      ██      ██ ████   ██ ",
        " ██████   ██    ██ ███████ █████   ██ ██ ██  ██ ",
        "      ██  ██    ██      ██ ██      ██ ██  ██ ██ ",
        " ██████    ██████  ███████ ██      ██ ██   ████ "
    ]
    
    subtitle = "SISTEMA FINANCEIRO"
    version = "VERSÃO 1.0"
    
    print("=" * width)
    print(" " * ((width - len("SYSFIN SPLASH SCREEN")) // 2) + "SYSFIN SPLASH SCREEN")
    print("=" * width)
    print()
    
    # Center the logo
    for line in logo:
        print(" " * ((width - len(line)) // 2) + line)
    
    print()
    print(" " * ((width - len(subtitle)) // 2) + subtitle)
    print(" " * ((width - len(version)) // 2) + version)
    print()
    print("=" * width)
    print(" " * ((width - len("90% Screen Size: 1728x972 pixels")) // 2) + "90% Screen Size: 1728x972 pixels")
    print(" " * ((width - len("Ready for GUI Implementation")) // 2) + "Ready for GUI Implementation")
    print("=" * width)

def main():
    """Main function"""
    print("Gerando SYSFIN Splash Screen...")
    print()
    generate_ascii_splash()
    print()
    print("✓ Splash screen básica gerada!")
    print("Para versão completa com imagens, instale: pip install Pillow")

if __name__ == "__main__":
    main()