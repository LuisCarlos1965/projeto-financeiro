# SYSFIN v1.0 - Sistema Financeiro Completo

Este projeto contém um sistema financeiro pessoal completo com tela de abertura futurista em 3D e interface web moderna.

## 🚀 Características

### Tela de Abertura (Splash Screen)
- **Design Futurista**: Visual cyberpunk com cores vibrantes (ciano, magenta, roxo)
- **Efeito 3D**: Texto com profundidade e brilho
- **Tamanho Responsivo**: Ocupa 90% da tela automaticamente
- **Barra de Progresso**: Animação de carregamento realística
- **Controles Intuitivos**: ESC, clique ou fechamento automático

### Sistema Web Completo
- **Dashboard Interativo**: Visão geral financeira com gráficos
- **Gestão de Transações**: Adicionar, editar e excluir receitas/despesas
- **Relatórios Visuais**: Gráficos de distribuição e evolução temporal
- **Categorias Personalizáveis**: Organize suas transações
- **Interface Responsiva**: Funciona em desktop, tablet e mobile
- **Tema Cyberpunk**: Design futurista consistente
- **Persistência Local**: Dados salvos no navegador

## 📁 Estrutura do Projeto

### Arquivos Python (Splash Screen)
- `sysfin_splash.jpg` - Imagem da tela de abertura gerada
- `create_splash_screen.py` - Script para gerar a imagem
- `sysfin_splash_display.py` - Script para exibir a tela de abertura
- `demo_sysfin.py` - Demonstração completa do sistema

### Arquivos Web Frontend
- `index.html` - Página principal da aplicação web
- `styles.css` - Estilos CSS com tema cyberpunk/futurista
- `script.js` - JavaScript para funcionalidade completa
- `README.md` - Esta documentação

## 🔧 Instalação e Uso

### Pré-requisitos Web
Apenas um navegador moderno (Chrome, Firefox, Safari, Edge)

### Pré-requisitos Python
```bash
# Ubuntu/Debian
sudo apt update
sudo apt install python3-pil python3-numpy python3-tk

# Ou via pip
pip install -r requirements.txt
```

## 🌐 Como Usar o Sistema Web

### 1. Abrir a Aplicação
```bash
# Simplesmente abra o arquivo index.html em seu navegador
# Ou use um servidor local:
python3 -m http.server 8000
# Em seguida, acesse http://localhost:8000
```

### 2. Funcionalidades Principais

#### Dashboard
- **Saldo Total**: Mostra o saldo atual (receitas - despesas)
- **Receitas/Despesas**: Valores do mês atual
- **Gráfico Financeiro**: Evolução dos últimos 6 meses
- **Transações Recentes**: Lista das últimas 5 transações

#### Gestão de Transações
- **Adicionar**: Clique em "Nova Transação" ou no botão "+"
- **Editar**: Clique no ícone de edição na tabela
- **Excluir**: Clique no ícone de lixeira
- **Filtrar**: Use os filtros de busca, categoria e data

#### Relatórios
- **Distribuição por Categoria**: Gráfico pizza das despesas
- **Evolução Mensal**: Gráfico de linha do saldo ao longo do tempo
- **Período Personalizável**: Selecione diferentes períodos

#### Configurações
- **Gerenciar Categorias**: Adicionar, editar, excluir categorias
- **Exportar Dados**: Download dos dados em formato JSON
- **Limpar Dados**: Reset completo do sistema

## 🐍 Como Usar a Versão Python

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

## 🎨 Personalização

### Cores do Tema
- **Ciano**: `#00ffff` - Texto principal e bordas
- **Magenta**: `#ff00ff` - Elementos de destaque
- **Verde**: `#00ff00` - Receitas e valores positivos
- **Vermelho**: `#ff4444` - Despesas e valores negativos
- **Gradiente**: Azul escuro → Ciano → Roxo → Preto

