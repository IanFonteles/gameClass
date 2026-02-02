# 🤖 Guia: Mensagens de Commit com Copilot e GitHub Actions

## 📝 Parte 1: Mensagens de Commit com Copilot

### 🎯 Por que Boas Mensagens de Commit?

Mensagens claras ajudam a:
- 📚 Documentar histórico do projeto
- 🔍 Facilitar busca de mudanças
- 🤝 Colaborar efetivamente
- 🐛 Debugar problemas
- 📊 Gerar changelogs automáticos

---

## ✍️ Como Usar Copilot para Commits

### Método 1: Source Control do VS Code

#### Passo 1: Staging das Mudanças
```
1. Abra Source Control (Ctrl+Shift+G)
2. Clique no "+" ao lado dos arquivos modificados
3. Clique no ícone ✨ "Generate Commit Message" acima da caixa de mensagem
```

#### Passo 2: Copilot Gera Mensagem
O Copilot analisa:
- Arquivos modificados (diff)
- Tipo de mudanças (features, fixes, docs)
- Escopo das alterações
- Convenções do projeto

#### Exemplo Gerado:
```
feat(gameplay): adiciona sistema de partículas ao acertar toupeira

- Implementa explosão radial de 12 partículas neon
- Cores alternadas: cyan, magenta, lime
- Otimização GPU com will-change
```

---

### Método 2: Terminal com Git

#### Commit Vazio para Trigger
```bash
git commit --allow-empty
```

**No editor que abrir**, digite `#` e pressione `Ctrl+Space` para ativar Copilot.

#### Exemplo:
```bash
# Adicionar sistema de som
# Copilot sugere:

feat(audio): implementa sistema de som completo com música cyberpunk

- Adiciona música de fundo em loop
- Efeitos sonoros ao acertar/errar
- Controles de volume e mute
- Sons temáticos cyberpunk neon

Closes #1
```

---

### Método 3: Extensão Copilot Chat

#### Comando no Chat:
```
@workspace crie uma mensagem de commit para as mudanças staged seguindo Conventional Commits
```

#### Copilot Analisa e Gera:
```
feat(ui): adiciona modal de game over com tema cyberpunk

- Implementa modal responsiva com animação slideUp
- Background dark gradient (#0a0e27 → #1a1a2e)
- Border cyan (#00ffff) com glow neon
- Título "⚡ MISSÃO FINALIZADA ⚡"
- Exibe pontuação final com destaque magenta
- Botão de reiniciar com gradient neon

Visual: Mantém coerência com tema cyberpunk
Performance: Animação GPU-accelerated
```

---

## 📐 Formato: Conventional Commits

### Estrutura Básica
```
<tipo>(<escopo>): <descrição curta>

<corpo detalhado opcional>

<footer opcional>
```

### Tipos Principais
```
feat:     Nova funcionalidade
fix:      Correção de bug
docs:     Documentação
style:    Formatação (sem mudança de lógica)
refactor: Refatoração de código
perf:     Melhoria de performance
test:     Adição de testes
chore:    Tarefas de manutenção
```

### Exemplos para Cyber Mole

#### Feature
```bash
git commit -m "feat(gameplay): adiciona toupeiras especiais com comportamentos únicos

- Toupeira Turbo: 2x mais rápida, 3 pontos
- Toupeira Bônus: 2x mais lenta, 5 pontos  
- Toupeira Fantasma: semi-transparente, 4 pontos
- Toupeira Bomba: penalidade de -5 pontos

Cada tipo tem visual distinto com cores neon
Probabilidades balanceadas para gameplay justo

Closes #4"
```

#### Bug Fix
```bash
git commit -m "fix(gameplay): corrige toupeiras duplicadas na mesma toca

- Adiciona verificação de toca ocupada antes de spawn
- Implementa classe 'occupied' para controle de estado
- Previne race condition em múltiplos spawns simultâneos

Reprodução: ocorria em dificuldade INSANO com múltiplos cliques rápidos
Solução: filtro de tocas disponíveis antes de seleção aleatória

Fixes #8"
```

