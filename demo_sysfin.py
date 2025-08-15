#!/usr/bin/env python3
"""
SYSFIN Demo Application
Demonstrates the complete splash screen experience for SYSFIN v1.0
"""

import time
import sys
import os

# Add current directory to path to import our modules
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from sysfin_splash_display import SysfinSplashScreen

def main():
    """Main demo function"""
    print("=" * 60)
    print("SYSFIN v1.0 - SISTEMA FINANCEIRO")
    print("=" * 60)
    print()
    print("Este é um demo da tela de abertura do SYSFIN v1.0")
    print("Características:")
    print("• Tela de splash em 90% do tamanho da tela")
    print("• Design futurista com cores cyberpunk em 3D")
    print("• Barra de progresso animada")
    print("• Simulação de carregamento do sistema")
    print("• Imagem salva em formato JPG")
    print()
    print("Controles:")
    print("• Pressione ESC para fechar")
    print("• Clique em qualquer lugar para fechar")
    print("• A tela fecha automaticamente após o carregamento")
    print()
    
    input("Pressione ENTER para iniciar o demo...")
    print()
    print("Iniciando SYSFIN...")
    
    try:
        # Show the splash screen
        splash = SysfinSplashScreen()
        splash.show()
        
        print("Demo concluído!")
        print()
        print("Arquivos gerados:")
        print("• sysfin_splash.jpg - Imagem da tela de abertura")
        print("• create_splash_screen.py - Gerador da imagem")
        print("• sysfin_splash_display.py - Exibidor da tela")
        print()
        print("Para usar em seu projeto:")
        print("1. Importe: from sysfin_splash_display import SysfinSplashScreen")
        print("2. Crie: splash = SysfinSplashScreen()")
        print("3. Exiba: splash.show()")
        
    except Exception as e:
        print(f"Erro durante o demo: {e}")
        print("Verifique se o sistema suporta interface gráfica")
    
    print()
    print("Obrigado por usar SYSFIN v1.0!")

if __name__ == "__main__":
    main()