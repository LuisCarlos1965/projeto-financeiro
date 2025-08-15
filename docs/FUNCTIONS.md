# Documentação de Funções - Sistema de Controle Financeiro

## Visão Geral

Esta documentação descreve todas as funções públicas e utilitárias disponíveis no sistema de controle financeiro pessoal. As funções estão organizadas por módulos e incluem exemplos práticos de uso.

---

## Módulo de Transações

### createTransaction()

Cria uma nova transação financeira.

**Assinatura:**
```typescript
function createTransaction(data: CreateTransactionData): Promise<Transaction>
```

**Parâmetros:**
- `data` (CreateTransactionData): Dados da transação a ser criada

**Retorno:**
- `Promise<Transaction>`: Promise que resolve com a transação criada

**Exemplo de Uso:**
```typescript
import { createTransaction } from '@/lib/transactions';

async function handleCreateTransaction() {
  try {
    const transaction = await createTransaction({
      description: 'Supermercado ABC',
      amount: 125.50,
      type: 'expense',
      category_id: 2,
      account_id: 1,
      date: '2024-01-15'
    });
    
    console.log('Transação criada:', transaction);
    return transaction;
  } catch (error) {
    console.error('Erro ao criar transação:', error);
    throw error;
  }
}
```

**Validações:**
- `description`: Obrigatório, 3-255 caracteres
- `amount`: Obrigatório, maior que 0
- `type`: Obrigatório, 'income' ou 'expense'
- `category_id`: Obrigatório, categoria deve existir
- `account_id`: Opcional, conta deve existir se fornecida
- `date`: Obrigatório, formato YYYY-MM-DD

---

### updateTransaction()

Atualiza uma transação existente.

**Assinatura:**
```typescript
function updateTransaction(id: number, data: UpdateTransactionData): Promise<Transaction>
```

**Parâmetros:**
- `id` (number): ID da transação a ser atualizada
- `data` (UpdateTransactionData): Dados a serem atualizados

**Exemplo de Uso:**
```typescript
import { updateTransaction } from '@/lib/transactions';

async function handleUpdateTransaction(transactionId: number) {
  try {
    const updatedTransaction = await updateTransaction(transactionId, {
      description: 'Supermercado ABC - Atualizado',
      amount: 135.75
    });
    
    console.log('Transação atualizada:', updatedTransaction);
    return updatedTransaction;
  } catch (error) {
    console.error('Erro ao atualizar transação:', error);
    throw error;
  }
}
```

---

### deleteTransaction()

Remove uma transação.

**Assinatura:**
```typescript
function deleteTransaction(id: number): Promise<void>
```

**Parâmetros:**
- `id` (number): ID da transação a ser removida

**Exemplo de Uso:**
```typescript
import { deleteTransaction } from '@/lib/transactions';

async function handleDeleteTransaction(transactionId: number) {
  try {
    await deleteTransaction(transactionId);
    console.log('Transação removida com sucesso');
  } catch (error) {
    console.error('Erro ao remover transação:', error);
    throw error;
  }
}
```

---

### getTransactions()

Obtém lista de transações com filtros e paginação.

**Assinatura:**
```typescript
function getTransactions(params?: GetTransactionsParams): Promise<PaginatedTransactions>
```

**Parâmetros:**
- `params` (GetTransactionsParams, opcional): Parâmetros de filtro e paginação

**Exemplo de Uso:**
```typescript
import { getTransactions } from '@/lib/transactions';

async function loadTransactions() {
  try {
    const result = await getTransactions({
      page: 1,
      limit: 20,
      type: 'expense',
      start_date: '2024-01-01',
      end_date: '2024-01-31',
      category_id: 2,
      search: 'supermercado'
    });
    
    console.log('Transações:', result.data);
    console.log('Total de páginas:', result.pagination.total_pages);
    
    return result;
  } catch (error) {
    console.error('Erro ao carregar transações:', error);
    throw error;
  }
}
```

---

### getTransactionById()

Obtém uma transação específica pelo ID.

**Assinatura:**
```typescript
function getTransactionById(id: number): Promise<Transaction>
```

**Exemplo de Uso:**
```typescript
import { getTransactionById } from '@/lib/transactions';

async function loadTransaction(id: number) {
  try {
    const transaction = await getTransactionById(id);
    console.log('Transação encontrada:', transaction);
    return transaction;
  } catch (error) {
    console.error('Transação não encontrada:', error);
    throw error;
  }
}
```

---

## Módulo de Categorias

