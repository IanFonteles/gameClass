# 🔌 GitHub MCP + Copilot Chat - Guia Completo

## 📋 O que é MCP (Model Context Protocol)?

O **Model Context Protocol (MCP)** é um protocolo que permite ao Copilot Chat conectar-se diretamente a serviços externos como GitHub, fornecendo acesso em tempo real a:

- 📦 Repositórios e código
- 🐛 Issues e Pull Requests
- 📊 Projetos e Milestones
- 👥 Discussões e comentários
- 📈 Estatísticas e insights

---

## 🚀 Configuração do GitHub MCP

### Passo 1: Verificar Extensões Necessárias

Certifique-se de ter instalado:
- ✅ **GitHub Copilot** (`GitHub.copilot`)
- ✅ **GitHub Copilot Chat** (`GitHub.copilot-chat`)
- ✅ **GitHub Pull Requests** (`GitHub.vscode-pull-request-github`) - Opcional mas recomendado

### Passo 2: Instalar GitHub CLI (gh)

O MCP do GitHub usa o GitHub CLI para autenticação.

#### Windows (PowerShell):
```powershell
# Via winget
winget install --id GitHub.cli

# OU via Chocolatey
choco install gh

# OU via Scoop
scoop install gh
```

#### Verificar Instalação:
```bash
gh --version
# Saída esperada: gh version 2.x.x
```

### Passo 3: Autenticar no GitHub

```bash
# Autenticar com sua conta GitHub
gh auth login

# Escolha as opções:
# ? What account do you want to log into? GitHub.com
# ? What is your preferred protocol for Git operations? HTTPS
# ? Authenticate Git with your GitHub credentials? Yes
# ? How would you like to authenticate GitHub CLI? Login with a web browser
```

Siga as instruções no navegador para autorizar o GitHub CLI.

### Passo 4: Verificar Autenticação

```bash
# Verificar status
gh auth status

# Testar conexão
gh repo list
```

### Passo 5: Configurar MCP no VS Code

1. Abra as **Configurações** (`Ctrl+,`)
2. Pesquise por `@ext:github.copilot-chat mcp`
3. Ou edite `settings.json` diretamente:

```json
{
  "github.copilot.chat.mcp.enabled": true,
  "github.copilot.chat.mcp.servers": {
    "github": {
      "command": "gh",
      "args": ["copilot", "mcp"],
      "env": {}
    }
  }
}
```

### Passo 6: Reiniciar VS Code

Feche e reabra o VS Code para aplicar as configurações.

---

## 💬 Usando Copilot Chat com GitHub MCP

### Abrir Copilot Chat

- **Atalho:** `Ctrl+Shift+I` (Windows/Linux) ou `Cmd+Shift+I` (Mac)
- **Comando:** `View: Toggle Copilot Chat`
- **Sidebar:** Ícone do Copilot na barra lateral

### Verificar se MCP está Ativo

No Copilot Chat, digite:
```
@github status
```

Se o MCP estiver ativo, você verá informações sobre sua conexão GitHub.

---

## 🎯 Comandos Úteis com GitHub MCP

### 📦 Gerenciamento de Repositórios

#### Criar novo repositório
```
@github crie um repositório público chamado "cyber-mole" com descrição "Jogo Whack-a-Mole futurista com tema cyberpunk"
```

#### Listar seus repositórios
```
@github liste meus repositórios públicos
```

#### Ver detalhes de um repositório
```
@github mostre informações sobre o repositório cyber-mole
```

#### Clonar repositório
```
@github clone o repositório cyber-mole na pasta C:\Workspaces
```

---

### 🐛 Gerenciamento de Issues

#### Criar issue
```
@github crie uma issue no repositório cyber-mole:
Título: 🎵 Adicionar Sistema de Som
Labels: enhancement, priority-high
Descrição: Implementar música de fundo e efeitos sonoros com tema cyberpunk
```

#### Listar issues abertas
```
@github liste as issues abertas do repositório cyber-mole
```

#### Filtrar issues por label
```
@github mostre as issues com label "bug" do repositório cyber-mole
```

#### Fechar issue
```
@github feche a issue #8 do repositório cyber-mole com comentário "Bug corrigido na versão 1.1"
```

#### Adicionar comentário em issue
```
@github comente na issue #5: "Implementação iniciada, previsão de conclusão: 3 dias"
```

---

### 🏷️ Gerenciamento de Labels

