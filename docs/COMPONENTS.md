# Documentação de Componentes - Sistema de Controle Financeiro

## Visão Geral

Esta documentação descreve todos os componentes públicos disponíveis no sistema de controle financeiro pessoal. Os componentes são reutilizáveis e seguem as melhores práticas de desenvolvimento frontend.

---

## Componentes de Interface

### TransactionForm

Componente para criar e editar transações financeiras.

**Props:**
```typescript
interface TransactionFormProps {
  initialData?: Transaction;
  onSubmit: (data: TransactionData) => Promise<void>;
  onCancel?: () => void;
  categories: Category[];
  accounts: Account[];
  isLoading?: boolean;
}
```

**Exemplo de Uso:**
```tsx
import { TransactionForm } from '@/components/TransactionForm';

function AddTransactionModal() {
  const [categories, setCategories] = useState([]);
  const [accounts, setAccounts] = useState([]);

  const handleSubmit = async (data) => {
    try {
      await createTransaction(data);
      toast.success('Transação criada com sucesso!');
    } catch (error) {
      toast.error('Erro ao criar transação');
    }
  };

  return (
    <Modal>
      <TransactionForm
        categories={categories}
        accounts={accounts}
        onSubmit={handleSubmit}
        onCancel={() => setModalOpen(false)}
      />
    </Modal>
  );
}
```

**Validações:**
- `description`: Obrigatório, mínimo 3 caracteres
- `amount`: Obrigatório, maior que 0
- `type`: Obrigatório, 'income' ou 'expense'
- `category_id`: Obrigatório
- `date`: Obrigatório, formato válido

---

### TransactionList

Componente para exibir lista de transações com paginação e filtros.

**Props:**
```typescript
interface TransactionListProps {
  transactions: Transaction[];
  loading?: boolean;
  onEdit?: (transaction: Transaction) => void;
  onDelete?: (id: number) => void;
  onLoadMore?: () => void;
  hasMore?: boolean;
  filters?: TransactionFilters;
  onFilterChange?: (filters: TransactionFilters) => void;
}
```

**Exemplo de Uso:**
```tsx
import { TransactionList } from '@/components/TransactionList';

function TransactionsPage() {
  const [transactions, setTransactions] = useState([]);
  const [filters, setFilters] = useState({});
  const [loading, setLoading] = useState(false);

  const handleEdit = (transaction) => {
    setEditingTransaction(transaction);
    setEditModalOpen(true);
  };

  const handleDelete = async (id) => {
    if (confirm('Deseja excluir esta transação?')) {
      await deleteTransaction(id);
      setTransactions(prev => prev.filter(t => t.id !== id));
    }
  };

  return (
    <div>
      <TransactionList
        transactions={transactions}
        loading={loading}
        onEdit={handleEdit}
        onDelete={handleDelete}
        filters={filters}
        onFilterChange={setFilters}
      />
    </div>
  );
}
```

**Recursos:**
- Paginação infinita
- Filtros por data, categoria e tipo
- Busca por descrição
- Ações de editar/excluir
- Estado de loading
- Responsivo

---

### CategorySelector

Componente para seleção de categorias com criação dinâmica.

**Props:**
```typescript
interface CategorySelectorProps {
  value?: number;
  onChange: (categoryId: number) => void;
  type: 'income' | 'expense';
  categories: Category[];
  onCreateCategory?: (category: CreateCategoryData) => Promise<Category>;
  placeholder?: string;
  disabled?: boolean;
}
```

**Exemplo de Uso:**
```tsx
import { CategorySelector } from '@/components/CategorySelector';

function ExpenseForm() {
  const [selectedCategory, setSelectedCategory] = useState(null);
  const [categories, setCategories] = useState([]);

  const handleCreateCategory = async (data) => {
    const newCategory = await createCategory(data);
    setCategories(prev => [...prev, newCategory]);
    return newCategory;
  };

  return (
    <form>
      <CategorySelector
        value={selectedCategory}
        onChange={setSelectedCategory}
        type="expense"
        categories={categories}
        onCreateCategory={handleCreateCategory}
        placeholder="Selecione uma categoria"
      />
    </form>
  );
}
```

**Funcionalidades:**
- Busca e filtro por nome
- Criação rápida de novas categorias
- Ícones e cores personalizadas
- Agrupamento por tipo (receita/despesa)

---

### DateRangePicker

Componente para seleção de período de datas.

