# SYSFIN v1.0 - Tela de Abertura Futurista

Este projeto contém uma tela de abertura (splash screen) futurista em 3D para o sistema SYSFIN v1.0.

## Características

- **Design Futurista**: Visual cyberpunk com cores vibrantes (ciano, magenta, roxo)
- **Efeito 3D**: Texto com profundidade e brilho
- **Tamanho Responsivo**: Ocupa 90% da tela automaticamente
- **Barra de Progresso**: Animação de carregamento realística
- **Formato JPG**: Imagem de alta qualidade para carregamento rápido
- **Interface Intuitiva**: Controles simples (ESC, clique ou fechamento automático)

## Arquivos

- `sysfin_splash.jpg` - Imagem da tela de abertura gerada
- `create_splash_screen.py` - Script para gerar a imagem
- `sysfin_splash_display.py` - Script para exibir a tela de abertura
- `demo_sysfin.py` - Demonstração completa do sistema
- `requirements.txt` - Dependências do projeto

## Dependências

### Instalação Ubuntu/Debian
```bash
sudo apt update
sudo apt install python3-pil python3-numpy python3-tk
```

### Instalação via pip (em virtual environment)
```bash
pip install -r requirements.txt
```

## Como Usar

### Método 1: Demo Completo
```bash
python3 demo_sysfin.py
```

### Método 2: Apenas a Tela de Abertura
```bash
python3 sysfin_splash_display.py
```

### Método 3: Gerar Nova Imagem
```bash
python3 create_splash_screen.py
```

### Método 4: Integração em Seu Projeto
```python
from sysfin_splash_display import SysfinSplashScreen

# Criar e exibir a tela de abertura
splash = SysfinSplashScreen()
splash.show()
```

## Personalização

### Cores
As cores podem ser ajustadas no arquivo `create_splash_screen.py`:
- **Ciano**: `(0, 255, 255)` - Texto principal
- **Magenta**: `(255, 0, 255)` - Elementos geométricos
- **Gradiente**: Azul escuro → Ciano → Roxo → Preto

### Tamanho da Tela
Por padrão, a tela ocupa 90% do monitor. Para alterar:
```python
# Em sysfin_splash_display.py, linha ~25
self.window_width = int(screen_width * 0.9)  # Altere 0.9 para o valor desejado
self.window_height = int(screen_height * 0.9)
```

### Duração do Carregamento
Para alterar o tempo de carregamento:
```python
# Em sysfin_splash_display.py, método simulate_loading()
time.sleep(0.8)  # Altere para o tempo desejado entre etapas
```

## Controles da Tela de Abertura

- **ESC**: Fecha a tela imediatamente
- **Clique**: Fecha a tela imediatamente  
- **Automático**: Fecha após completar o carregamento (~6 segundos)

## Resolução da Imagem

A imagem padrão é gerada em **1920x1080** (Full HD). Para alterar:
```python
# Em create_splash_screen.py, função main()
splash = create_splash_screen(1920, 1080)  # Altere as dimensões
```

## Etapas de Carregamento

1. Carregando módulos... (10%)
2. Inicializando banco de dados... (25%)
3. Configurando interface... (40%)
4. Carregando configurações... (60%)
5. Preparando sistema... (80%)
6. Finalizando... (95%)
7. Sistema pronto! (100%)

## Compatibilidade

- **Python**: 3.7+
- **SO**: Linux, Windows, macOS
- **Interface**: Requer suporte a Tkinter (GUI)
- **Resolução**: Adaptável a qualquer tamanho de tela

## Exemplo de Integração

```python
#!/usr/bin/env python3
import sys
import os

# Adicionar ao path se necessário
sys.path.insert(0, '/caminho/para/sysfin')

from sysfin_splash_display import SysfinSplashScreen

def iniciar_aplicacao():
    """Função principal da aplicação"""
    
    # Exibir tela de abertura
    splash = SysfinSplashScreen()
    splash.show()
    
    # Continuar com a inicialização da aplicação
    print("SYSFIN carregado com sucesso!")
    
    # Sua aplicação principal aqui...

if __name__ == "__main__":
    iniciar_aplicacao()
```

## Solução de Problemas

### Erro: "No module named 'PIL'"
```bash
sudo apt install python3-pil
```

### Erro: "No module named 'numpy'"
```bash
sudo apt install python3-numpy
```

### Erro: "No module named 'tkinter'"
```bash
sudo apt install python3-tk
```

### Erro: Interface gráfica não disponível
Certifique-se de que está executando em um ambiente com suporte a GUI (não em servidor sem interface).

---

**SYSFIN v1.0** - Sistema Financeiro com Interface Futurista  
Desenvolvido com Python, PIL, NumPy e Tkinter