### Modificações CSS
Para alterar cores, edite o arquivo `styles.css`:
```css
:root {
    --primary-color: #00ffff;
    --secondary-color: #ff00ff;
    --success-color: #00ff00;
    --danger-color: #ff4444;
}
```

### Configurações JavaScript
Para alterar comportamentos, edite `script.js`:
```javascript
// Duração do splash screen (em ms)
const SPLASH_DURATION = 6000;

// Categorias padrão
const DEFAULT_CATEGORIES = [...];
```

## 📱 Recursos Mobile

### Responsividade
- Layout adaptativo para telas pequenas
- Navegação otimizada para touch
- Formulários amigáveis para mobile
- Gráficos escaláveis

### Gestos Suportados
- Toque para navegar
- Swipe para fechar modais
- Long press para ações contextuais

## 💾 Persistência de Dados

### Armazenamento Local
Os dados são salvos automaticamente no navegador usando `localStorage`:
- `sysfin_transactions` - Lista de todas as transações
- `sysfin_categories` - Categorias personalizadas

### Backup e Restore
- **Exportar**: Botão nas configurações gera arquivo JSON
- **Importar**: Cole dados no console do navegador:
```javascript
// Para importar dados
const data = { /* seus dados JSON */ };
localStorage.setItem('sysfin_transactions', JSON.stringify(data.transactions));
localStorage.setItem('sysfin_categories', JSON.stringify(data.categories));
location.reload();
```

## 🔧 Solução de Problemas

### Web Frontend
- **Dados não aparecem**: Verifique se JavaScript está habilitado
- **Gráficos não carregam**: Atualize a página
- **Layout quebrado**: Use navegador atualizado

### Python Version
- **Erro "No module named 'PIL'"**: `sudo apt install python3-pil`
- **Erro "No module named 'numpy'"**: `sudo apt install python3-numpy`
- **Erro "No module named 'tkinter'"**: `sudo apt install python3-tk`
- **Interface gráfica não disponível**: Execute em ambiente com GUI

## 🔄 Integração Python + Web

### Usando Ambos
1. Execute o splash screen Python primeiro
2. Ao fechar, abra automaticamente a versão web
3. Dados podem ser sincronizados via arquivos JSON

### Exemplo de Integração
```python
import webbrowser
from sysfin_splash_display import SysfinSplashScreen

# Mostrar splash screen
splash = SysfinSplashScreen()
splash.show()

# Após splash, abrir versão web
webbrowser.open('index.html')
```

## 🛡️ Segurança

### Dados Locais
- Todos os dados ficam no seu navegador
- Nenhuma informação é enviada para servidores externos
- Use HTTPS em produção para maior segurança

### Backup Regular
- Exporte seus dados regularmente
- Mantenha backups em locais seguros
- Considere criptografia para dados sensíveis

## 🔮 Funcionalidades Futuras

### Planejadas
- [ ] Sincronização em nuvem
- [ ] Aplicativo mobile nativo
- [ ] Integração bancária
- [ ] Análises avançadas com IA
- [ ] Multi-idiomas
- [ ] Temas personalizáveis
- [ ] Orçamentos e metas
- [ ] Notificações

### Contribuições
Sinta-se à vontade para contribuir com:
- Novos recursos
- Correções de bugs
- Melhorias de UI/UX
- Documentação
- Traduções

---

## 📄 Licença

Projeto open source para uso pessoal e educacional.

## 👥 Suporte

Para dúvidas ou sugestões:
- Abra uma issue no repositório
- Consulte a documentação completa
- Verifique a seção de solução de problemas

---

**SYSFIN v1.0** - Sistema Financeiro com Interface Futurista  
Desenvolvido com HTML5, CSS3, JavaScript ES6+ e Python 3.7+

🚀 **Versão Web**: Interface moderna e responsiva  
🐍 **Versão Python**: Splash screen futurista em 3D  
💫 **Design**: Tema cyberpunk com animações suaves 