**Props:**
```typescript
interface DateRangePickerProps {
  startDate?: Date;
  endDate?: Date;
  onChange: (range: { startDate: Date; endDate: Date }) => void;
  maxDate?: Date;
  minDate?: Date;
  presets?: DateRangePreset[];
  placeholder?: string;
}
```

**Exemplo de Uso:**
```tsx
import { DateRangePicker } from '@/components/DateRangePicker';

function ReportsPage() {
  const [dateRange, setDateRange] = useState({
    startDate: startOfMonth(new Date()),
    endDate: endOfMonth(new Date())
  });

  const presets = [
    { label: 'Este mês', value: 'current-month' },
    { label: 'Mês passado', value: 'last-month' },
    { label: 'Últimos 3 meses', value: 'last-3-months' },
    { label: 'Este ano', value: 'current-year' }
  ];

  return (
    <div>
      <DateRangePicker
        startDate={dateRange.startDate}
        endDate={dateRange.endDate}
        onChange={setDateRange}
        presets={presets}
        placeholder="Selecione o período"
      />
    </div>
  );
}
```

---

### FinancialSummary

Componente para exibir resumo financeiro com métricas principais.

**Props:**
```typescript
interface FinancialSummaryProps {
  summary: {
    totalIncome: number;
    totalExpenses: number;
    netIncome: number;
    transactionCount: number;
  };
  period: {
    startDate: string;
    endDate: string;
  };
  loading?: boolean;
  showComparison?: boolean;
  previousPeriodData?: FinancialSummary;
}
```

**Exemplo de Uso:**
```tsx
import { FinancialSummary } from '@/components/FinancialSummary';

function Dashboard() {
  const [summary, setSummary] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    loadSummary();
  }, []);

  const loadSummary = async () => {
    setLoading(true);
    try {
      const data = await getFinancialSummary({
        startDate: '2024-01-01',
        endDate: '2024-01-31'
      });
      setSummary(data);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="dashboard">
      <FinancialSummary
        summary={summary}
        period={{ startDate: '2024-01-01', endDate: '2024-01-31' }}
        loading={loading}
        showComparison={true}
      />
    </div>
  );
}
```

**Métricas Exibidas:**
- Total de receitas
- Total de despesas
- Resultado líquido
- Número de transações
- Comparação com período anterior (opcional)

---

### CategoryChart

Componente para visualização de gastos por categoria.

**Props:**
```typescript
interface CategoryChartProps {
  data: CategoryData[];
  type: 'pie' | 'donut' | 'bar';
  height?: number;
  colors?: string[];
  showLegend?: boolean;
  showValues?: boolean;
  currency?: string;
}
```

**Exemplo de Uso:**
```tsx
import { CategoryChart } from '@/components/CategoryChart';

function ExpenseAnalysis() {
  const [categoryData, setCategoryData] = useState([]);

  const chartData = categoryData.map(category => ({
    name: category.name,
    value: category.amount,
    color: category.color,
    percentage: category.percentage
  }));

  return (
    <div className="chart-container">
      <h3>Gastos por Categoria</h3>
      <CategoryChart
        data={chartData}
        type="donut"
        height={300}
        showLegend={true}
        showValues={true}
        currency="BRL"
      />
    </div>
  );
}
```

---

### AccountCard

Componente para exibir informações de uma conta.

**Props:**
```typescript
interface AccountCardProps {
  account: Account;
  onEdit?: (account: Account) => void;
  onDelete?: (id: number) => void;
  showActions?: boolean;
  compact?: boolean;
}
```

**Exemplo de Uso:**
```tsx
import { AccountCard } from '@/components/AccountCard';

function AccountsPage() {
  const [accounts, setAccounts] = useState([]);

  const handleEdit = (account) => {
    setEditingAccount(account);
    setEditModalOpen(true);
  };

  const handleDelete = async (id) => {
    await deleteAccount(id);
    setAccounts(prev => prev.filter(a => a.id !== id));
  };

  return (
    <div className="accounts-grid">
      {accounts.map(account => (
        <AccountCard
          key={account.id}
          account={account}
          onEdit={handleEdit}
          onDelete={handleDelete}
          showActions={true}
        />
      ))}
    </div>
  );
}
```

---

## Componentes de Layout

### Sidebar

Componente de navegação lateral.

**Props:**
```typescript
interface SidebarProps {
  isOpen?: boolean;
  onToggle?: () => void;
  user?: User;
  currentPath?: string;
}
```