#### Criar labels
```
@github crie os seguintes labels no repositório cyber-mole:
- bug (#d73a4a)
- enhancement (#a2eeef)
- priority-high (#d93f0b)
- area-gameplay (#c5def5)
```

#### Listar labels
```
@github liste todos os labels do repositório cyber-mole
```

#### Adicionar label a issue
```
@github adicione o label "priority-high" na issue #3
```

---

### 🔀 Pull Requests

#### Criar PR
```
@github crie um pull request:
From: feature/sound-system
To: main
Título: feat: adiciona sistema de som (#1)
Descrição: Implementa música de fundo e efeitos sonoros cyberpunk
```

#### Listar PRs abertos
```
@github liste os pull requests abertos do cyber-mole
```

#### Revisar PR
```
@github mostre as mudanças do PR #12
```

#### Mergear PR
```
@github faça merge do PR #12 usando squash
```

---

### 📊 Projetos e Milestones

#### Criar milestone
```
@github crie um milestone no cyber-mole:
Título: v1.1 - Engajamento
Data: 2026-03-01
Descrição: Features de som, leaderboard e conquistas
```

#### Associar issue a milestone
```
@github adicione a issue #1 ao milestone "v1.1 - Engajamento"
```

#### Ver progresso do milestone
```
@github mostre o progresso do milestone "v1.1 - Engajamento"
```

---

### 📈 Estatísticas e Insights

#### Ver commits recentes
```
@github mostre os últimos 10 commits do cyber-mole
```

#### Ver contribuidores
```
@github liste os contribuidores do cyber-mole
```

#### Estatísticas do repositório
```
@github mostre estatísticas do repositório cyber-mole (stars, forks, issues, PRs)
```

#### Ver atividade recente
```
@github mostre a atividade recente do cyber-mole
```

---

### 🔍 Busca de Código

#### Buscar em um repositório
```
@github busque "function randomHole" no repositório cyber-mole
```

#### Buscar issues por palavra-chave
```
@github busque issues contendo "toupeira" no cyber-mole
```

#### Ver arquivo específico
```
@github mostre o conteúdo do arquivo app.py no cyber-mole
```

---

## 🎨 Exemplo: Configurando Cyber Mole no GitHub

### 1. Criar Repositório
```
@github crie um repositório público "cyber-mole" com:
Descrição: 🤖 Jogo Whack-a-Mole futurista com tema cyberpunk e toupeiras robóticas
Topics: game, python, flask, cyberpunk, javascript, whack-a-mole
```

### 2. Criar Labels
```
@github crie os labels no cyber-mole:
- 🐛 bug (#d73a4a): Algo não está funcionando
- ✨ enhancement (#a2eeef): Nova funcionalidade
- 🔥 priority-critical (#b60205): Urgente
- ⚡ priority-high (#d93f0b): Alta prioridade
- 🎮 area-gameplay (#c5def5): Mecânicas do jogo
- 🎨 area-ui-ux (#bfdadc): Interface do usuário
```

### 3. Criar Issues do Roadmap
```
@github crie uma issue no cyber-mole:
Título: 🎵 Sistema de Som e Música
Labels: enhancement, priority-high, area-gameplay
Descrição:
Implementar sistema completo de áudio:
- [ ] Música de fundo cyberpunk
- [ ] Efeito sonoro ao acertar toupeira
- [ ] Som de erro ao errar clique
- [ ] Controles de volume
- [ ] Toggle mute/unmute
```

### 4. Criar Milestone
```
@github crie um milestone no cyber-mole:
Título: v1.1 - Engajamento
Data: 2026-03-15
Descrição: Features de som, leaderboard, conquistas e correções de bugs
```

### 5. Inicializar Repositório Local
```bash
cd C:\Workspaces\gameClass

# Inicializar Git
git init

# Adicionar arquivos
git add .

# Commit inicial
git commit -m "feat: versão inicial do Cyber Mole com tema cyberpunk"

# Conectar ao GitHub
git remote add origin https://github.com/seu-usuario/cyber-mole.git

# Push inicial
git branch -M main
git push -u origin main
```

---

## 🔥 Comandos Avançados

