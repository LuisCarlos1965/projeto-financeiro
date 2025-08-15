# 📚 Documentação - Sistema de Controle Financeiro

Bem-vindo à documentação completa do Sistema de Controle Financeiro Pessoal! Esta página serve como guia de navegação para toda a documentação disponível.

## 📋 Índice da Documentação

### 🚀 Começando

- **[🏠 README Principal](../README.md)** - Visão geral do projeto, instalação e configuração
- **[📖 Guia de Uso](./USAGE_GUIDE.md)** - Tutorial completo com exemplos práticos
- **[⚡ Setup Rápido](#setup-rápido)** - Comece a usar em minutos

### 📖 Documentação Técnica

- **[🔗 API Documentation](./API.md)** - Documentação completa da API REST
- **[🧩 Components](./COMPONENTS.md)** - Componentes React reutilizáveis
- **[⚙️ Functions](./FUNCTIONS.md)** - Funções e utilitários do sistema

### 🎯 Guias Específicos

- **[💼 Para Desenvolvedores](#para-desenvolvedores)** - Guias técnicos
- **[👤 Para Usuários](#para-usuários)** - Guias de uso
- **[🚀 Deploy](#deploy)** - Guias de implantação

---

## ⚡ Setup Rápido

### 1. Instalação em 3 Passos

```bash
# 1. Clone e instale
git clone https://github.com/seu-usuario/projeto-financeiro.git
cd projeto-financeiro && npm install

# 2. Configure o ambiente
cp .env.example .env

# 3. Inicie o projeto
docker-compose up -d
```

### 2. Primeiro Uso

1. **Acesse**: `http://localhost:3000`
2. **Registre-se**: Crie sua conta
3. **Configure**: Adicione suas contas bancárias
4. **Use**: Comece a registrar transações

### 3. Recursos Essenciais

| Funcionalidade | Documentação | Exemplos |
|:---------------|:-------------|:---------|
| 💳 Transações | [API](./API.md#endpoints-de-transações) | [Uso](./USAGE_GUIDE.md#transações) |
| 📊 Relatórios | [API](./API.md#endpoints-de-relatórios) | [Uso](./USAGE_GUIDE.md#relatórios) |
| 🏦 Contas | [API](./API.md#endpoints-de-contas) | [Uso](./USAGE_GUIDE.md#gerenciamento-de-contas) |
| 🎯 Categorias | [API](./API.md#endpoints-de-categorias) | [Uso](./USAGE_GUIDE.md#categorias) |

---

## 💼 Para Desenvolvedores

### 🏗️ Arquitetura

```
Sistema de Controle Financeiro
├── Frontend (React + TypeScript)
│   ├── Components ─→ [Documentação](./COMPONENTS.md)
│   ├── Hooks ─────→ [Documentação](./FUNCTIONS.md#hooks-personalizados)
│   └── Utils ─────→ [Documentação](./FUNCTIONS.md#módulo-de-utilidades)
├── Backend (Node.js + Express)
│   ├── API REST ──→ [Documentação](./API.md)
│   ├── Services ──→ [Documentação](./FUNCTIONS.md)
│   └── Models ────→ [Documentação](./API.md#tipos-typescript)
└── Database (PostgreSQL)
    └── Schema ────→ [Documentação](./API.md#base-de-dados)
```

### 📚 Guias de Desenvolvimento

#### Backend Development
- **[🔗 API REST](./API.md)** - Endpoints, autenticação, exemplos
- **[⚙️ Funções do Sistema](./FUNCTIONS.md)** - Lógica de negócio, validações
- **[🗃️ Banco de Dados](./API.md#base-de-dados)** - Schema, relacionamentos

#### Frontend Development  
- **[🧩 Componentes React](./COMPONENTS.md)** - Props, exemplos, best practices
- **[🎣 Custom Hooks](./FUNCTIONS.md#hooks-personalizados)** - Estado, lógica reutilizável
- **[🎨 Temas e Estilos](./COMPONENTS.md#temas-e-estilos)** - CSS, variáveis, responsividade

#### Integração
- **[🔄 API Client](./FUNCTIONS.md#middleware-e-interceptors)** - Interceptors, cache
- **[📊 Estado Global](./COMPONENTS.md#hooks-personalizados)** - Context, providers
- **[🔐 Autenticação](./API.md#endpoints-de-autenticação)** - JWT, renovação de token

### 🧪 Testes

```bash
# Testes unitários
npm test

# Testes de integração  
npm run test:integration

# Coverage
npm run test:coverage
```

### 📦 Build e Deploy

```bash
# Build de produção
npm run build

# Deploy com Docker
docker-compose -f docker-compose.prod.yml up -d

# Deploy na Vercel
vercel --prod
```

---

## 👤 Para Usuários

### 🎯 Guias de Uso

#### Primeiros Passos
1. **[📋 Configuração Inicial](./USAGE_GUIDE.md#configuração-inicial)**
2. **[🏦 Configurar Contas](./USAGE_GUIDE.md#gerenciamento-de-contas)**
3. **[🎯 Criar Categorias](./USAGE_GUIDE.md#categorias)**
4. **[💳 Registrar Transações](./USAGE_GUIDE.md#transações)**

#### Funcionalidades Avançadas
- **[📊 Relatórios](./USAGE_GUIDE.md#relatórios)** - Análises financeiras
- **[📤 Import/Export](./USAGE_GUIDE.md#importação-e-exportação)** - Planilhas
- **[🎯 Metas](./USAGE_GUIDE.md#casos-de-uso-comuns)** - Orçamento e economia
- **[📈 Tendências](./USAGE_GUIDE.md#análise-de-tendências-de-gastos)** - Padrões de gastos

#### Casos de Uso Práticos
- **[💰 Controle Mensal](./USAGE_GUIDE.md#controle-de-orçamento-mensal)**
- **[🎯 Metas de Economia](./USAGE_GUIDE.md#planejamento-de-meta-de-economia)**
- **[💳 Cartão de Crédito](./USAGE_GUIDE.md#controle-de-cartão-de-crédito)**
- **[🔄 Transferências](./USAGE_GUIDE.md#transferências-entre-contas)**

### 📱 Interface de Usuário

#### Componentes Principais
- **[📊 Dashboard](./COMPONENTS.md#financialsummary)** - Resumo financeiro
- **[💳 Lista de Transações](./COMPONENTS.md#transactionlist)** - Histórico e filtros
- **[📈 Gráficos](./COMPONENTS.md#categorychart)** - Visualizações
- **[📝 Formulários](./COMPONENTS.md#transactionform)** - Criação/edição

#### Recursos de Acessibilidade
- **[♿ Navegação por Teclado](./COMPONENTS.md#acessibilidade)**
- **[🔍 Screen Readers](./COMPONENTS.md#acessibilidade)**
- **[🎨 Alto Contraste](./COMPONENTS.md#temas-e-estilos)**

---

## 🚀 Deploy

### ☁️ Cloud Providers

#### Frontend
- **[▲ Vercel](https://vercel.com/)** - Deploy automático
- **[🌐 Netlify](https://netlify.com/)** - JAMstack hosting
- **[🏗️ AWS Amplify](https://aws.amazon.com/amplify/)** - Full-stack

#### Backend
- **[🚂 Railway](https://railway.app/)** - Deploy simples
- **[🟣 Heroku](https://heroku.com/)** - Platform as a Service
- **[☁️ AWS EC2](https://aws.amazon.com/ec2/)** - Infraestrutura

#### Database
- **[🐘 Supabase](https://supabase.com/)** - PostgreSQL gerenciado
- **[🌊 PlanetScale](https://planetscale.com/)** - MySQL serverless
- **[🔺 Neon](https://neon.tech/)** - PostgreSQL serverless

### 🐳 Docker

```yaml
# docker-compose.yml
version: '3.8'
services:
  app:
    build: .
    ports:
      - "3000:3000"
    environment:
      - DATABASE_URL=${DATABASE_URL}
      - JWT_SECRET=${JWT_SECRET}
  
  db:
    image: postgres:15
    environment:
      POSTGRES_DB: financeiro
      POSTGRES_USER: usuario
      POSTGRES_PASSWORD: senha
```

### 🔧 Configuração de Ambiente

```env
# Produção
NODE_ENV=production
DATABASE_URL=postgresql://...
JWT_SECRET=seu_jwt_secret_seguro
REDIS_URL=redis://...

# Monitoramento
SENTRY_DSN=https://...
ANALYTICS_ID=GA_MEASUREMENT_ID
```

---

## 🔍 Referência Rápida

### 📡 Endpoints Principais

```bash
# Autenticação
POST /api/v1/auth/login
POST /api/v1/auth/register

# Transações
GET    /api/v1/transactions
POST   /api/v1/transactions
PUT    /api/v1/transactions/:id
DELETE /api/v1/transactions/:id

# Relatórios
GET /api/v1/reports/summary
GET /api/v1/reports/category-trends
```

### 🧩 Componentes Essenciais

```typescript
// Formulário de transação
<TransactionForm 
  onSubmit={handleSubmit}
  categories={categories}
  accounts={accounts}
/>

// Lista de transações
<TransactionList
  transactions={transactions}
  onEdit={handleEdit}
  onDelete={handleDelete}
/>

// Resumo financeiro
<FinancialSummary
  summary={summary}
  loading={loading}
/>
```

### ⚙️ Funções Úteis

```typescript
// Criar transação
const transaction = await createTransaction(data);

// Obter resumo
const summary = await getFinancialSummary(params);

// Formatar moeda
const formatted = formatCurrency(amount, 'BRL');
```

---

## 🆘 Ajuda e Suporte

### 📖 Documentação Adicional

- **[❓ FAQ](./USAGE_GUIDE.md#solução-de-problemas)** - Perguntas frequentes
- **[🐛 Troubleshooting](./USAGE_GUIDE.md#solução-de-problemas)** - Resolução de problemas
- **[💡 Best Practices](./USAGE_GUIDE.md#dicas-e-melhores-práticas)** - Melhores práticas

### 🤝 Comunidade

- **[💬 Discussions](https://github.com/seu-usuario/projeto-financeiro/discussions)** - Discussões
- **[🐛 Issues](https://github.com/seu-usuario/projeto-financeiro/issues)** - Bugs e sugestões
- **[📧 Email](mailto:suporte@projeto-financeiro.com)** - Suporte direto

### 🔗 Links Úteis

- **[🏠 Site Principal](https://projeto-financeiro.com)** - Homepage
- **[📈 Demo](https://demo.projeto-financeiro.com)** - Demonstração
- **[📊 Status](https://status.projeto-financeiro.com)** - Status dos serviços

---

## 📋 Checklist de Documentação

### ✅ Completo
- [x] Documentação da API REST
- [x] Componentes React
- [x] Funções e utilitários
- [x] Guia de uso completo
- [x] README principal
- [x] Setup e instalação

### 🚧 Em Desenvolvimento
- [ ] Tutoriais em vídeo
- [ ] Exemplos de integração
- [ ] Guias de migração
- [ ] API changelog

### 📅 Planejado
- [ ] Documentação da API mobile
- [ ] Guias de customização
- [ ] Exemplos avançados
- [ ] Documentação i18n

---

<div align="center">

## 🎯 Navegação Rápida

| **Documentação** | **Descrição** | **Público** |
|:----------------|:-------------|:-----------|
| [🔗 API](./API.md) | REST API completa | Desenvolvedores |
| [🧩 Components](./COMPONENTS.md) | Componentes React | Frontend |
| [⚙️ Functions](./FUNCTIONS.md) | Funções do sistema | Desenvolvedores |
| [📖 Usage Guide](./USAGE_GUIDE.md) | Guia prático | Usuários |

**[⬆️ Voltar ao Topo](#-documentação---sistema-de-controle-financeiro)** • 
**[🏠 README Principal](../README.md)** • 
**[🚀 Demo](https://demo.projeto-financeiro.com)**

---

**Feito com ❤️ pela equipe do Projeto Financeiro**

</div>