**Exemplo de Uso:**
```tsx
import { Sidebar } from '@/components/Layout/Sidebar';

function AppLayout({ children }) {
  const [sidebarOpen, setSidebarOpen] = useState(true);
  const user = useAuth();

  return (
    <div className="app-layout">
      <Sidebar
        isOpen={sidebarOpen}
        onToggle={() => setSidebarOpen(!sidebarOpen)}
        user={user}
        currentPath={window.location.pathname}
      />
      <main className={`main-content ${sidebarOpen ? 'with-sidebar' : ''}`}>
        {children}
      </main>
    </div>
  );
}
```

### Header

Componente de cabeçalho da aplicação.

**Props:**
```typescript
interface HeaderProps {
  title?: string;
  user?: User;
  onMenuToggle?: () => void;
  actions?: React.ReactNode;
}
```

---

## Componentes de Formulário

### CurrencyInput

Componente de input para valores monetários.

**Props:**
```typescript
interface CurrencyInputProps {
  value: number;
  onChange: (value: number) => void;
  currency?: string;
  placeholder?: string;
  disabled?: boolean;
  error?: string;
}
```

**Exemplo de Uso:**
```tsx
import { CurrencyInput } from '@/components/Form/CurrencyInput';

function TransactionForm() {
  const [amount, setAmount] = useState(0);

  return (
    <form>
      <CurrencyInput
        value={amount}
        onChange={setAmount}
        currency="BRL"
        placeholder="R$ 0,00"
        error={errors.amount}
      />
    </form>
  );
}
```

**Funcionalidades:**
- Formatação automática para moeda
- Suporte a diferentes moedas
- Validação de entrada
- Controle de decimais

---

### FormField

Componente wrapper para campos de formulário.

**Props:**
```typescript
interface FormFieldProps {
  label: string;
  error?: string;
  required?: boolean;
  children: React.ReactNode;
  helpText?: string;
}
```

**Exemplo de Uso:**
```tsx
import { FormField } from '@/components/Form/FormField';
import { Input } from '@/components/Form/Input';

function UserForm() {
  return (
    <form>
      <FormField
        label="Nome completo"
        required={true}
        error={errors.name}
        helpText="Informe seu nome completo"
      >
        <Input
          type="text"
          value={name}
          onChange={setName}
          placeholder="Digite seu nome"
        />
      </FormField>
    </form>
  );
}
```

---

## Componentes Utilitários

### LoadingSpinner

Componente de loading animado.

**Props:**
```typescript
interface LoadingSpinnerProps {
  size?: 'small' | 'medium' | 'large';
  color?: string;
  text?: string;
}
```

### Toast

Sistema de notificações.

**Métodos:**
```typescript
toast.success(message: string, options?: ToastOptions);
toast.error(message: string, options?: ToastOptions);
toast.warning(message: string, options?: ToastOptions);
toast.info(message: string, options?: ToastOptions);
```

**Exemplo de Uso:**
```tsx
import { toast } from '@/components/Toast';

function saveTransaction(data) {
  try {
    await api.post('/transactions', data);
    toast.success('Transação salva com sucesso!');
  } catch (error) {
    toast.error('Erro ao salvar transação');
  }
}
```

### Modal

Componente de modal reutilizável.

**Props:**
```typescript
interface ModalProps {
  isOpen: boolean;
  onClose: () => void;
  title?: string;
  size?: 'small' | 'medium' | 'large' | 'fullscreen';
  children: React.ReactNode;
  showCloseButton?: boolean;
}
```

---

## Hooks Personalizados

### useTransactions

Hook para gerenciar transações.

```tsx
import { useTransactions } from '@/hooks/useTransactions';

function TransactionsPage() {
  const {
    transactions,
    loading,
    error,
    filters,
    setFilters,
    addTransaction,
    updateTransaction,
    deleteTransaction,
    loadMore,
    hasMore
  } = useTransactions();

  return (
    <div>
      <TransactionList
        transactions={transactions}
        loading={loading}
        onEdit={updateTransaction}
        onDelete={deleteTransaction}
        filters={filters}
        onFilterChange={setFilters}
        onLoadMore={loadMore}
        hasMore={hasMore}
      />
    </div>
  );
}
```

### useFinancialData

Hook para dados financeiros e relatórios.

```tsx
import { useFinancialData } from '@/hooks/useFinancialData';

function Dashboard() {
  const {
    summary,
    categoryData,
    trends,
    loading,
    refresh,
    setDateRange
  } = useFinancialData();

  return (
    <div>
      <FinancialSummary summary={summary} loading={loading} />
      <CategoryChart data={categoryData} />
    </div>
  );
}
```

