// SYSFIN v1.0 - Sistema Financeiro
// Main JavaScript Application

class SysfinApp {
    constructor() {
        this.transactions = this.loadData('transactions') || [];
        this.categories = this.loadData('categories') || this.getDefaultCategories();
        this.currentTab = 'dashboard';
        this.editingTransaction = null;
        
        this.init();
    }

    init() {
        this.showSplashScreen();
        this.setupEventListeners();
        this.updateDashboard();
    }

    // Splash Screen Animation (matching Python version)
    showSplashScreen() {
        const splashScreen = document.getElementById('splash-screen');
        const mainApp = document.getElementById('main-app');
        const loadingFill = document.getElementById('loading-fill');
        const loadingText = document.getElementById('loading-text');
        const loadingPercentage = document.getElementById('loading-percentage');

        const loadingSteps = [
            { text: 'Carregando módulos...', percentage: 10 },
            { text: 'Inicializando banco de dados...', percentage: 25 },
            { text: 'Configurando interface...', percentage: 40 },
            { text: 'Carregando configurações...', percentage: 60 },
            { text: 'Preparando sistema...', percentage: 80 },
            { text: 'Finalizando...', percentage: 95 },
            { text: 'Sistema pronto!', percentage: 100 }
        ];

        let currentStep = 0;

        const updateLoading = () => {
            if (currentStep < loadingSteps.length) {
                const step = loadingSteps[currentStep];
                loadingFill.style.width = step.percentage + '%';
                loadingText.textContent = step.text;
                loadingPercentage.textContent = step.percentage + '%';
                currentStep++;
                
                setTimeout(updateLoading, 800); // Match Python timing
            } else {
                // Splash screen complete, show main app
                setTimeout(() => {
                    splashScreen.style.opacity = '0';
                    splashScreen.style.transform = 'scale(1.1)';
                    
                    setTimeout(() => {
                        splashScreen.classList.add('hidden');
                        mainApp.classList.remove('hidden');
                        setTimeout(() => {
                            mainApp.style.opacity = '1';
                        }, 100);
                    }, 500);
                }, 1000);
            }
        };

        // Allow ESC key and click to skip splash screen
        const skipSplash = () => {
            splashScreen.style.transition = 'opacity 0.3s ease';
            splashScreen.style.opacity = '0';
            setTimeout(() => {
                splashScreen.classList.add('hidden');
                mainApp.classList.remove('hidden');
                mainApp.style.opacity = '1';
            }, 300);
        };

        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape' && !splashScreen.classList.contains('hidden')) {
                skipSplash();
            }
        });

        splashScreen.addEventListener('click', skipSplash);

        // Start loading animation
        setTimeout(updateLoading, 500);
    }

    setupEventListeners() {
        // Navigation
        document.querySelectorAll('.nav-btn').forEach(btn => {
            btn.addEventListener('click', (e) => {
                const tab = e.currentTarget.dataset.tab;
                this.switchTab(tab);
            });
        });

        // Transaction modal
        document.getElementById('add-transaction-btn').addEventListener('click', () => {
            this.openTransactionModal();
        });

        document.getElementById('quick-add-transaction').addEventListener('click', () => {
            this.openTransactionModal();
        });

        // Modal controls
        document.querySelector('.modal-close').addEventListener('click', () => {
            this.closeTransactionModal();
        });

        document.querySelector('.modal-cancel').addEventListener('click', () => {
            this.closeTransactionModal();
        });

        document.getElementById('transaction-modal').addEventListener('click', (e) => {
            if (e.target.id === 'transaction-modal') {
                this.closeTransactionModal();
            }
        });

        // Form submission
        document.getElementById('transaction-form').addEventListener('submit', (e) => {
            e.preventDefault();
            this.saveTransaction();
        });

        // Settings
        document.getElementById('add-category-btn').addEventListener('click', () => {
            this.addCategory();
        });

        document.getElementById('export-data-btn').addEventListener('click', () => {
            this.exportData();
        });

        document.getElementById('clear-data-btn').addEventListener('click', () => {
            this.clearAllData();
        });

        // Transaction type change
        document.getElementById('transaction-type').addEventListener('change', () => {
            this.updateCategoryOptions();
        });

        // Search and filters
        document.querySelector('.search-input').addEventListener('input', (e) => {
            this.filterTransactions(e.target.value);
        });

        document.querySelector('.filter-select').addEventListener('change', (e) => {
            this.filterTransactionsByType(e.target.value);
        });

        document.querySelector('.date-filter').addEventListener('change', (e) => {
            this.filterTransactionsByDate(e.target.value);
        });
    }

    switchTab(tabName) {
        // Update navigation
        document.querySelectorAll('.nav-btn').forEach(btn => {
            btn.classList.remove('active');
        });
        document.querySelector(`[data-tab="${tabName}"]`).classList.add('active');

        // Update content
        document.querySelectorAll('.tab-content').forEach(content => {
            content.classList.remove('active');
        });
        document.getElementById(tabName).classList.add('active');

        this.currentTab = tabName;

        // Load tab-specific content
        switch (tabName) {
            case 'dashboard':
                this.updateDashboard();
                break;
            case 'transactions':
                this.updateTransactionsTable();
                break;
            case 'reports':
                this.updateReports();
                break;
            case 'settings':
                this.updateSettings();
                break;
        }
    }

    updateDashboard() {
        const currentMonth = new Date().getMonth();
        const currentYear = new Date().getFullYear();
        
        const monthlyTransactions = this.transactions.filter(t => {
            const date = new Date(t.date);
            return date.getMonth() === currentMonth && date.getFullYear() === currentYear;
        });

        const totalIncome = monthlyTransactions
            .filter(t => t.type === 'income')
            .reduce((sum, t) => sum + parseFloat(t.amount), 0);

        const totalExpenses = monthlyTransactions
            .filter(t => t.type === 'expense')
            .reduce((sum, t) => sum + parseFloat(t.amount), 0);

        const balance = totalIncome - totalExpenses;

        // Update dashboard cards
        document.getElementById('total-balance').textContent = this.formatCurrency(balance);
        document.getElementById('total-income').textContent = this.formatCurrency(totalIncome);
        document.getElementById('total-expenses').textContent = this.formatCurrency(totalExpenses);

        // Update balance change indicator
        const balanceChange = document.querySelector('.balance-change');
        const prevMonthBalance = this.getPreviousMonthBalance();
        const changePercent = prevMonthBalance > 0 ? ((balance - prevMonthBalance) / prevMonthBalance * 100) : 0;
        
        balanceChange.className = 'balance-change ' + (changePercent >= 0 ? 'positive' : 'negative');
        balanceChange.querySelector('span').textContent = 
            `${changePercent >= 0 ? '+' : ''}${changePercent.toFixed(1)}% este mês`;

        // Update recent transactions
        this.updateRecentTransactions();

        // Update financial chart
        this.updateFinancialChart();
    }

    updateRecentTransactions() {
        const recentList = document.getElementById('recent-transactions-list');
        const recent = this.transactions
            .sort((a, b) => new Date(b.date) - new Date(a.date))
            .slice(0, 5);

        if (recent.length === 0) {
            recentList.innerHTML = '<p style="color: #888; text-align: center; padding: 2rem;">Nenhuma transação encontrada</p>';
            return;
        }

        recentList.innerHTML = recent.map(transaction => `
            <div class="transaction-item">
                <div class="transaction-info">
                    <h4>${transaction.description}</h4>
                    <p>${this.getCategoryName(transaction.category)} • ${this.formatDate(transaction.date)}</p>
                </div>
                <div class="transaction-amount ${transaction.type}">
                    ${transaction.type === 'income' ? '+' : '-'}${this.formatCurrency(transaction.amount)}
                </div>
            </div>
        `).join('');
    }

    updateTransactionsTable() {
        const tbody = document.getElementById('transactions-tbody');
        
        if (this.transactions.length === 0) {
            tbody.innerHTML = '<tr><td colspan="5" style="text-align: center; color: #888; padding: 2rem;">Nenhuma transação encontrada</td></tr>';
            return;
        }

        const sortedTransactions = this.transactions.sort((a, b) => new Date(b.date) - new Date(a.date));

        tbody.innerHTML = sortedTransactions.map(transaction => `
            <tr>
                <td>${this.formatDate(transaction.date)}</td>
                <td>${transaction.description}</td>
                <td>${this.getCategoryName(transaction.category)}</td>
                <td class="${transaction.type}">
                    ${transaction.type === 'income' ? '+' : '-'}${this.formatCurrency(transaction.amount)}
                </td>
                <td>
                    <button class="secondary-btn btn-small" onclick="app.editTransaction('${transaction.id}')">
                        <i class="fas fa-edit"></i>
                    </button>
                    <button class="danger-btn btn-small" onclick="app.deleteTransaction('${transaction.id}')">
                        <i class="fas fa-trash"></i>
                    </button>
                </td>
            </tr>
        `).join('');
    }

    updateReports() {
        this.updateCategoryChart();
        this.updateMonthlyChart();
    }

    updateSettings() {
        const categoriesList = document.getElementById('categories-list');
        
        categoriesList.innerHTML = this.categories.map(category => `
            <div class="category-item">
                <span class="category-name">${category.name}</span>
                <div class="category-actions">
                    <button class="secondary-btn btn-small" onclick="app.editCategory('${category.id}')">
                        <i class="fas fa-edit"></i>
                    </button>
                    ${!category.isDefault ? `
                        <button class="danger-btn btn-small" onclick="app.deleteCategory('${category.id}')">
                            <i class="fas fa-trash"></i>
                        </button>
                    ` : ''}
                </div>
            </div>
        `).join('');
    }

    openTransactionModal(transactionId = null) {
        const modal = document.getElementById('transaction-modal');
        const form = document.getElementById('transaction-form');
        const title = document.getElementById('modal-title');

        if (transactionId) {
            // Edit mode
            const transaction = this.transactions.find(t => t.id === transactionId);
            title.textContent = 'Editar Transação';
            
            document.getElementById('transaction-type').value = transaction.type;
            document.getElementById('transaction-description').value = transaction.description;
            document.getElementById('transaction-category').value = transaction.category;
            document.getElementById('transaction-amount').value = transaction.amount;
            document.getElementById('transaction-date').value = transaction.date;
            
            this.editingTransaction = transactionId;
        } else {
            // Add mode
            title.textContent = 'Nova Transação';
            form.reset();
            document.getElementById('transaction-date').value = new Date().toISOString().split('T')[0];
            this.editingTransaction = null;
        }

        this.updateCategoryOptions();
        modal.classList.add('show');
    }

    closeTransactionModal() {
        const modal = document.getElementById('transaction-modal');
        modal.classList.remove('show');
        this.editingTransaction = null;
    }

    saveTransaction() {
        const form = document.getElementById('transaction-form');
        const formData = new FormData(form);
        
        const transaction = {
            id: this.editingTransaction || this.generateId(),
            type: document.getElementById('transaction-type').value,
            description: document.getElementById('transaction-description').value,
            category: document.getElementById('transaction-category').value,
            amount: parseFloat(document.getElementById('transaction-amount').value),
            date: document.getElementById('transaction-date').value
        };

        if (this.editingTransaction) {
            // Update existing transaction
            const index = this.transactions.findIndex(t => t.id === this.editingTransaction);
            this.transactions[index] = transaction;
        } else {
            // Add new transaction
            this.transactions.push(transaction);
        }

        this.saveData('transactions', this.transactions);
        this.closeTransactionModal();
        this.updateDashboard();
        this.updateTransactionsTable();
        
        // Show success message
        this.showNotification('Transação salva com sucesso!', 'success');
    }

    editTransaction(id) {
        this.openTransactionModal(id);
    }

    deleteTransaction(id) {
        if (confirm('Tem certeza que deseja excluir esta transação?')) {
            this.transactions = this.transactions.filter(t => t.id !== id);
            this.saveData('transactions', this.transactions);
            this.updateDashboard();
            this.updateTransactionsTable();
            this.showNotification('Transação excluída com sucesso!', 'success');
        }
    }

    updateCategoryOptions() {
        const select = document.getElementById('transaction-category');
        const type = document.getElementById('transaction-type').value;
        
        const filteredCategories = this.categories.filter(cat => 
            cat.type === type || cat.type === 'both'
        );

        select.innerHTML = filteredCategories.map(category => 
            `<option value="${category.id}">${category.name}</option>`
        ).join('');
    }

    addCategory() {
        const name = prompt('Nome da nova categoria:');
        if (name && name.trim()) {
            const category = {
                id: this.generateId(),
                name: name.trim(),
                type: 'both',
                isDefault: false
            };
            this.categories.push(category);
            this.saveData('categories', this.categories);
            this.updateSettings();
            this.showNotification('Categoria adicionada com sucesso!', 'success');
        }
    }

    editCategory(id) {
        const category = this.categories.find(c => c.id === id);
        const newName = prompt('Novo nome da categoria:', category.name);
        if (newName && newName.trim()) {
            category.name = newName.trim();
            this.saveData('categories', this.categories);
            this.updateSettings();
            this.showNotification('Categoria atualizada com sucesso!', 'success');
        }
    }

    deleteCategory(id) {
        if (confirm('Tem certeza que deseja excluir esta categoria?')) {
            this.categories = this.categories.filter(c => c.id !== id);
            this.saveData('categories', this.categories);
            this.updateSettings();
            this.showNotification('Categoria excluída com sucesso!', 'success');
        }
    }

    exportData() {
        const data = {
            transactions: this.transactions,
            categories: this.categories,
            exportDate: new Date().toISOString()
        };

        const blob = new Blob([JSON.stringify(data, null, 2)], { type: 'application/json' });
        const url = URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = `sysfin-backup-${new Date().toISOString().split('T')[0]}.json`;
        a.click();
        URL.revokeObjectURL(url);
        
        this.showNotification('Dados exportados com sucesso!', 'success');
    }

    clearAllData() {
        if (confirm('Tem certeza que deseja limpar todos os dados? Esta ação não pode ser desfeita.')) {
            if (confirm('Esta ação irá apagar TODAS as transações e categorias personalizadas. Confirma?')) {
                localStorage.clear();
                this.transactions = [];
                this.categories = this.getDefaultCategories();
                this.updateDashboard();
                this.updateTransactionsTable();
                this.updateSettings();
                this.showNotification('Todos os dados foram limpos!', 'warning');
            }
        }
    }

    // Chart Methods
    updateFinancialChart() {
        const canvas = document.getElementById('financial-chart');
        const ctx = canvas.getContext('2d');
        
        // Simple chart implementation
        this.drawFinancialChart(ctx, canvas.width, canvas.height);
    }

    drawFinancialChart(ctx, width, height) {
        ctx.clearRect(0, 0, width, height);
        
        // Get last 6 months data
        const monthsData = this.getLast6MonthsData();
        const maxValue = Math.max(...monthsData.map(m => Math.max(m.income, m.expenses)));
        
        // Chart properties
        const margin = 40;
        const chartWidth = width - margin * 2;
        const chartHeight = height - margin * 2;
        const barWidth = chartWidth / monthsData.length / 2 - 10;
        
        // Draw bars
        monthsData.forEach((month, index) => {
            const x = margin + index * (chartWidth / monthsData.length);
            
            // Income bar
            const incomeHeight = (month.income / maxValue) * chartHeight;
            ctx.fillStyle = '#00ff00';
            ctx.fillRect(x, margin + chartHeight - incomeHeight, barWidth, incomeHeight);
            
            // Expense bar
            const expenseHeight = (month.expenses / maxValue) * chartHeight;
            ctx.fillStyle = '#ff4444';
            ctx.fillRect(x + barWidth + 5, margin + chartHeight - expenseHeight, barWidth, expenseHeight);
            
            // Month label
            ctx.fillStyle = '#00ffff';
            ctx.font = '10px Rajdhani';
            ctx.textAlign = 'center';
            ctx.fillText(month.name, x + barWidth, height - 10);
        });
        
        // Legend
        ctx.fillStyle = '#00ff00';
        ctx.fillRect(width - 100, 10, 15, 15);
        ctx.fillStyle = '#00ffff';
        ctx.font = '12px Rajdhani';
        ctx.fillText('Receitas', width - 80, 22);
        
        ctx.fillStyle = '#ff4444';
        ctx.fillRect(width - 100, 30, 15, 15);
        ctx.fillStyle = '#00ffff';
        ctx.fillText('Despesas', width - 80, 42);
    }

    updateCategoryChart() {
        const canvas = document.getElementById('category-chart');
        const ctx = canvas.getContext('2d');
        
        // Get category data
        const categoryData = this.getCategoryData();
        this.drawPieChart(ctx, canvas.width, canvas.height, categoryData);
    }

    drawPieChart(ctx, width, height, data) {
        ctx.clearRect(0, 0, width, height);
        
        const centerX = width / 2;
        const centerY = height / 2;
        const radius = Math.min(width, height) / 3;
        
        let total = data.reduce((sum, item) => sum + item.value, 0);
        let currentAngle = 0;
        
        const colors = ['#00ffff', '#ff00ff', '#00ff00', '#ffff00', '#ff4444', '#8800ff'];
        
        data.forEach((item, index) => {
            const sliceAngle = (item.value / total) * 2 * Math.PI;
            
            ctx.beginPath();
            ctx.moveTo(centerX, centerY);
            ctx.arc(centerX, centerY, radius, currentAngle, currentAngle + sliceAngle);
            ctx.closePath();
            
            ctx.fillStyle = colors[index % colors.length];
            ctx.fill();
            
            // Label
            const labelAngle = currentAngle + sliceAngle / 2;
            const labelX = centerX + Math.cos(labelAngle) * (radius + 20);
            const labelY = centerY + Math.sin(labelAngle) * (radius + 20);
            
            ctx.fillStyle = '#00ffff';
            ctx.font = '10px Rajdhani';
            ctx.textAlign = 'center';
            ctx.fillText(item.name, labelX, labelY);
            
            currentAngle += sliceAngle;
        });
    }

    updateMonthlyChart() {
        const canvas = document.getElementById('monthly-chart');
        const ctx = canvas.getContext('2d');
        
        const monthlyData = this.getMonthlyEvolutionData();
        this.drawLineChart(ctx, canvas.width, canvas.height, monthlyData);
    }

    drawLineChart(ctx, width, height, data) {
        ctx.clearRect(0, 0, width, height);
        
        const margin = 40;
        const chartWidth = width - margin * 2;
        const chartHeight = height - margin * 2;
        
        const maxValue = Math.max(...data.map(d => d.balance));
        const minValue = Math.min(...data.map(d => d.balance));
        const range = maxValue - minValue || 1;
        
        // Draw line
        ctx.beginPath();
        data.forEach((point, index) => {
            const x = margin + (index / (data.length - 1)) * chartWidth;
            const y = margin + chartHeight - ((point.balance - minValue) / range) * chartHeight;
            
            if (index === 0) {
                ctx.moveTo(x, y);
            } else {
                ctx.lineTo(x, y);
            }
        });
        
        ctx.strokeStyle = '#00ffff';
        ctx.lineWidth = 2;
        ctx.stroke();
        
        // Draw points
        data.forEach((point, index) => {
            const x = margin + (index / (data.length - 1)) * chartWidth;
            const y = margin + chartHeight - ((point.balance - minValue) / range) * chartHeight;
            
            ctx.beginPath();
            ctx.arc(x, y, 4, 0, 2 * Math.PI);
            ctx.fillStyle = '#ff00ff';
            ctx.fill();
            
            // Month label
            ctx.fillStyle = '#00ffff';
            ctx.font = '10px Rajdhani';
            ctx.textAlign = 'center';
            ctx.fillText(point.name, x, height - 10);
        });
    }

    // Filter Methods
    filterTransactions(searchTerm) {
        // Implementation for transaction filtering
        console.log('Filtering transactions:', searchTerm);
    }

    filterTransactionsByType(type) {
        // Implementation for type filtering
        console.log('Filtering by type:', type);
    }

    filterTransactionsByDate(date) {
        // Implementation for date filtering
        console.log('Filtering by date:', date);
    }

    // Utility Methods
    formatCurrency(amount) {
        return new Intl.NumberFormat('pt-BR', {
            style: 'currency',
            currency: 'BRL'
        }).format(amount);
    }

    formatDate(dateString) {
        return new Date(dateString).toLocaleDateString('pt-BR');
    }

    generateId() {
        return Date.now().toString(36) + Math.random().toString(36).substr(2);
    }

    getCategoryName(categoryId) {
        const category = this.categories.find(c => c.id === categoryId);
        return category ? category.name : 'Categoria não encontrada';
    }

    getPreviousMonthBalance() {
        const prevMonth = new Date();
        prevMonth.setMonth(prevMonth.getMonth() - 1);
        
        const prevMonthTransactions = this.transactions.filter(t => {
            const date = new Date(t.date);
            return date.getMonth() === prevMonth.getMonth() && 
                   date.getFullYear() === prevMonth.getFullYear();
        });

        const income = prevMonthTransactions
            .filter(t => t.type === 'income')
            .reduce((sum, t) => sum + parseFloat(t.amount), 0);

        const expenses = prevMonthTransactions
            .filter(t => t.type === 'expense')
            .reduce((sum, t) => sum + parseFloat(t.amount), 0);

        return income - expenses;
    }

    getLast6MonthsData() {
        const months = [];
        const monthNames = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 
                           'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'];
        
        for (let i = 5; i >= 0; i--) {
            const date = new Date();
            date.setMonth(date.getMonth() - i);
            
            const monthTransactions = this.transactions.filter(t => {
                const tDate = new Date(t.date);
                return tDate.getMonth() === date.getMonth() && 
                       tDate.getFullYear() === date.getFullYear();
            });

            const income = monthTransactions
                .filter(t => t.type === 'income')
                .reduce((sum, t) => sum + parseFloat(t.amount), 0);

            const expenses = monthTransactions
                .filter(t => t.type === 'expense')
                .reduce((sum, t) => sum + parseFloat(t.amount), 0);

            months.push({
                name: monthNames[date.getMonth()],
                income,
                expenses
            });
        }
        
        return months;
    }

    getCategoryData() {
        const categoryTotals = {};
        
        this.transactions.forEach(transaction => {
            const categoryName = this.getCategoryName(transaction.category);
            if (transaction.type === 'expense') {
                categoryTotals[categoryName] = (categoryTotals[categoryName] || 0) + parseFloat(transaction.amount);
            }
        });

        return Object.entries(categoryTotals)
            .map(([name, value]) => ({ name, value }))
            .sort((a, b) => b.value - a.value)
            .slice(0, 6);
    }

    getMonthlyEvolutionData() {
        const months = [];
        const monthNames = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 
                           'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'];
        
        let runningBalance = 0;
        
        for (let i = 11; i >= 0; i--) {
            const date = new Date();
            date.setMonth(date.getMonth() - i);
            
            const monthTransactions = this.transactions.filter(t => {
                const tDate = new Date(t.date);
                return tDate.getMonth() === date.getMonth() && 
                       tDate.getFullYear() === date.getFullYear();
            });

            const income = monthTransactions
                .filter(t => t.type === 'income')
                .reduce((sum, t) => sum + parseFloat(t.amount), 0);

            const expenses = monthTransactions
                .filter(t => t.type === 'expense')
                .reduce((sum, t) => sum + parseFloat(t.amount), 0);

            runningBalance += income - expenses;

            months.push({
                name: monthNames[date.getMonth()],
                balance: runningBalance
            });
        }
        
        return months;
    }

    getDefaultCategories() {
        return [
            { id: 'cat1', name: 'Salário', type: 'income', isDefault: true },
            { id: 'cat2', name: 'Freelance', type: 'income', isDefault: true },
            { id: 'cat3', name: 'Investimentos', type: 'income', isDefault: true },
            { id: 'cat4', name: 'Alimentação', type: 'expense', isDefault: true },
            { id: 'cat5', name: 'Transporte', type: 'expense', isDefault: true },
            { id: 'cat6', name: 'Moradia', type: 'expense', isDefault: true },
            { id: 'cat7', name: 'Saúde', type: 'expense', isDefault: true },
            { id: 'cat8', name: 'Educação', type: 'expense', isDefault: true },
            { id: 'cat9', name: 'Lazer', type: 'expense', isDefault: true },
            { id: 'cat10', name: 'Outros', type: 'both', isDefault: true }
        ];
    }

    showNotification(message, type = 'info') {
        // Create notification element
        const notification = document.createElement('div');
        notification.className = `notification ${type}`;
        notification.style.cssText = `
            position: fixed;
            top: 20px;
            right: 20px;
            padding: 1rem 2rem;
            background: rgba(26, 10, 46, 0.95);
            border: 2px solid ${type === 'success' ? '#00ff00' : type === 'warning' ? '#ffff00' : '#00ffff'};
            border-radius: 8px;
            color: ${type === 'success' ? '#00ff00' : type === 'warning' ? '#ffff00' : '#00ffff'};
            z-index: 10001;
            animation: slideInRight 0.3s ease;
            box-shadow: 0 0 20px rgba(0, 255, 255, 0.3);
        `;
        notification.textContent = message;

        document.body.appendChild(notification);

        // Auto remove after 3 seconds
        setTimeout(() => {
            notification.style.animation = 'slideOutRight 0.3s ease';
            setTimeout(() => {
                if (notification.parentNode) {
                    notification.parentNode.removeChild(notification);
                }
            }, 300);
        }, 3000);
    }

    // Data persistence
    saveData(key, data) {
        localStorage.setItem(`sysfin_${key}`, JSON.stringify(data));
    }

    loadData(key) {
        const data = localStorage.getItem(`sysfin_${key}`);
        return data ? JSON.parse(data) : null;
    }
}

// Initialize app when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    window.app = new SysfinApp();
});

// Add CSS for notifications animation
const style = document.createElement('style');
style.textContent = `
    @keyframes slideInRight {
        from {
            opacity: 0;
            transform: translateX(100%);
        }
        to {
            opacity: 1;
            transform: translateX(0);
        }
    }
    
    @keyframes slideOutRight {
        from {
            opacity: 1;
            transform: translateX(0);
        }
        to {
            opacity: 0;
            transform: translateX(100%);
        }
    }
`;
document.head.appendChild(style);