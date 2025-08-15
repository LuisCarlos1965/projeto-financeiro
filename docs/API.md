# API Documentation - Sistema de Controle Financeiro

## Visão Geral

Esta documentação descreve todas as APIs públicas disponíveis no sistema de controle financeiro pessoal. Todas as APIs seguem os padrões REST e retornam dados no formato JSON.

## Base URL

```
http://localhost:3000/api/v1
```

## Autenticação

Todas as requisições requerem autenticação via Bearer Token:

```
Authorization: Bearer {seu_token_aqui}
```

## Códigos de Status HTTP

- `200` - Sucesso
- `201` - Criado com sucesso
- `400` - Erro na requisição
- `401` - Não autorizado
- `404` - Recurso não encontrado
- `500` - Erro interno do servidor

---

## Endpoints de Transações

### POST /transactions
Cria uma nova transação financeira.

**Parâmetros:**
```json
{
  "description": "string (obrigatório) - Descrição da transação",
  "amount": "number (obrigatório) - Valor da transação",
  "type": "string (obrigatório) - 'income' ou 'expense'",
  "category_id": "number (obrigatório) - ID da categoria",
  "date": "string (obrigatório) - Data no formato YYYY-MM-DD",
  "account_id": "number (opcional) - ID da conta"
}
```

**Exemplo de Requisição:**
```bash
curl -X POST http://localhost:3000/api/v1/transactions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..." \
  -d '{
    "description": "Salário mensal",
    "amount": 5000.00,
    "type": "income",
    "category_id": 1,
    "date": "2024-01-15",
    "account_id": 1
  }'
```

**Resposta de Sucesso (201):**
```json
{
  "success": true,
  "data": {
    "id": 123,
    "description": "Salário mensal",
    "amount": 5000.00,
    "type": "income",
    "category_id": 1,
    "category": {
      "id": 1,
      "name": "Salário",
      "color": "#4CAF50"
    },
    "date": "2024-01-15",
    "account_id": 1,
    "created_at": "2024-01-15T10:30:00Z",
    "updated_at": "2024-01-15T10:30:00Z"
  }
}
```

### GET /transactions
Lista todas as transações do usuário com filtros opcionais.

**Parâmetros de Query:**
- `page` (number, opcional) - Número da página (padrão: 1)
- `limit` (number, opcional) - Itens por página (padrão: 10, máximo: 100)
- `type` (string, opcional) - Filtrar por tipo ('income' ou 'expense')
- `category_id` (number, opcional) - Filtrar por categoria
- `start_date` (string, opcional) - Data inicial (YYYY-MM-DD)
- `end_date` (string, opcional) - Data final (YYYY-MM-DD)
- `search` (string, opcional) - Buscar na descrição

**Exemplo de Requisição:**
```bash
curl -X GET "http://localhost:3000/api/v1/transactions?page=1&limit=20&type=expense&start_date=2024-01-01&end_date=2024-01-31" \
  -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
```

**Resposta de Sucesso (200):**
```json
{
  "success": true,
  "data": {
    "transactions": [
      {
        "id": 124,
        "description": "Supermercado",
        "amount": 250.00,
        "type": "expense",
        "category_id": 2,
        "category": {
          "id": 2,
          "name": "Alimentação",
          "color": "#FF9800"
        },
        "date": "2024-01-20",
        "account_id": 1,
        "created_at": "2024-01-20T14:30:00Z",
        "updated_at": "2024-01-20T14:30:00Z"
      }
    ],
    "pagination": {
      "current_page": 1,
      "total_pages": 5,
      "total_items": 95,
      "items_per_page": 20,
      "has_next": true,
      "has_previous": false
    }
  }
}
```

### GET /transactions/{id}
Obtém uma transação específica pelo ID.

**Exemplo de Requisição:**
```bash
curl -X GET http://localhost:3000/api/v1/transactions/123 \
  -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
```

### PUT /transactions/{id}
Atualiza uma transação existente.

**Parâmetros:** (mesmos do POST, todos opcionais)

**Exemplo de Requisição:**
```bash
curl -X PUT http://localhost:3000/api/v1/transactions/123 \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..." \
  -d '{
    "description": "Salário mensal atualizado",
    "amount": 5500.00
  }'
```

### DELETE /transactions/{id}
Remove uma transação.

**Exemplo de Requisição:**
```bash
curl -X DELETE http://localhost:3000/api/v1/transactions/123 \
  -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
```

---

## Endpoints de Categorias

### GET /categories
Lista todas as categorias disponíveis.

**Resposta de Sucesso (200):**
```json
{
  "success": true,
  "data": [
    {
      "id": 1,
      "name": "Salário",
      "color": "#4CAF50",
      "type": "income",
      "icon": "work",
      "created_at": "2024-01-01T00:00:00Z"
    },
    {
      "id": 2,
      "name": "Alimentação",
      "color": "#FF9800",
      "type": "expense",
      "icon": "restaurant",
      "created_at": "2024-01-01T00:00:00Z"
    }
  ]
}
```