### getCategories()

Obtém todas as categorias disponíveis.

**Assinatura:**
```typescript
function getCategories(type?: 'income' | 'expense'): Promise<Category[]>
```

**Parâmetros:**
- `type` (string, opcional): Filtrar por tipo de categoria

**Exemplo de Uso:**
```typescript
import { getCategories } from '@/lib/categories';

async function loadCategories() {
  try {
    // Carregar todas as categorias
    const allCategories = await getCategories();
    
    // Carregar apenas categorias de despesa
    const expenseCategories = await getCategories('expense');
    
    console.log('Todas as categorias:', allCategories);
    console.log('Categorias de despesa:', expenseCategories);
    
    return { allCategories, expenseCategories };
  } catch (error) {
    console.error('Erro ao carregar categorias:', error);
    throw error;
  }
}
```

---

### createCategory()

Cria uma nova categoria.

**Assinatura:**
```typescript
function createCategory(data: CreateCategoryData): Promise<Category>
```

**Parâmetros:**
- `data` (CreateCategoryData): Dados da categoria a ser criada

**Exemplo de Uso:**
```typescript
import { createCategory } from '@/lib/categories';

async function handleCreateCategory() {
  try {
    const category = await createCategory({
      name: 'Educação',
      color: '#9C27B0',
      type: 'expense',
      icon: 'school'
    });
    
    console.log('Categoria criada:', category);
    return category;
  } catch (error) {
    console.error('Erro ao criar categoria:', error);
    throw error;
  }
}
```

**Validações:**
- `name`: Obrigatório, 2-50 caracteres, único por tipo
- `color`: Obrigatório, formato hexadecimal válido
- `type`: Obrigatório, 'income' ou 'expense'
- `icon`: Opcional, nome do ícone válido

---

### updateCategory()

Atualiza uma categoria existente.

**Assinatura:**
```typescript
function updateCategory(id: number, data: UpdateCategoryData): Promise<Category>
```

---

### deleteCategory()

Remove uma categoria (apenas se não possuir transações).

**Assinatura:**
```typescript
function deleteCategory(id: number): Promise<void>
```

**Exemplo de Uso:**
```typescript
import { deleteCategory } from '@/lib/categories';

async function handleDeleteCategory(categoryId: number) {
  try {
    await deleteCategory(categoryId);
    console.log('Categoria removida com sucesso');
  } catch (error) {
    if (error.code === 'CATEGORY_HAS_TRANSACTIONS') {
      console.error('Não é possível excluir categoria com transações');
    } else {
      console.error('Erro ao remover categoria:', error);
    }
    throw error;
  }
}
```

---

## Módulo de Contas

### getAccounts()

Obtém todas as contas do usuário.

**Assinatura:**
```typescript
function getAccounts(): Promise<Account[]>
```

**Exemplo de Uso:**
```typescript
import { getAccounts } from '@/lib/accounts';

async function loadUserAccounts() {
  try {
    const accounts = await getAccounts();
    
    console.log('Contas do usuário:', accounts);
    
    // Calcular saldo total
    const totalBalance = accounts.reduce((sum, account) => sum + account.balance, 0);
    console.log('Saldo total:', totalBalance);
    
    return accounts;
  } catch (error) {
    console.error('Erro ao carregar contas:', error);
    throw error;
  }
}
```

---

### createAccount()

Cria uma nova conta.

**Assinatura:**
```typescript
function createAccount(data: CreateAccountData): Promise<Account>
```

**Exemplo de Uso:**
```typescript
import { createAccount } from '@/lib/accounts';

async function handleCreateAccount() {
  try {
    const account = await createAccount({
      name: 'Conta Poupança',
      type: 'savings',
      initial_balance: 1500.00,
      currency: 'BRL',
      bank_name: 'Banco Itaú'
    });
    
    console.log('Conta criada:', account);
    return account;
  } catch (error) {
    console.error('Erro ao criar conta:', error);
    throw error;
  }
}
```

**Validações:**
- `name`: Obrigatório, 2-100 caracteres
- `type`: Obrigatório, 'checking', 'savings', 'credit', 'investment'
- `initial_balance`: Opcional, padrão 0
- `currency`: Opcional, padrão 'BRL'
- `bank_name`: Opcional, máximo 100 caracteres

---

### updateAccount()

Atualiza uma conta existente.

**Assinatura:**
```typescript
function updateAccount(id: number, data: UpdateAccountData): Promise<Account>
```

---

### deleteAccount()