#### Performance
```bash
git commit -m "perf(rendering): otimiza animações para 60fps constante

- Substitui manipulação de width/height por transform
- Adiciona will-change em elementos animados
- Usa requestIdleCallback para scheduling
- Cache de elementos DOM em holesCache
- Bitwise operator (| 0) para random mais rápido

Antes: ~45fps em INSANO, ~50ms por frame
Depois: 60fps estável, ~16ms por frame
Ganho: ~35% performance, sem drops em mobile"
```

#### Refactor
```bash
git commit -m "refactor(architecture): modulariza JavaScript em arquivos separados

- Extrai game.js: lógica principal do jogo
- Extrai ui.js: manipulação de interface
- Extrai audio.js: sistema de som
- Extrai particles.js: efeitos visuais
- Cria main.js como entry point

Estrutura:
/static/js/
├── main.js (300 lines → 50 lines)
├── game.js (150 lines)
├── ui.js (100 lines)
├── audio.js (80 lines)
└── particles.js (70 lines)

Benefícios: 
- Melhor manutenibilidade
- Testes mais fáceis
- Imports explícitos
- Separação de responsabilidades"
```

---

## 🚀 Parte 2: GitHub Actions - CI/CD

### 📦 O que Foram Criados

Criei 2 workflows completos para o Cyber Mole:

#### 1. **CI Pipeline** (`.github/workflows/ci.yml`)
- 🔍 Lint e qualidade de código
- 🧪 Testes automatizados (Python 3.8-3.11)
- 🔒 Security scan (Safety, Bandit)
- 🏗️ Build e validação
- 🚦 Lighthouse performance
- 📢 Notificações

#### 2. **CD Pipeline** (`.github/workflows/cd.yml`)
- 🚀 Deploy automático Staging (Heroku)
- 🌟 Deploy Production (Azure)
- 📄 Deploy documentação (GitHub Pages)
- 🐳 Build e push Docker image
- 📦 Criar GitHub Release
- 📢 Notificações de deploy

---

## 🎯 Como Funciona o CI

### Trigger Automático
```yaml
on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]
```

**Quando você faz push ou PR, automaticamente:**

1. **Lint (2-3 min)**
   - Black verifica formatação
   - Pylint analisa qualidade
   - Flake8 valida PEP8

2. **Testes (4-6 min)**
   - Roda em Python 3.8, 3.9, 3.10, 3.11
   - Executa pytest com coverage
   - Upload para Codecov

3. **Security (1-2 min)**
   - Safety verifica vulnerabilidades
   - Bandit analisa código inseguro

4. **Build (2-3 min)**
   - Testa inicialização do servidor
   - Cria artefato empacotado
   - Upload para Actions

5. **Lighthouse (3-4 min)**
   - Performance score
   - Acessibilidade
   - Best practices
   - SEO

### Resultado Visual no GitHub
```
✅ Lint e Qualidade (2m 15s)
✅ Testes - Python 3.8 (3m 42s)
✅ Testes - Python 3.9 (3m 38s)
✅ Testes - Python 3.10 (3m 45s)
✅ Testes - Python 3.11 (3m 40s)
✅ Security Scan (1m 22s)
✅ Build e Validação (2m 18s)
✅ Lighthouse Performance (3m 55s)
```

---

## 🚢 Como Funciona o CD

### Deploy Automático por Branch/Tag

#### Staging (Push para `main`)
```bash
git push origin main
# Automaticamente deploya para Heroku staging
# URL: https://cyber-mole-staging.herokuapp.com
```

#### Production (Tag de versão)
```bash
git tag v1.1.0
git push origin v1.1.0
# Automaticamente:
# 1. Deploy Azure Production
# 2. Deploy GitHub Pages (docs)
# 3. Build e push Docker image
# 4. Cria GitHub Release
```

### Deploy Manual (Workflow Dispatch)
```
1. Acesse Actions no GitHub
2. Selecione "CD - Deploy Cyber Mole"
3. Clique "Run workflow"
4. Escolha ambiente (staging/production)
5. Confirme
```

---

## 🔧 Configuração de Secrets