### POST /categories
Cria uma nova categoria.

**Parâmetros:**
```json
{
  "name": "string (obrigatório) - Nome da categoria",
  "color": "string (obrigatório) - Cor em formato hexadecimal",
  "type": "string (obrigatório) - 'income' ou 'expense'",
  "icon": "string (opcional) - Nome do ícone"
}
```

---

## Endpoints de Contas

### GET /accounts
Lista todas as contas do usuário.

**Resposta de Sucesso (200):**
```json
{
  "success": true,
  "data": [
    {
      "id": 1,
      "name": "Conta Corrente",
      "type": "checking",
      "balance": 2500.00,
      "currency": "BRL",
      "bank_name": "Banco do Brasil",
      "created_at": "2024-01-01T00:00:00Z"
    }
  ]
}
```

### POST /accounts
Cria uma nova conta.

**Parâmetros:**
```json
{
  "name": "string (obrigatório) - Nome da conta",
  "type": "string (obrigatório) - 'checking', 'savings', 'credit', 'investment'",
  "initial_balance": "number (opcional) - Saldo inicial",
  "currency": "string (opcional, padrão: 'BRL') - Moeda",
  "bank_name": "string (opcional) - Nome do banco"
}
```

---

## Endpoints de Relatórios

### GET /reports/summary
Obtém resumo financeiro do período.

**Parâmetros de Query:**
- `start_date` (string, obrigatório) - Data inicial (YYYY-MM-DD)
- `end_date` (string, obrigatório) - Data final (YYYY-MM-DD)
- `account_id` (number, opcional) - Filtrar por conta

**Exemplo de Requisição:**
```bash
curl -X GET "http://localhost:3000/api/v1/reports/summary?start_date=2024-01-01&end_date=2024-01-31" \
  -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
```

**Resposta de Sucesso (200):**
```json
{
  "success": true,
  "data": {
    "period": {
      "start_date": "2024-01-01",
      "end_date": "2024-01-31"
    },
    "summary": {
      "total_income": 5000.00,
      "total_expenses": 3200.00,
      "net_income": 1800.00,
      "transaction_count": 25
    },
    "by_category": {
      "income": [
        {
          "category_id": 1,
          "category_name": "Salário",
          "amount": 5000.00,
          "percentage": 100.0
        }
      ],
      "expenses": [
        {
          "category_id": 2,
          "category_name": "Alimentação",
          "amount": 800.00,
          "percentage": 25.0
        },
        {
          "category_id": 3,
          "category_name": "Transporte",
          "amount": 400.00,
          "percentage": 12.5
        }
      ]
    }
  }
}
```

### GET /reports/monthly
Obtém relatório mensal com comparativo.

### GET /reports/category-trends
Obtém tendências de gastos por categoria.

---

## Endpoints de Autenticação

### POST /auth/login
Realiza login do usuário.

**Parâmetros:**
```json
{
  "email": "string (obrigatório) - Email do usuário",
  "password": "string (obrigatório) - Senha do usuário"
}
```

**Exemplo de Requisição:**
```bash
curl -X POST http://localhost:3000/api/v1/auth/login \
  -H "Content-Type: application/json" \
  -d '{
    "email": "usuario@exemplo.com",
    "password": "minhasenha123"
  }'
```

**Resposta de Sucesso (200):**
```json
{
  "success": true,
  "data": {
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
    "user": {
      "id": 1,
      "name": "João Silva",
      "email": "usuario@exemplo.com",
      "created_at": "2024-01-01T00:00:00Z"
    },
    "expires_in": 3600
  }
}
```

### POST /auth/register
Registra um novo usuário.

### POST /auth/refresh
Renova o token de acesso.

### POST /auth/logout
Realiza logout do usuário.

---

## Tratamento de Erros

### Formato de Resposta de Erro

```json
{
  "success": false,
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Dados inválidos fornecidos",
    "details": {
      "amount": ["O valor deve ser maior que zero"],
      "category_id": ["Categoria não encontrada"]
    }
  }
}
```

### Códigos de Erro Comuns

- `VALIDATION_ERROR` - Erro de validação dos dados
- `UNAUTHORIZED` - Token inválido ou expirado
- `FORBIDDEN` - Sem permissão para acessar o recurso
- `NOT_FOUND` - Recurso não encontrado
- `DUPLICATE_ENTRY` - Tentativa de criar registro duplicado
- `INSUFFICIENT_BALANCE` - Saldo insuficiente para a operação

---

## Rate Limiting

- **Limite:** 1000 requisições por hora por usuário
- **Header de resposta:** `X-RateLimit-Remaining: 999`
- **Reset:** `X-RateLimit-Reset: 1640995200`

---

## Versionamento

A API utiliza versionamento por URL. A versão atual é `v1`.

Para garantir compatibilidade, mudanças breaking sempre resultarão em uma nova versão.

---

## Suporte

Para dúvidas sobre a API, consulte a documentação completa ou entre em contato através dos canais oficiais.