Remove uma conta (apenas se não possuir transações).

**Assinatura:**
```typescript
function deleteAccount(id: number): Promise<void>
```

---

### getAccountBalance()

Obtém o saldo atual de uma conta.

**Assinatura:**
```typescript
function getAccountBalance(accountId: number, date?: string): Promise<number>
```

**Parâmetros:**
- `accountId` (number): ID da conta
- `date` (string, opcional): Data para cálculo do saldo (YYYY-MM-DD)

**Exemplo de Uso:**
```typescript
import { getAccountBalance } from '@/lib/accounts';

async function checkAccountBalance(accountId: number) {
  try {
    // Saldo atual
    const currentBalance = await getAccountBalance(accountId);
    
    // Saldo em uma data específica
    const balanceAtDate = await getAccountBalance(accountId, '2024-01-15');
    
    console.log('Saldo atual:', currentBalance);
    console.log('Saldo em 15/01:', balanceAtDate);
    
    return { currentBalance, balanceAtDate };
  } catch (error) {
    console.error('Erro ao consultar saldo:', error);
    throw error;
  }
}
```

---

## Módulo de Relatórios

### getFinancialSummary()

Obtém resumo financeiro de um período.

**Assinatura:**
```typescript
function getFinancialSummary(params: SummaryParams): Promise<FinancialSummary>
```

**Parâmetros:**
- `params` (SummaryParams): Parâmetros do relatório

**Exemplo de Uso:**
```typescript
import { getFinancialSummary } from '@/lib/reports';

async function generateMonthlySummary() {
  try {
    const summary = await getFinancialSummary({
      start_date: '2024-01-01',
      end_date: '2024-01-31',
      account_id: 1 // opcional
    });
    
    console.log('Resumo financeiro:', {
      receitas: summary.total_income,
      despesas: summary.total_expenses,
      resultado: summary.net_income,
      transacoes: summary.transaction_count
    });
    
    // Análise por categoria
    summary.by_category.expenses.forEach(category => {
      console.log(`${category.category_name}: R$ ${category.amount} (${category.percentage}%)`);
    });
    
    return summary;
  } catch (error) {
    console.error('Erro ao gerar relatório:', error);
    throw error;
  }
}
```

---

### getCategoryTrends()

Obtém tendências de gastos por categoria.

**Assinatura:**
```typescript
function getCategoryTrends(params: TrendsParams): Promise<CategoryTrend[]>
```

**Exemplo de Uso:**
```typescript
import { getCategoryTrends } from '@/lib/reports';

async function analyzeCategoryTrends() {
  try {
    const trends = await getCategoryTrends({
      start_date: '2024-01-01',
      end_date: '2024-03-31',
      type: 'expense',
      period: 'monthly'
    });
    
    trends.forEach(trend => {
      console.log(`Categoria: ${trend.category_name}`);
      console.log(`Tendência: ${trend.trend > 0 ? 'Crescimento' : 'Redução'} de ${Math.abs(trend.trend)}%`);
      console.log(`Média mensal: R$ ${trend.average_amount}`);
    });
    
    return trends;
  } catch (error) {
    console.error('Erro ao analisar tendências:', error);
    throw error;
  }
}
```

---

### getMonthlyComparison()

Compara dados financeiros entre meses.

**Assinatura:**
```typescript
function getMonthlyComparison(params: ComparisonParams): Promise<MonthlyComparison>
```

**Exemplo de Uso:**
```typescript
import { getMonthlyComparison } from '@/lib/reports';

async function compareMonths() {
  try {
    const comparison = await getMonthlyComparison({
      current_month: '2024-02',
      previous_month: '2024-01'
    });
    
    console.log('Comparação mensal:', {
      receitas: {
        atual: comparison.current.total_income,
        anterior: comparison.previous.total_income,
        variacao: comparison.income_change_percentage
      },
      despesas: {
        atual: comparison.current.total_expenses,
        anterior: comparison.previous.total_expenses,
        variacao: comparison.expenses_change_percentage
      }
    });
    
    return comparison;
  } catch (error) {
    console.error('Erro na comparação:', error);
    throw error;
  }
}
```

---

## Módulo de Autenticação

### login()

Realiza autenticação do usuário.

**Assinatura:**
```typescript
function login(credentials: LoginCredentials): Promise<AuthResponse>
```

**Parâmetros:**
- `credentials` (LoginCredentials): Email e senha do usuário

