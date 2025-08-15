# 💰 Sistema de Controle Financeiro Pessoal

> Uma aplicação completa para gerenciamento de finanças pessoais com interface moderna, relatórios avançados e funcionalidades robustas.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Node.js Version](https://img.shields.io/badge/Node.js-16%2B-green.svg)](https://nodejs.org/)
[![TypeScript](https://img.shields.io/badge/TypeScript-4.8%2B-blue.svg)](https://www.typescriptlang.org/)
[![React](https://img.shields.io/badge/React-18%2B-61dafb.svg)](https://reactjs.org/)

## 📋 Índice

- [Características](#-características)
- [Demonstração](#-demonstração)
- [Instalação Rápida](#-instalação-rápida)
- [Documentação](#-documentação)
- [Tecnologias](#-tecnologias)
- [Estrutura do Projeto](#-estrutura-do-projeto)
- [Funcionalidades Principais](#-funcionalidades-principais)
- [APIs e Integrações](#-apis-e-integrações)
- [Contribuindo](#-contribuindo)
- [Suporte](#-suporte)
- [Licença](#-licença)

## 🚀 Características

### ⭐ Principais Funcionalidades

- 💳 **Gerenciamento de Transações**: Registre receitas e despesas com categorização automática
- 🏦 **Múltiplas Contas**: Gerencie conta corrente, poupança, cartão de crédito e investimentos
- 📊 **Relatórios Avançados**: Análises detalhadas com gráficos interativos
- 🎯 **Controle de Orçamento**: Defina metas e acompanhe seu progresso
- 📈 **Análise de Tendências**: Identifique padrões nos seus gastos
- 📱 **Responsivo**: Interface adaptada para desktop, tablet e mobile
- 🔒 **Seguro**: Autenticação robusta e proteção de dados
- 📤 **Import/Export**: Importe dados de planilhas e exporte relatórios

### 🎨 Interface Moderna

- ✨ Design limpo e intuitivo
- 🌙 Modo escuro/claro
- 📊 Gráficos interativos
- 🎯 Dashboard personalizado
- 📱 PWA (Progressive Web App)

## 🎮 Demonstração

### Screenshots

| Dashboard Principal | Transações | Relatórios |
|:---:|:---:|:---:|
| ![Dashboard](docs/images/dashboard.png) | ![Transactions](docs/images/transactions.png) | ![Reports](docs/images/reports.png) |

### Demo Online

🌐 **[Acesse a demonstração](https://projeto-financeiro-demo.vercel.app)**

- **Usuário demo**: `demo@exemplo.com`
- **Senha**: `demo123`

## ⚡ Instalação Rápida

### Pré-requisitos

- [Node.js 16+](https://nodejs.org/)
- [PostgreSQL](https://www.postgresql.org/) ou [Docker](https://www.docker.com/)

### Opção 1: Instalação Tradicional

```bash
# 1. Clone o repositório
git clone https://github.com/seu-usuario/projeto-financeiro.git
cd projeto-financeiro

# 2. Instale as dependências
npm install

# 3. Configure o ambiente
cp .env.example .env
# Edite o arquivo .env com suas configurações

# 4. Configure o banco de dados
npm run migrate
npm run seed

# 5. Inicie o servidor
npm run dev
```

### Opção 2: Docker (Recomendado)

```bash
# 1. Clone o repositório
git clone https://github.com/seu-usuario/projeto-financeiro.git
cd projeto-financeiro

# 2. Inicie com Docker Compose
docker-compose up -d

# 3. Acesse a aplicação
# Frontend: http://localhost:3000
# API: http://localhost:3001
```

### Configuração de Ambiente

```env
# .env
DATABASE_URL=postgresql://usuario:senha@localhost:5432/financeiro
JWT_SECRET=seu_jwt_secret_aqui
API_BASE_URL=http://localhost:3001
FRONTEND_URL=http://localhost:3000

# Opcionais
REDIS_URL=redis://localhost:6379
SMTP_HOST=smtp.gmail.com
SMTP_USER=seu-email@gmail.com
SMTP_PASS=sua-senha-app
```

## 📚 Documentação

### Documentação Completa

- 🔗 **[API Documentation](docs/API.md)** - Todas as APIs REST com exemplos
- 🧩 **[Components Documentation](docs/COMPONENTS.md)** - Componentes React reutilizáveis
- ⚙️ **[Functions Documentation](docs/FUNCTIONS.md)** - Funções e utilitários
- 📖 **[Usage Guide](docs/USAGE_GUIDE.md)** - Guia prático de uso

### Início Rápido

```typescript
// Exemplo: Criar uma transação
import { createTransaction } from '@/lib/transactions';

const novaTransacao = await createTransaction({
  description: "Salário Janeiro",
  amount: 5000.00,
  type: "income",
  category_id: 1,
  account_id: 1,
  date: "2024-01-05"
});
```

### Arquitetura

```
├── frontend/          # React + TypeScript
│   ├── src/
│   │   ├── components/    # Componentes reutilizáveis
│   │   ├── pages/         # Páginas da aplicação
│   │   ├── hooks/         # Custom hooks
│   │   ├── lib/           # Utilitários e APIs
│   │   └── types/         # Definições TypeScript
│   └── public/
├── backend/           # Node.js + Express
│   ├── src/
│   │   ├── controllers/   # Controladores da API
│   │   ├── models/        # Modelos do banco de dados
│   │   ├── services/      # Lógica de negócio
│   │   ├── middleware/    # Middlewares
│   │   └── routes/        # Rotas da API
│   └── database/
├── docs/              # Documentação
└── docker/            # Configurações Docker
```

## 🛠 Tecnologias

### Frontend
- ⚛️ **React 18** - Interface de usuário
- 📘 **TypeScript** - Tipagem estática
- 🎨 **Tailwind CSS** - Estilização
- 📊 **Recharts** - Gráficos interativos
- 🔄 **React Query** - Gerenciamento de estado do servidor
- 📱 **React Hook Form** - Formulários otimizados

### Backend
- 🟢 **Node.js** - Runtime JavaScript
- ⚡ **Express** - Framework web
- 🗄️ **PostgreSQL** - Banco de dados principal
- ⚡ **Redis** - Cache e sessões
- 🔐 **JWT** - Autenticação
- 📧 **Nodemailer** - Envio de emails

### DevOps & Ferramentas
- 🐳 **Docker** - Containerização
- 🚀 **Vercel/Netlify** - Deploy do frontend
- 🌐 **Railway/Heroku** - Deploy do backend
- 🧪 **Jest** - Testes unitários
- 📝 **ESLint + Prettier** - Qualidade de código

## 📁 Estrutura do Projeto

```
projeto-financeiro/
├── 📱 frontend/
│   ├── 🧩 src/components/
│   │   ├── TransactionForm.tsx
│   │   ├── TransactionList.tsx
│   │   ├── CategoryChart.tsx
│   │   └── FinancialSummary.tsx
│   ├── 📄 src/pages/
│   │   ├── Dashboard.tsx
│   │   ├── Transactions.tsx
│   │   └── Reports.tsx
│   └── 🔧 src/lib/
│       ├── api.ts
│       ├── utils.ts
│       └── validation.ts
├── 🖥️ backend/
│   ├── 🎮 src/controllers/
│   │   ├── authController.ts
│   │   ├── transactionController.ts
│   │   └── reportController.ts
│   ├── 📊 src/models/
│   │   ├── User.ts
│   │   ├── Transaction.ts
│   │   └── Category.ts
│   └── 🔧 src/services/
│       ├── transactionService.ts
│       ├── reportService.ts
│       └── authService.ts
├── 📚 docs/
│   ├── API.md
│   ├── COMPONENTS.md
│   ├── FUNCTIONS.md
│   └── USAGE_GUIDE.md
└── 🐳 docker/
    ├── Dockerfile
    └── docker-compose.yml
```

## 💡 Funcionalidades Principais

### 💳 Gerenciamento de Transações

```typescript
// Criar transação
const transaction = await createTransaction({
  description: "Compra no supermercado",
  amount: 150.75,
  type: "expense",
  category_id: 2,
  date: "2024-01-15"
});

// Buscar transações com filtros
const transactions = await getTransactions({
  start_date: "2024-01-01",
  end_date: "2024-01-31",
  category_id: 2,
  type: "expense"
});
```

### 📊 Relatórios Financeiros

```typescript
// Resumo financeiro do mês
const summary = await getFinancialSummary({
  start_date: "2024-01-01",
  end_date: "2024-01-31"
});

console.log(`Receitas: R$ ${summary.total_income}`);
console.log(`Despesas: R$ ${summary.total_expenses}`);
console.log(`Resultado: R$ ${summary.net_income}`);
```

### 🏦 Gerenciamento de Contas

```typescript
// Criar nova conta
const account = await createAccount({
  name: "Conta Corrente Itaú",
  type: "checking",
  initial_balance: 1500.00,
  bank_name: "Banco Itaú"
});

// Consultar saldo
const balance = await getAccountBalance(account.id);
```

### 🎯 Categorização Inteligente

```typescript
// Categorias personalizadas
const category = await createCategory({
  name: "Delivery de Comida",
  color: "#FF6B35",
  type: "expense",
  icon: "delivery"
});

// Análise por categoria
const categoryAnalysis = await getCategoryTrends({
  start_date: "2024-01-01",
  end_date: "2024-06-30",
  type: "expense"
});
```

## 🔌 APIs e Integrações

### REST API

A aplicação possui uma API REST completa com endpoints para:

- 🔐 **Autenticação**: Login, registro, renovação de token
- 💳 **Transações**: CRUD completo com filtros avançados
- 🏦 **Contas**: Gerenciamento de contas bancárias
- 📊 **Relatórios**: Análises e estatísticas financeiras
- 🎯 **Categorias**: Organização e personalização

### Exemplos de Uso da API

```bash
# Listar transações
curl -X GET "http://localhost:3001/api/v1/transactions" \
  -H "Authorization: Bearer YOUR_TOKEN"

# Criar transação
curl -X POST "http://localhost:3001/api/v1/transactions" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -d '{
    "description": "Salário",
    "amount": 5000.00,
    "type": "income",
    "category_id": 1,
    "date": "2024-01-05"
  }'
```

### Integrações Disponíveis

- 📊 **Exportação**: CSV, Excel, PDF
- 📤 **Importação**: Planilhas, extratos bancários
- 🔄 **APIs Bancárias**: Open Banking (em desenvolvimento)
- 📧 **Email**: Relatórios automáticos
- 📱 **Mobile**: API REST compatível

## 🧪 Testes

### Executar Testes

```bash
# Testes do frontend
cd frontend
npm test

# Testes do backend
cd backend
npm test

# Testes de integração
npm run test:integration

# Coverage
npm run test:coverage
```

### Estrutura de Testes

```
tests/
├── unit/              # Testes unitários
│   ├── components/    # Testes de componentes
│   ├── functions/     # Testes de funções
│   └── services/      # Testes de serviços
├── integration/       # Testes de integração
└── e2e/              # Testes end-to-end
```

## 🚀 Deploy

### Frontend (Vercel)

```bash
# Conecte seu repositório ao Vercel
npm i -g vercel
vercel

# Configure as variáveis de ambiente
vercel env add REACT_APP_API_URL
```

### Backend (Railway)

```bash
# Deploy via Railway CLI
npm i -g @railway/cli
railway login
railway init
railway up
```

### Docker Production

```yaml
# docker-compose.prod.yml
version: '3.8'
services:
  app:
    build: .
    ports:
      - "3000:3000"
    environment:
      - NODE_ENV=production
      - DATABASE_URL=${DATABASE_URL}
```

## 🤝 Contribuindo

Adoramos contribuições! Veja como participar:

### 1. Fork e Clone

```bash
git clone https://github.com/seu-usuario/projeto-financeiro.git
cd projeto-financeiro
```

### 2. Configure o Ambiente

```bash
npm install
cp .env.example .env
npm run dev
```

### 3. Faça suas Alterações

- 🐛 **Bug fixes**: Correções de problemas
- ✨ **Features**: Novas funcionalidades
- 📚 **Docs**: Melhorias na documentação
- 🎨 **Style**: Melhorias de UI/UX

### 4. Submeta um Pull Request

```bash
git checkout -b feature/nova-funcionalidade
git commit -m "feat: adiciona nova funcionalidade"
git push origin feature/nova-funcionalidade
```

### Diretrizes

- 📝 Siga os padrões de código (ESLint + Prettier)
- 🧪 Adicione testes para novas funcionalidades
- 📚 Atualize a documentação quando necessário
- 💬 Use mensagens de commit semânticas

## 📋 Roadmap

### v1.0 ✅
- [x] Gerenciamento básico de transações
- [x] Categorização
- [x] Relatórios básicos
- [x] Autenticação

### v1.1 🚧
- [ ] Metas de orçamento
- [ ] Notificações
- [ ] Modo escuro
- [ ] PWA

### v1.2 📅
- [ ] Open Banking
- [ ] Categorização automática com IA
- [ ] App mobile nativo
- [ ] Sincronização offline

### v2.0 🔮
- [ ] Multi-usuário/família
- [ ] Investimentos avançados
- [ ] Planejamento financeiro
- [ ] API pública

## 🆘 Suporte

### Documentação

- 📖 [Guia de Uso Completo](docs/USAGE_GUIDE.md)
- 🔗 [Documentação da API](docs/API.md)
- 🧩 [Componentes](docs/COMPONENTS.md)

### Comunidade

- 💬 [Discord](https://discord.gg/projeto-financeiro)
- 🐛 [Issues no GitHub](https://github.com/seu-usuario/projeto-financeiro/issues)
- 📧 [Email de Suporte](mailto:suporte@projeto-financeiro.com)

### FAQ

<details>
<summary>Como importar dados de outros sistemas?</summary>

Use a funcionalidade de importação CSV disponível em "Configurações > Importar". Suportamos formatos de diversos bancos brasileiros.
</details>

<details>
<summary>É seguro armazenar dados financeiros?</summary>

Sim! Usamos criptografia de ponta, HTTPS, autenticação JWT e seguimos as melhores práticas de segurança.
</details>

<details>
<summary>Posso usar sem internet?</summary>

Atualmente não, mas estamos desenvolvendo funcionalidades offline para a versão PWA.
</details>

## 🏆 Reconhecimentos

- 🎨 Ícones por [Lucide Icons](https://lucide.dev/)
- 📊 Gráficos por [Recharts](https://recharts.org/)
- 🎯 Inspiração de design por [Dribbble](https://dribbble.com/)

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para detalhes.

```
MIT License

Copyright (c) 2024 Projeto Financeiro

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
```

---

<div align="center">

### ⭐ Se este projeto foi útil, deixe uma estrela!

[![GitHub stars](https://img.shields.io/github/stars/seu-usuario/projeto-financeiro?style=social)](https://github.com/seu-usuario/projeto-financeiro/stargazers)

**Feito com ❤️ por [Seu Nome](https://github.com/seu-usuario)**

[📈 Dashboard](https://projeto-financeiro-demo.vercel.app) • 
[📖 Documentação](docs/) • 
[🐛 Reportar Bug](https://github.com/seu-usuario/projeto-financeiro/issues) • 
[💡 Sugerir Feature](https://github.com/seu-usuario/projeto-financeiro/issues)

</div>