### Criar Issue Complexa com Template
```
@github crie uma issue detalhada no cyber-mole:

**Título:** 🏆 Sistema de Leaderboard

**Labels:** enhancement, priority-high, area-backend, difficulty-hard

**Descrição:**
## Objetivo
Criar sistema persistente de ranking com top 10 melhores pontuações.

## Requisitos
- [ ] Banco de dados SQLite
- [ ] API endpoints (/api/leaderboard)
- [ ] Interface neon cyberpunk
- [ ] Filtro por dificuldade
- [ ] Input para nome do jogador

## Estrutura de Dados
\`\`\`python
leaderboard_entry = {
    'player_name': 'CYBER_PLAYER',
    'score': 25,
    'difficulty': 'EXTREMO',
    'date': '2026-02-02'
}
\`\`\`

## Critérios de Aceitação
- ✅ Scores persistem após fechar jogo
- ✅ Performance com 1000+ entradas
- ✅ Interface integrada ao tema

**Milestone:** v1.1 - Engajamento
**Assignees:** @seu-usuario
```

### Workflow Completo de Feature
```
# 1. Criar branch
@github crie uma branch "feature/sound-system" no cyber-mole

# 2. Fazer alterações localmente
# ... editar código ...

# 3. Commit e push
git add .
git commit -m "feat: adiciona sistema de som (#1)"
git push origin feature/sound-system

# 4. Criar PR
@github crie um pull request no cyber-mole:
From: feature/sound-system
To: main
Título: feat: adiciona sistema de som (#1)
Body: Implementa sistema completo de áudio com música de fundo e efeitos sonoros cyberpunk. Closes #1

# 5. Solicitar review
@github solicite review de @colega no PR #15

# 6. Após aprovação, mergear
@github faça merge do PR #15 usando squash
```

---

## 🛠️ Troubleshooting

### MCP não está funcionando

#### Problema: `@github` não responde
```bash
# Verificar se gh está instalado
gh --version

# Verificar autenticação
gh auth status

# Re-autenticar se necessário
gh auth logout
gh auth login
```

#### Problema: "MCP server not found"
```json
// settings.json
{
  "github.copilot.chat.mcp.enabled": true,
  "github.copilot.chat.mcp.servers": {
    "github": {
      "command": "gh",
      "args": ["copilot", "mcp"]
    }
  }
}
```

Reinicie o VS Code após salvar.

#### Problema: Permissões insuficientes
```bash
# Verificar scopes autorizados
gh auth status

# Adicionar scopes necessários
gh auth refresh -s repo,read:org,read:project
```

---

## 📚 Recursos Adicionais

### Documentação Oficial
- [GitHub CLI](https://cli.github.com/manual/)
- [GitHub Copilot Chat](https://docs.github.com/en/copilot/using-github-copilot/using-github-copilot-chat)
- [Model Context Protocol](https://modelcontextprotocol.io/)

### Comandos GitHub CLI Úteis
```bash
# Ver todos os comandos
gh help

# Comandos específicos
gh issue list
gh pr list
gh repo view
gh workflow list
gh release list
```

### Aliases Úteis
```bash
# Adicionar aliases no Git
git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.ci commit
git config --global alias.st status
```

---

## 🎯 Próximos Passos para Cyber Mole

1. **Inicializar repositório:**
   ```bash
   cd C:\Workspaces\gameClass
   git init
   git add .
   git commit -m "feat: versão inicial Cyber Mole"
   ```

2. **Criar no GitHub via MCP:**
   ```
   @github crie um repositório público cyber-mole
   ```

3. **Push inicial:**
   ```bash
   git remote add origin https://github.com/seu-usuario/cyber-mole.git
   git push -u origin main
   ```

4. **Criar issues do roadmap:**
   ```
   @github crie as 10 issues do arquivo GITHUB_ISSUES_LABELS.md
   ```

5. **Configurar projeto board:**
   ```
   @github crie um projeto board "Cyber Mole Roadmap" com colunas: Backlog, To Do, In Progress, Done
   ```

---

## 💡 Dicas de Produtividade

### Use Comandos Naturais
O MCP entende linguagem natural. Seja específico mas natural:
```
✅ "crie uma issue sobre adicionar sons no jogo"
✅ "mostre as 5 issues mais antigas abertas"
✅ "feche todas as issues marcadas como duplicadas"
```

### Combine com @workspace
```
@github @workspace crie issues para cada TODO encontrado no código
```

### Automatize Workflows
```
@github crie um workflow GitHub Actions para:
- Rodar testes automaticamente em cada PR
- Deploy automático para GitHub Pages
- Verificar formatação do código
```

---

**CYBER MOLE | GitHub MCP Setup | 2026**