**Exemplo de Uso:**
```typescript
import { login } from '@/lib/auth';

async function handleLogin(email: string, password: string) {
  try {
    const response = await login({ email, password });
    
    // Armazenar token
    localStorage.setItem('auth_token', response.token);
    
    console.log('Login realizado com sucesso:', response.user);
    return response;
  } catch (error) {
    console.error('Erro no login:', error);
    throw error;
  }
}
```

---

### register()

Registra um novo usuário.

**Assinatura:**
```typescript
function register(userData: RegisterData): Promise<AuthResponse>
```

**Exemplo de Uso:**
```typescript
import { register } from '@/lib/auth';

async function handleRegister() {
  try {
    const response = await register({
      name: 'João Silva',
      email: 'joao@exemplo.com',
      password: 'senha123',
      password_confirmation: 'senha123'
    });
    
    console.log('Usuário registrado:', response.user);
    return response;
  } catch (error) {
    console.error('Erro no registro:', error);
    throw error;
  }
}
```

---

### logout()

Realiza logout do usuário.

**Assinatura:**
```typescript
function logout(): Promise<void>
```

**Exemplo de Uso:**
```typescript
import { logout } from '@/lib/auth';

async function handleLogout() {
  try {
    await logout();
    localStorage.removeItem('auth_token');
    console.log('Logout realizado com sucesso');
  } catch (error) {
    console.error('Erro no logout:', error);
  }
}
```

---

### refreshToken()

Renova o token de acesso.

**Assinatura:**
```typescript
function refreshToken(): Promise<string>
```

---

### getCurrentUser()

Obtém dados do usuário autenticado.

**Assinatura:**
```typescript
function getCurrentUser(): Promise<User>
```

---

## Módulo de Validação

### validateTransactionData()

Valida dados de transação.

**Assinatura:**
```typescript
function validateTransactionData(data: any): ValidationResult<TransactionData>
```

**Exemplo de Uso:**
```typescript
import { validateTransactionData } from '@/lib/validation';

function processTransactionForm(formData: any) {
  const validation = validateTransactionData(formData);
  
  if (!validation.isValid) {
    console.error('Dados inválidos:', validation.errors);
    return;
  }
  
  // Dados válidos, prosseguir com criação
  createTransaction(validation.data);
}
```

---

### validateCategoryData()

Valida dados de categoria.

**Assinatura:**
```typescript
function validateCategoryData(data: any): ValidationResult<CategoryData>
```

---

### validateAccountData()

Valida dados de conta.

**Assinatura:**
```typescript
function validateAccountData(data: any): ValidationResult<AccountData>
```

---

## Módulo de Formatação

### formatCurrency()

Formata valores monetários.

**Assinatura:**
```typescript
function formatCurrency(amount: number, currency?: string, locale?: string): string
```

**Parâmetros:**
- `amount` (number): Valor a ser formatado
- `currency` (string, opcional): Código da moeda (padrão: 'BRL')
- `locale` (string, opcional): Locale para formatação (padrão: 'pt-BR')

**Exemplo de Uso:**
```typescript
import { formatCurrency } from '@/lib/format';

function displayTransactionAmount(transaction: Transaction) {
  const formattedAmount = formatCurrency(transaction.amount, 'BRL');
  console.log('Valor formatado:', formattedAmount); // "R$ 1.234,56"
  
  // Para outras moedas
  const usdAmount = formatCurrency(100, 'USD', 'en-US'); // "$100.00"
  const eurAmount = formatCurrency(100, 'EUR', 'de-DE'); // "100,00 €"
  
  return formattedAmount;
}
```

---

### formatDate()

Formata datas.

**Assinatura:**
```typescript
function formatDate(date: string | Date, format?: string): string
```

**Parâmetros:**
- `date` (string | Date): Data a ser formatada
- `format` (string, opcional): Formato desejado (padrão: 'dd/MM/yyyy')

**Exemplo de Uso:**
```typescript
import { formatDate } from '@/lib/format';

function displayTransactionDate(transaction: Transaction) {
  const shortDate = formatDate(transaction.date); // "15/01/2024"
  const longDate = formatDate(transaction.date, 'dd MMMM yyyy'); // "15 janeiro 2024"
  const isoDate = formatDate(transaction.date, 'yyyy-MM-dd'); // "2024-01-15"
  
  return shortDate;
}
```

---

### formatPercentage()

Formata valores percentuais.

**Assinatura:**
```typescript
function formatPercentage(value: number, decimals?: number): string
```

