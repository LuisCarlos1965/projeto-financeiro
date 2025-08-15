# Guia de Uso - Sistema de Controle Financeiro

## Índice

1. [Primeiros Passos](#primeiros-passos)
2. [Configuração Inicial](#configuração-inicial)
3. [Gerenciamento de Contas](#gerenciamento-de-contas)
4. [Categorias](#categorias)
5. [Transações](#transações)
6. [Relatórios](#relatórios)
7. [Importação e Exportação](#importação-e-exportação)
8. [Casos de Uso Comuns](#casos-de-uso-comuns)
9. [Dicas e Melhores Práticas](#dicas-e-melhores-práticas)
10. [Solução de Problemas](#solução-de-problemas)

---

## Primeiros Passos

### 1. Instalação e Configuração

**Pré-requisitos:**
- Node.js 16+ ou Docker
- Banco de dados (PostgreSQL, MySQL ou SQLite)
- Editor de código (recomendado: VS Code)

**Instalação via NPM:**
```bash
# Clone o repositório
git clone https://github.com/seu-usuario/projeto-financeiro.git
cd projeto-financeiro

# Instale as dependências
npm install

# Configure as variáveis de ambiente
cp .env.example .env

# Execute as migrações do banco
npm run migrate

# Inicie o servidor de desenvolvimento
npm run dev
```

**Instalação via Docker:**
```bash
# Clone o repositório
git clone https://github.com/seu-usuario/projeto-financeiro.git
cd projeto-financeiro

# Inicie com Docker Compose
docker-compose up -d
```

### 2. Acesso Inicial

Após a instalação, acesse `http://localhost:3000` e:

1. **Primeira vez**: Clique em "Criar conta" e preencha seus dados
2. **Usuário existente**: Faça login com email e senha

---

## Configuração Inicial

### 1. Criando seu Primeiro Usuário

```typescript
// Exemplo de registro via API
const userData = {
  name: "João Silva",
  email: "joao@exemplo.com",
  password: "senha123",
  password_confirmation: "senha123"
};

const response = await register(userData);
console.log("Usuário criado:", response.user);
```

### 2. Configuração do Perfil

Após o primeiro login, configure seu perfil:

- **Moeda padrão**: BRL, USD, EUR, etc.
- **Idioma**: Português, Inglês, Espanhol
- **Fuso horário**: Sua localização
- **Formato de data**: DD/MM/YYYY ou MM/DD/YYYY

---

## Gerenciamento de Contas

### 1. Criando sua Primeira Conta

As contas representam onde seu dinheiro está guardado (banco, carteira, investimentos).

**Via Interface:**
1. Acesse "Contas" no menu lateral
2. Clique em "Nova Conta"
3. Preencha os dados:
   - Nome: "Conta Corrente Banco do Brasil"
   - Tipo: Conta Corrente
   - Saldo inicial: R$ 1.000,00
   - Banco: Banco do Brasil

**Via API:**
```typescript
const novaConta = await createAccount({
  name: "Conta Corrente Banco do Brasil",
  type: "checking",
  initial_balance: 1000.00,
  currency: "BRL",
  bank_name: "Banco do Brasil"
});
```

### 2. Tipos de Conta

- **Conta Corrente (`checking`)**: Para movimentação diária
- **Poupança (`savings`)**: Para reservas
- **Cartão de Crédito (`credit`)**: Para compras parceladas
- **Investimentos (`investment`)**: Para aplicações

### 3. Exemplo Completo de Setup de Contas

```typescript
// Configuração inicial de contas
const contas = [
  {
    name: "Conta Corrente Principal",
    type: "checking",
    initial_balance: 2500.00,
    bank_name: "Banco Itaú"
  },
  {
    name: "Poupança Reserva",
    type: "savings", 
    initial_balance: 10000.00,
    bank_name: "Banco Itaú"
  },
  {
    name: "Cartão Nubank",
    type: "credit",
    initial_balance: 0.00,
    bank_name: "Nubank"
  }
];

for (const conta of contas) {
  await createAccount(conta);
}
```

---

## Categorias

### 1. Categorias Padrão

O sistema vem com categorias pré-configuradas, mas você pode personalizar:

**Receitas:**
- Salário
- Freelances
- Investimentos
- Outros

**Despesas:**
- Alimentação
- Transporte
- Moradia
- Saúde
- Educação
- Lazer
- Compras

### 2. Criando Categorias Personalizadas

**Via Interface:**
1. Acesse "Categorias"
2. Clique em "Nova Categoria"
3. Defina nome, cor e ícone

**Via Código:**
```typescript
// Criando categoria personalizada
const categoria = await createCategory({
  name: "Pet Shop",
  color: "#FF6B35",
  type: "expense",
  icon: "pets"
});
```

### 3. Exemplo de Organização por Categorias

```typescript
// Estrutura organizacional de categorias
const estruturaCategorias = {
  receitas: [
    { name: "Salário CLT", color: "#4CAF50" },
    { name: "Freelances", color: "#8BC34A" },
    { name: "Renda Extra", color: "#CDDC39" }
  ],
  despesas: {
    essenciais: [
      { name: "Moradia", color: "#F44336" },
      { name: "Alimentação", color: "#FF9800" },
      { name: "Transporte", color: "#FF5722" }
    ],
    pessoais: [
      { name: "Lazer", color: "#9C27B0" },
      { name: "Roupas", color: "#E91E63" },
      { name: "Educação", color: "#3F51B5" }
    ]
  }
};
```

---

## Transações

### 1. Registrando sua Primeira Transação

**Receita (Entrada de dinheiro):**
```typescript
const salario = await createTransaction({
  description: "Salário Janeiro 2024",
  amount: 5000.00,
  type: "income",
  category_id: 1, // Categoria "Salário"
  account_id: 1,  // Conta corrente
  date: "2024-01-05"
});
```

**Despesa (Saída de dinheiro):**
```typescript
const compraSupermercado = await createTransaction({
  description: "Supermercado Atacadão",
  amount: 250.75,
  type: "expense", 
  category_id: 2, // Categoria "Alimentação"
  account_id: 1,  // Conta corrente
  date: "2024-01-10"
});
```

### 2. Transações Recorrentes

Para transações que se repetem mensalmente:

```typescript
// Exemplo: Salário mensal
async function criarSalarioMensal(mes: string) {
  return await createTransaction({
    description: `Salário ${mes}`,
    amount: 5000.00,
    type: "income",
    category_id: 1,
    account_id: 1,
    date: `${mes}-05` // Todo dia 5
  });
}

// Criando para vários meses
const meses = ["2024-01", "2024-02", "2024-03"];
for (const mes of meses) {
  await criarSalarioMensal(mes);
}
```

### 3. Transferências entre Contas

```typescript
// Transferência da conta corrente para poupança
async function transferirParaPoupanca(valor: number, data: string) {
  // Saída da conta corrente
  await createTransaction({
    description: "Transferência para poupança",
    amount: valor,
    type: "expense",
    category_id: getCategoryId("Transferência"),
    account_id: 1, // Conta corrente
    date: data
  });
  
  // Entrada na poupança
  await createTransaction({
    description: "Transferência da conta corrente", 
    amount: valor,
    type: "income",
    category_id: getCategoryId("Transferência"),
    account_id: 2, // Poupança
    date: data
  });
}
```

### 4. Exemplo de Uso Mensal Completo

```typescript
// Simulando um mês completo de transações
async function exemploMesCompleto() {
  // Receitas
  await createTransaction({
    description: "Salário Empresa XYZ",
    amount: 5000.00,
    type: "income",
    category_id: 1,
    account_id: 1,
    date: "2024-01-05"
  });
  
  await createTransaction({
    description: "Freelance Website",
    amount: 800.00,
    type: "income", 
    category_id: 2,
    account_id: 1,
    date: "2024-01-15"
  });
  
  // Despesas essenciais
  const despesasEssenciais = [
    { desc: "Aluguel", valor: 1200.00, cat: "Moradia", data: "2024-01-01" },
    { desc: "Conta de luz", valor: 85.50, cat: "Moradia", data: "2024-01-10" },
    { desc: "Internet", valor: 99.90, cat: "Moradia", data: "2024-01-15" },
    { desc: "Supermercado", valor: 350.00, cat: "Alimentação", data: "2024-01-08" },
    { desc: "Gasolina", valor: 180.00, cat: "Transporte", data: "2024-01-12" }
  ];
  
  for (const despesa of despesasEssenciais) {
    await createTransaction({
      description: despesa.desc,
      amount: despesa.valor,
      type: "expense",
      category_id: getCategoryId(despesa.cat),
      account_id: 1,
      date: despesa.data
    });
  }
  
  // Despesas pessoais
  const despesasPessoais = [
    { desc: "Cinema", valor: 45.00, cat: "Lazer", data: "2024-01-20" },
    { desc: "Restaurante", valor: 120.00, cat: "Alimentação", data: "2024-01-22" },
    { desc: "Curso online", valor: 79.90, cat: "Educação", data: "2024-01-25" }
  ];
  
  for (const despesa of despesasPessoais) {
    await createTransaction({
      description: despesa.desc,
      amount: despesa.valor,
      type: "expense",
      category_id: getCategoryId(despesa.cat),
      account_id: 1,
      date: despesa.data
    });
  }
}
```

---

## Relatórios

### 1. Resumo Financeiro Mensal

```typescript
// Obtendo resumo do mês atual
async function resumoMesAtual() {
  const hoje = new Date();
  const primeiroDia = new Date(hoje.getFullYear(), hoje.getMonth(), 1);
  const ultimoDia = new Date(hoje.getFullYear(), hoje.getMonth() + 1, 0);
  
  const resumo = await getFinancialSummary({
    start_date: primeiroDia.toISOString().split('T')[0],
    end_date: ultimoDia.toISOString().split('T')[0]
  });
  
  console.log("📊 Resumo Financeiro do Mês:");
  console.log(`💰 Receitas: ${formatCurrency(resumo.total_income)}`);
  console.log(`💸 Despesas: ${formatCurrency(resumo.total_expenses)}`);
  console.log(`📈 Resultado: ${formatCurrency(resumo.net_income)}`);
  console.log(`🔢 Transações: ${resumo.transaction_count}`);
  
  return resumo;
}
```

### 2. Análise por Categoria

```typescript
// Analisando gastos por categoria
async function analisePorCategoria(startDate: string, endDate: string) {
  const resumo = await getFinancialSummary({ start_date: startDate, end_date: endDate });
  
  console.log("📊 Gastos por Categoria:");
  resumo.by_category.expenses.forEach(categoria => {
    console.log(`${categoria.category_name}: ${formatCurrency(categoria.amount)} (${categoria.percentage}%)`);
  });
  
  // Identificar maior gasto
  const maiorGasto = resumo.by_category.expenses[0];
  console.log(`🔺 Maior gasto: ${maiorGasto.category_name} - ${formatCurrency(maiorGasto.amount)}`);
  
  return resumo.by_category;
}
```

### 3. Comparação entre Meses

```typescript
// Comparando dois meses
async function compararMeses(mesAtual: string, mesAnterior: string) {
  const comparacao = await getMonthlyComparison({
    current_month: mesAtual,
    previous_month: mesAnterior
  });
  
  console.log(`📊 Comparação: ${mesAnterior} vs ${mesAtual}`);
  
  const variacaoReceitas = comparacao.income_change_percentage;
  const variacaoDespesas = comparacao.expenses_change_percentage;
  
  console.log(`💰 Receitas: ${variacaoReceitas > 0 ? '↗️' : '↘️'} ${Math.abs(variacaoReceitas)}%`);
  console.log(`💸 Despesas: ${variacaoDespesas > 0 ? '↗️' : '↘️'} ${Math.abs(variacaoDespesas)}%`);
  
  return comparacao;
}
```

### 4. Relatório Completo Mensal

```typescript
// Gerando relatório completo
async function relatorioCompletoMensal(ano: number, mes: number) {
  const startDate = `${ano}-${mes.toString().padStart(2, '0')}-01`;
  const endDate = new Date(ano, mes, 0).toISOString().split('T')[0];
  
  console.log(`📋 RELATÓRIO FINANCEIRO - ${mes}/${ano}`);
  console.log("=" * 50);
  
  // 1. Resumo geral
  const resumo = await resumoMesAtual();
  
  // 2. Análise por categoria
  await analisePorCategoria(startDate, endDate);
  
  // 3. Transações recentes
  const transacoes = await getTransactions({ 
    start_date: startDate, 
    end_date: endDate,
    limit: 10 
  });
  
  console.log("\n💳 Últimas Transações:");
  transacoes.data.forEach(t => {
    const sinal = t.type === 'income' ? '+' : '-';
    console.log(`${formatDate(t.date)} ${sinal}${formatCurrency(t.amount)} - ${t.description}`);
  });
  
  // 4. Saldo das contas
  const contas = await getAccounts();
  console.log("\n🏦 Saldo das Contas:");
  contas.forEach(conta => {
    console.log(`${conta.name}: ${formatCurrency(conta.balance)}`);
  });
  
  const saldoTotal = contas.reduce((sum, conta) => sum + conta.balance, 0);
  console.log(`💰 Total: ${formatCurrency(saldoTotal)}`);
}
```

---

## Importação e Exportação

### 1. Exportando Dados

**Exportar todas as transações:**
```typescript
async function exportarTransacoes() {
  // Buscar todas as transações
  const todasTransacoes = await getTransactions({ limit: 10000 });
  
  // Exportar para CSV
  exportToCSV(
    todasTransacoes.data,
    `transacoes-${new Date().getFullYear()}.csv`,
    ['date', 'description', 'amount', 'type', 'category.name', 'account.name']
  );
  
  console.log("✅ Exportação concluída!");
}
```

**Exportar por período:**
```typescript
async function exportarPorPeriodo(startDate: string, endDate: string) {
  const transacoes = await getTransactions({
    start_date: startDate,
    end_date: endDate,
    limit: 10000
  });
  
  const filename = `transacoes-${startDate}-${endDate}.csv`;
  exportToCSV(transacoes.data, filename);
  
  return filename;
}
```

### 2. Importando de Planilha

**Preparação do arquivo CSV:**
```csv
Data,Descrição,Valor,Tipo,Categoria
2024-01-01,Salário,5000.00,receita,Salário
2024-01-02,Supermercado,-250.50,despesa,Alimentação
2024-01-03,Gasolina,-120.00,despesa,Transporte
```

**Código de importação:**
```typescript
async function importarTransacoes(arquivo: File) {
  const mapeamento = {
    date: 'Data',
    description: 'Descrição', 
    amount: 'Valor',
    type: 'Tipo',
    category: 'Categoria'
  };
  
  try {
    const resultado = await importFromCSV(arquivo, mapeamento);
    
    console.log(`✅ Importação concluída:`);
    console.log(`   Sucessos: ${resultado.successful_imports}`);
    console.log(`   Erros: ${resultado.failed_imports}`);
    console.log(`   Total: ${resultado.total_records}`);
    
    return resultado;
  } catch (error) {
    console.error("❌ Erro na importação:", error);
    throw error;
  }
}
```

---

## Casos de Uso Comuns

### 1. Controle de Orçamento Mensal

```typescript
// Definindo orçamento por categoria
const orcamentoMensal = {
  "Alimentação": 800.00,
  "Transporte": 300.00,
  "Lazer": 200.00,
  "Roupas": 150.00
};

async function verificarOrcamento(mes: string) {
  const startDate = `${mes}-01`;
  const endDate = `${mes}-31`;
  
  const resumo = await getFinancialSummary({ start_date: startDate, end_date: endDate });
  
  console.log("🎯 Controle de Orçamento:");
  
  resumo.by_category.expenses.forEach(categoria => {
    const orcado = orcamentoMensal[categoria.category_name] || 0;
    const gasto = categoria.amount;
    const percentual = (gasto / orcado) * 100;
    
    const status = percentual > 100 ? "🔴 EXCEDEU" : 
                   percentual > 80 ? "🟡 ATENÇÃO" : "🟢 OK";
    
    console.log(`${categoria.category_name}: ${formatCurrency(gasto)}/${formatCurrency(orcado)} (${percentual.toFixed(1)}%) ${status}`);
  });
}
```

### 2. Planejamento de Meta de Economia

```typescript
// Meta: economizar R$ 1000 por mês
const metaEconomia = 1000.00;

async function acompanharMetaEconomia(mes: string) {
  const resumo = await getFinancialSummary({
    start_date: `${mes}-01`,
    end_date: `${mes}-31`
  });
  
  const economia = resumo.net_income;
  const percentualMeta = (economia / metaEconomia) * 100;
  
  console.log("🎯 Meta de Economia:");
  console.log(`Economizado: ${formatCurrency(economia)}`);
  console.log(`Meta: ${formatCurrency(metaEconomia)}`);
  console.log(`Progresso: ${percentualMeta.toFixed(1)}%`);
  
  if (economia >= metaEconomia) {
    console.log("🎉 Meta atingida!");
  } else {
    const faltam = metaEconomia - economia;
    console.log(`💪 Faltam: ${formatCurrency(faltam)}`);
  }
}
```

### 3. Análise de Tendências de Gastos

```typescript
// Analisando tendência dos últimos 6 meses
async function analisarTendencias() {
  const trends = await getCategoryTrends({
    start_date: "2024-01-01",
    end_date: "2024-06-30",
    type: "expense",
    period: "monthly"
  });
  
  console.log("📈 Tendências de Gastos (6 meses):");
  
  trends.forEach(trend => {
    const emoji = trend.trend > 0 ? "📈" : "📉";
    const direcao = trend.trend > 0 ? "aumentaram" : "diminuíram";
    
    console.log(`${emoji} ${trend.category_name}: ${direcao} ${Math.abs(trend.trend).toFixed(1)}%`);
    console.log(`   Média mensal: ${formatCurrency(trend.average_amount)}`);
  });
}
```

### 4. Controle de Cartão de Crédito

```typescript
// Registrando compras no cartão
async function compraCartao(descricao: string, valor: number, parcelas: number = 1) {
  const contaCartao = 3; // ID da conta do cartão
  
  if (parcelas === 1) {
    // Compra à vista
    await createTransaction({
      description: descricao,
      amount: valor,
      type: "expense",
      category_id: getCategoryId("Compras"),
      account_id: contaCartao,
      date: new Date().toISOString().split('T')[0]
    });
  } else {
    // Compra parcelada
    const valorParcela = valor / parcelas;
    const hoje = new Date();
    
    for (let i = 0; i < parcelas; i++) {
      const dataVencimento = new Date(hoje);
      dataVencimento.setMonth(hoje.getMonth() + i);
      
      await createTransaction({
        description: `${descricao} (${i + 1}/${parcelas})`,
        amount: valorParcela,
        type: "expense", 
        category_id: getCategoryId("Compras"),
        account_id: contaCartao,
        date: dataVencimento.toISOString().split('T')[0]
      });
    }
  }
}

// Exemplo de uso
await compraCartao("Smartphone Samsung", 1200.00, 6); // 6x de R$ 200
```

---

## Dicas e Melhores Práticas

### 1. Organização de Categorias

```typescript
// ✅ Boas práticas para categorias
const categoriasOrganizadas = {
  // Seja específico mas não excessivo
  "Alimentação": ["Supermercado", "Restaurante", "Delivery"],
  "Transporte": ["Combustível", "Uber", "Manutenção"],
  "Casa": ["Aluguel", "Contas", "Limpeza"],
  
  // Use cores consistentes
  essenciais: "#F44336", // Vermelho para gastos essenciais
  pessoais: "#9C27B0",   // Roxo para gastos pessoais
  receitas: "#4CAF50"    // Verde para receitas
};
```

### 2. Frequência de Lançamentos

```typescript
// ✅ Registre transações regularmente
async function lembreteDiario() {
  console.log("📝 Lembrete: Registrar transações do dia");
  
  // Verificar transações não registradas
  const hoje = new Date().toISOString().split('T')[0];
  const transacoesHoje = await getTransactions({
    start_date: hoje,
    end_date: hoje
  });
  
  if (transacoesHoje.data.length === 0) {
    console.log("⚠️ Nenhuma transação registrada hoje");
  }
}
```

### 3. Backup Regular

```typescript
// ✅ Fazer backup mensal
async function backupMensal() {
  const mesAtual = new Date().toISOString().slice(0, 7); // YYYY-MM
  
  // Exportar transações
  await exportarPorPeriodo(`${mesAtual}-01`, `${mesAtual}-31`);
  
  // Exportar configurações
  const contas = await getAccounts();
  const categorias = await getCategories();
  
  exportToCSV(contas, `backup-contas-${mesAtual}.csv`);
  exportToCSV(categorias, `backup-categorias-${mesAtual}.csv`);
  
  console.log("💾 Backup mensal realizado");
}
```

### 4. Validação de Dados

```typescript
// ✅ Sempre validar dados importantes
function validarTransacao(data: any) {
  const validation = validateTransactionData(data);
  
  if (!validation.isValid) {
    console.error("❌ Dados inválidos:");
    Object.entries(validation.errors).forEach(([campo, erros]) => {
      console.error(`  ${campo}: ${erros.join(", ")}`);
    });
    return false;
  }
  
  return true;
}
```

---

## Solução de Problemas

### 1. Problemas Comuns de Autenticação

```typescript
// Verificar se o token está válido
async function verificarAutenticacao() {
  try {
    const user = await getCurrentUser();
    console.log("✅ Usuário autenticado:", user.name);
    return true;
  } catch (error) {
    console.log("❌ Erro de autenticação:", error.message);
    
    // Tentar renovar o token
    try {
      const novoToken = await refreshToken();
      console.log("✅ Token renovado com sucesso");
      return true;
    } catch (refreshError) {
      console.log("❌ Erro ao renovar token, necessário novo login");
      return false;
    }
  }
}
```

### 2. Problemas de Sincronização

```typescript
// Resolver inconsistências de saldo
async function verificarConsistenciaSaldos() {
  const contas = await getAccounts();
  
  for (const conta of contas) {
    // Calcular saldo baseado nas transações
    const transacoes = await getTransactions({ 
      account_id: conta.id,
      limit: 10000 
    });
    
    const saldoCalculado = transacoes.data.reduce((sum, t) => {
      return sum + (t.type === 'income' ? t.amount : -t.amount);
    }, conta.initial_balance || 0);
    
    const diferenca = Math.abs(saldoCalculado - conta.balance);
    
    if (diferenca > 0.01) { // Diferença maior que 1 centavo
      console.log(`⚠️ Inconsistência na conta ${conta.name}:`);
      console.log(`   Saldo registrado: ${formatCurrency(conta.balance)}`);
      console.log(`   Saldo calculado: ${formatCurrency(saldoCalculado)}`);
      console.log(`   Diferença: ${formatCurrency(diferenca)}`);
    }
  }
}
```

### 3. Recuperação de Dados

```typescript
// Recuperar transações excluídas por engano
async function recuperarTransacao(id: number) {
  try {
    const transacao = await getTransactionById(id);
    console.log("✅ Transação encontrada:", transacao);
    return transacao;
  } catch (error) {
    console.log("❌ Transação não encontrada no banco");
    
    // Verificar se existe em backup
    console.log("🔍 Verificando backups...");
    // Implementar lógica de recuperação de backup
  }
}
```

### 4. Performance e Otimização

```typescript
// Otimizar consultas grandes
async function consultaOtimizada(startDate: string, endDate: string) {
  // Usar cache quando possível
  const cacheKey = `summary:${startDate}:${endDate}`;
  let resumo = await cacheGet(cacheKey);
  
  if (!resumo) {
    resumo = await getFinancialSummary({ start_date: startDate, end_date: endDate });
    await cacheSet(cacheKey, resumo, 300); // Cache por 5 minutos
  }
  
  return resumo;
}
```

---

## Recursos Avançados

### 1. Automação com Scripts

```typescript
// Script para processar extratos bancários automaticamente
async function processarExtratoAutomatico(arquivo: string) {
  // 1. Ler arquivo de extrato
  const linhas = await lerArquivoExtrato(arquivo);
  
  // 2. Processar cada linha
  for (const linha of linhas) {
    const transacao = parsearLinhaExtrato(linha);
    
    // 3. Categorizar automaticamente
    const categoria = await categorizarAutomatico(transacao.description);
    
    // 4. Criar transação
    await createTransaction({
      ...transacao,
      category_id: categoria.id
    });
  }
  
  console.log(`✅ Processadas ${linhas.length} transações`);
}
```

### 2. Integração com APIs Bancárias

```typescript
// Sincronizar com Open Banking
async function sincronizarContaBancaria(accountId: string) {
  try {
    const transacoesBanco = await buscarTransacoesBanco(accountId);
    
    for (const transacao of transacoesBanco) {
      // Verificar se já existe
      const existe = await verificarTransacaoExiste(transacao.id);
      
      if (!existe) {
        await createTransaction({
          description: transacao.description,
          amount: transacao.amount,
          type: transacao.type,
          category_id: await inferirCategoria(transacao.description),
          account_id: 1,
          date: transacao.date,
          external_id: transacao.id
        });
      }
    }
    
    console.log("✅ Sincronização bancária concluída");
  } catch (error) {
    console.error("❌ Erro na sincronização:", error);
  }
}
```

---

## Conclusão

Este guia fornece uma base sólida para usar o sistema de controle financeiro de forma eficiente. Lembre-se:

1. **Seja consistente**: Registre transações regularmente
2. **Organize bem**: Use categorias claras e contas separadas
3. **Analise regularmente**: Gere relatórios mensais
4. **Faça backup**: Exporte dados periodicamente
5. **Monitore tendências**: Acompanhe seus padrões de gastos

Para mais informações, consulte:
- [Documentação da API](./API.md)
- [Documentação de Componentes](./COMPONENTS.md)
- [Documentação de Funções](./FUNCTIONS.md)

**Suporte:** Para dúvidas, abra uma issue no repositório ou entre em contato através dos canais oficiais.