### Necessários para CD:

#### Heroku
```
HEROKU_API_KEY
- Obter em: https://dashboard.heroku.com/account
- Settings → Secrets → New repository secret
```

#### Azure
```
AZURE_CREDENTIALS
- Obter via Azure CLI:
  az ad sp create-for-rbac --name "cyber-mole-deploy" --role contributor
- Copiar JSON output completo
```

#### Docker Hub
```
DOCKER_USERNAME
DOCKER_PASSWORD
- Usar credenciais Docker Hub
```

---

## 🎨 Usando Copilot para Criar Workflows

### Método 1: Chat do Copilot

```
@workspace crie um workflow do GitHub Actions para:
1. Rodar testes em Python 3.8-3.11
2. Fazer lint com pylint
3. Verificar cobertura de testes
4. Deploy automático no Heroku quando push em main
```

**Copilot gera workflow completo!**

### Método 2: Inline no Arquivo

Crie `.github/workflows/novo-workflow.yml`:

```yaml
name: # Digite "Test" e Ctrl+Space

# Copilot sugere:
on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      # ... resto do workflow
```

### Método 3: Comentários Descritivos

```yaml
# Workflow para deploy automático em staging e production
# Staging: push em main → Heroku
# Production: tag v* → Azure + Docker

# Copilot expande automaticamente com estrutura completa
```

---

## 📊 Exemplo Completo: Feature → Deploy

### 1. Desenvolver Feature
```bash
# Criar branch
git checkout -b feature/sound-system

# Desenvolver...
# Copilot ajuda no código
```

### 2. Commit com Copilot
```bash
git add .
# No VS Code Source Control, clicar ✨ "Generate Commit Message"
# Copilot gera:

feat(audio): implementa sistema completo de som cyberpunk

- Música de fundo em loop com volume ajustável
- Efeitos sonoros ao acertar/errar toupeira
- Som de contagem regressiva nos últimos 5s
- Controles independentes música/efeitos
- Arquivos otimizados (<100KB cada)

Performance: Áudios não impactam FPS
UX: Toggle mute/unmute intuitivo

Closes #1
```

### 3. Push e PR
```bash
git push origin feature/sound-system
# Criar PR no GitHub
```

### 4. CI Roda Automaticamente
```
✅ Todos os checks passam
✅ Coverage: 85%
✅ Lighthouse: 92/100
✅ No security issues
```

### 5. Merge e Deploy Staging
```bash
# Aprovar PR
git checkout main
git merge feature/sound-system
git push origin main

# CI/CD automaticamente:
# 1. Roda testes novamente
# 2. Build passa
# 3. Deploy staging Heroku
```

### 6. Release Production
```bash
# Testar em staging
# Se OK, criar tag:
git tag v1.1.0
git push origin v1.1.0

# CD automaticamente:
# 1. Deploy Azure Production
# 2. Build Docker image
# 3. Deploy Pages
# 4. Cria GitHub Release com changelog
```

---

## 🎯 Benefícios da Automação

### Antes (Manual)
```
❌ Commits inconsistentes
❌ Testes esquecidos
❌ Deploy manual com erros
❌ Sem histórico claro
❌ Difícil colaboração
⏱️ ~2-3 horas por release
```

### Depois (Com CI/CD)
```
✅ Commits padronizados
✅ Testes sempre executados
✅ Deploy confiável e rápido
✅ Changelog automático
✅ Fácil rollback
⏱️ ~15 minutos por release
```

---

## 📚 Recursos Adicionais

### Documentação
- [Conventional Commits](https://www.conventionalcommits.org/)
- [GitHub Actions Docs](https://docs.github.com/actions)
- [Copilot for Commits](https://docs.github.com/copilot/using-github-copilot/commit-messages)

### Ferramentas
- [Commitizen](https://github.com/commitizen/cz-cli) - CLI interativo
- [Husky](https://typicode.github.io/husky/) - Git hooks
- [Conventional Changelog](https://github.com/conventional-changelog/conventional-changelog)

---

**CYBER MOLE | CI/CD Guide | 2026** 🤖⚡