**Exemplo de Uso:**
```typescript
import { formatPercentage } from '@/lib/format';

function displayCategoryPercentage(category: CategoryData) {
  const percentage = formatPercentage(category.percentage, 1); // "25.5%"
  console.log(`${category.name}: ${percentage}`);
  return percentage;
}
```

---

## Módulo de Utilidades

### calculateCategoryPercentages()

Calcula percentuais de categorias.

**Assinatura:**
```typescript
function calculateCategoryPercentages(categories: CategoryData[]): CategoryData[]
```

**Exemplo de Uso:**
```typescript
import { calculateCategoryPercentages } from '@/lib/utils';

async function generateCategoryReport() {
  const rawCategoryData = await getCategoryData();
  const categoriesWithPercentages = calculateCategoryPercentages(rawCategoryData);
  
  categoriesWithPercentages.forEach(category => {
    console.log(`${category.name}: ${category.percentage}%`);
  });
  
  return categoriesWithPercentages;
}
```

---

### groupTransactionsByDate()

Agrupa transações por data.

**Assinatura:**
```typescript
function groupTransactionsByDate(transactions: Transaction[], groupBy: 'day' | 'month' | 'year'): GroupedTransactions
```

**Exemplo de Uso:**
```typescript
import { groupTransactionsByDate } from '@/lib/utils';

function analyzeTransactionsByMonth(transactions: Transaction[]) {
  const groupedByMonth = groupTransactionsByDate(transactions, 'month');
  
  Object.entries(groupedByMonth).forEach(([month, monthTransactions]) => {
    const totalAmount = monthTransactions.reduce((sum, t) => sum + t.amount, 0);
    console.log(`${month}: ${monthTransactions.length} transações, total: R$ ${totalAmount}`);
  });
  
  return groupedByMonth;
}
```

---

### calculateNetWorth()

Calcula patrimônio líquido.

**Assinatura:**
```typescript
function calculateNetWorth(accounts: Account[]): NetWorthCalculation
```

**Exemplo de Uso:**
```typescript
import { calculateNetWorth } from '@/lib/utils';

async function getNetWorthReport() {
  const accounts = await getAccounts();
  const netWorth = calculateNetWorth(accounts);
  
  console.log('Relatório de Patrimônio:', {
    total: netWorth.total,
    porTipo: netWorth.byAccountType,
    crescimento: netWorth.growth_percentage
  });
  
  return netWorth;
}
```

---

### exportToCSV()

Exporta dados para CSV.

**Assinatura:**
```typescript
function exportToCSV<T>(data: T[], filename: string, columns?: string[]): void
```

**Exemplo de Uso:**
```typescript
import { exportToCSV } from '@/lib/utils';

async function exportTransactions() {
  const transactions = await getTransactions({ limit: 1000 });
  
  exportToCSV(
    transactions.data,
    'transacoes-janeiro-2024.csv',
    ['date', 'description', 'amount', 'type', 'category.name']
  );
  
  console.log('Exportação concluída');
}
```

---

### importFromCSV()

Importa dados de CSV.

**Assinatura:**
```typescript
function importFromCSV(file: File, mapping: CSVMapping): Promise<ImportResult>
```

**Exemplo de Uso:**
```typescript
import { importFromCSV } from '@/lib/utils';

async function handleFileImport(file: File) {
  try {
    const result = await importFromCSV(file, {
      description: 'Descrição',
      amount: 'Valor',
      date: 'Data',
      category: 'Categoria'
    });
    
    console.log('Importação concluída:', {
      sucesso: result.successful_imports,
      erros: result.failed_imports,
      total: result.total_records
    });
    
    return result;
  } catch (error) {
    console.error('Erro na importação:', error);
    throw error;
  }
}
```

---

## Módulo de Cache

### cacheGet()

Obtém dados do cache.

**Assinatura:**
```typescript
function cacheGet<T>(key: string): Promise<T | null>
```

---

### cacheSet()

Armazena dados no cache.

**Assinatura:**
```typescript
function cacheSet<T>(key: string, data: T, ttl?: number): Promise<void>
```

---

### cacheInvalidate()

Invalida cache por padrão.

**Assinatura:**
```typescript
function cacheInvalidate(pattern: string): Promise<void>
```