---

## Tipos TypeScript

### Principais Interfaces

```typescript
interface Transaction {
  id: number;
  description: string;
  amount: number;
  type: 'income' | 'expense';
  category_id: number;
  category: Category;
  account_id: number;
  account: Account;
  date: string;
  created_at: string;
  updated_at: string;
}

interface Category {
  id: number;
  name: string;
  color: string;
  type: 'income' | 'expense';
  icon?: string;
  created_at: string;
}

interface Account {
  id: number;
  name: string;
  type: 'checking' | 'savings' | 'credit' | 'investment';
  balance: number;
  currency: string;
  bank_name?: string;
  created_at: string;
}
```

---

## Temas e Estilos

### Sistema de Temas

O sistema suporta múltiplos temas através de CSS Variables:

```css
:root {
  --primary-color: #3b82f6;
  --secondary-color: #64748b;
  --success-color: #10b981;
  --warning-color: #f59e0b;
  --error-color: #ef4444;
  --background-color: #ffffff;
  --surface-color: #f8fafc;
  --text-primary: #1e293b;
  --text-secondary: #64748b;
}

[data-theme="dark"] {
  --background-color: #0f172a;
  --surface-color: #1e293b;
  --text-primary: #f1f5f9;
  --text-secondary: #94a3b8;
}
```

### Classes Utilitárias

```css
.currency-positive { color: var(--success-color); }
.currency-negative { color: var(--error-color); }
.loading-shimmer { /* animação de loading */ }
.fade-in { /* animação de entrada */ }
.slide-up { /* animação de slide */ }
```

---

## Acessibilidade

Todos os componentes seguem as diretrizes WCAG 2.1:

- **Navegação por teclado**: Todos os elementos interativos são acessíveis via teclado
- **Screen readers**: Uso adequado de ARIA labels e roles
- **Contraste**: Cores seguem os padrões de contraste mínimo
- **Foco visível**: Indicadores claros de foco para navegação

### Exemplo de Implementação:

```tsx
<button
  aria-label="Excluir transação"
  aria-describedby="delete-help"
  onClick={handleDelete}
  className="btn-delete"
>
  <TrashIcon aria-hidden="true" />
</button>
<div id="delete-help" className="sr-only">
  Esta ação não pode ser desfeita
</div>
```

---

## Performance

### Otimizações Implementadas

1. **React.memo**: Componentes otimizados para re-renders
2. **useMemo/useCallback**: Memoização de cálculos e funções
3. **Lazy loading**: Carregamento sob demanda de componentes
4. **Virtual scrolling**: Para listas grandes de transações
5. **Debounce**: Em campos de busca e filtros

### Exemplo de Otimização:

```tsx
const TransactionItem = React.memo(({ transaction, onEdit, onDelete }) => {
  const handleEdit = useCallback(() => {
    onEdit(transaction);
  }, [transaction, onEdit]);

  const formattedAmount = useMemo(() => {
    return formatCurrency(transaction.amount, transaction.currency);
  }, [transaction.amount, transaction.currency]);

  return (
    <div className="transaction-item">
      {/* conteúdo do componente */}
    </div>
  );
});
```

---

## Testes

### Exemplo de Teste de Componente:

```tsx
import { render, screen, fireEvent } from '@testing-library/react';
import { TransactionForm } from '../TransactionForm';

describe('TransactionForm', () => {
  const mockProps = {
    categories: [{ id: 1, name: 'Alimentação', type: 'expense' }],
    accounts: [{ id: 1, name: 'Conta Corrente' }],
    onSubmit: jest.fn(),
    onCancel: jest.fn()
  };

  it('should render form fields correctly', () => {
    render(<TransactionForm {...mockProps} />);
    
    expect(screen.getByLabelText('Descrição')).toBeInTheDocument();
    expect(screen.getByLabelText('Valor')).toBeInTheDocument();
    expect(screen.getByLabelText('Categoria')).toBeInTheDocument();
  });

  it('should call onSubmit with correct data', () => {
    render(<TransactionForm {...mockProps} />);
    
    fireEvent.change(screen.getByLabelText('Descrição'), {
      target: { value: 'Supermercado' }
    });
    
    fireEvent.click(screen.getByText('Salvar'));
    
    expect(mockProps.onSubmit).toHaveBeenCalledWith({
      description: 'Supermercado',
      // ... outros campos
    });
  });
});
```