**Exemplo de Uso:**
```typescript
import { cacheGet, cacheSet, cacheInvalidate } from '@/lib/cache';

async function getCachedTransactions() {
  const cacheKey = 'transactions:recent';
  
  // Tentar obter do cache
  let transactions = await cacheGet<Transaction[]>(cacheKey);
  
  if (!transactions) {
    // Não encontrou no cache, buscar da API
    const result = await getTransactions({ limit: 50 });
    transactions = result.data;
    
    // Armazenar no cache por 5 minutos
    await cacheSet(cacheKey, transactions, 300);
  }
  
  return transactions;
}

// Invalidar cache após criar transação
async function createTransactionWithCache(data: CreateTransactionData) {
  const transaction = await createTransaction(data);
  
  // Invalidar caches relacionados
  await cacheInvalidate('transactions:*');
  await cacheInvalidate('summary:*');
  
  return transaction;
}
```

---

## Middleware e Interceptors

### apiInterceptor()

Intercepta requisições HTTP para adicionar autenticação.

**Exemplo de Configuração:**
```typescript
import axios from 'axios';
import { apiInterceptor } from '@/lib/interceptors';

// Configurar interceptor
apiInterceptor(axios);

// Agora todas as requisições incluirão automaticamente:
// - Header de autorização
// - Tratamento de erros
// - Renovação automática de token
```

---

### errorHandler()

Manipulador global de erros.

**Assinatura:**
```typescript
function errorHandler(error: Error, context?: string): void
```

**Exemplo de Uso:**
```typescript
import { errorHandler } from '@/lib/errors';

async function safeTransactionOperation() {
  try {
    return await createTransaction(data);
  } catch (error) {
    errorHandler(error, 'createTransaction');
    // Erro foi logado e tratado automaticamente
    throw error;
  }
}
```

---

## Tipos TypeScript Principais

### Interfaces de Dados

```typescript
interface CreateTransactionData {
  description: string;
  amount: number;
  type: 'income' | 'expense';
  category_id: number;
  account_id?: number;
  date: string;
}

interface GetTransactionsParams {
  page?: number;
  limit?: number;
  type?: 'income' | 'expense';
  category_id?: number;
  account_id?: number;
  start_date?: string;
  end_date?: string;
  search?: string;
}

interface ValidationResult<T> {
  isValid: boolean;
  data?: T;
  errors?: Record<string, string[]>;
}
```

---

## Configuração e Inicialização

### initializeApp()

Inicializa a aplicação com configurações necessárias.

**Assinatura:**
```typescript
function initializeApp(config: AppConfig): Promise<void>
```

**Exemplo de Uso:**
```typescript
import { initializeApp } from '@/lib/app';

async function bootstrap() {
  await initializeApp({
    apiBaseUrl: process.env.REACT_APP_API_URL,
    enableCache: true,
    logLevel: 'info',
    features: {
      enableReports: true,
      enableExport: true,
      enableImport: true
    }
  });
  
  console.log('Aplicação inicializada com sucesso');
}
```

---

## Práticas Recomendadas

### 1. Tratamento de Erros

```typescript
// ✅ Bom: Tratamento específico de erros
try {
  await createTransaction(data);
} catch (error) {
  if (error.code === 'VALIDATION_ERROR') {
    // Tratar erro de validação
  } else if (error.code === 'INSUFFICIENT_BALANCE') {
    // Tratar saldo insuficiente
  } else {
    // Erro genérico
    errorHandler(error);
  }
}
```

### 2. Uso de Cache

```typescript
// ✅ Bom: Usar cache para dados que mudam pouco
const categories = await getCachedCategories();

// ✅ Bom: Invalidar cache após mutações
await createCategory(data);
await cacheInvalidate('categories:*');
```

### 3. Validação de Dados

```typescript
// ✅ Bom: Sempre validar antes de enviar
const validation = validateTransactionData(formData);
if (!validation.isValid) {
  showValidationErrors(validation.errors);
  return;
}
```

### 4. Formatação Consistente

```typescript
// ✅ Bom: Usar funções de formatação
const displayAmount = formatCurrency(transaction.amount);
const displayDate = formatDate(transaction.date);
```

---

## Debugging e Logs

### debug()

Função para logs de debug.

**Assinatura:**
```typescript
function debug(message: string, data?: any): void
```

**Exemplo de Uso:**
```typescript
import { debug } from '@/lib/debug';

async function complexOperation() {
  debug('Iniciando operação complexa');
  
  const result = await someOperation();
  debug('Operação concluída', { result });
  
  return result;
}
```

---

Esta documentação fornece uma base sólida para entender e utilizar todas as funções disponíveis no sistema de controle financeiro. Cada função inclui exemplos práticos e orientações de uso para facilitar a implementação.