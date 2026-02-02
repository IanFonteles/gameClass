# 🤖 CYBER MOLE

<div align="center">

![Version](https://img.shields.io/badge/version-1.0.0-00ffff?style=for-the-badge)
![Python](https://img.shields.io/badge/python-3.8+-ff00ff?style=for-the-badge&logo=python)
![Flask](https://img.shields.io/badge/flask-2.3.3-00ff00?style=for-the-badge&logo=flask)
![License](https://img.shields.io/badge/license-MIT-00ffff?style=for-the-badge)

**Jogo Whack-a-Mole futurista com tema cyberpunk e toupeiras robóticas** 🎮⚡

</div>

---

## 🎮 Sobre o Jogo

**CYBER MOLE** é uma reimaginação futurista do clássico jogo Whack-a-Mole, ambientado em um universo cyberpunk com toupeiras robóticas neon. Teste seus reflexos eliminando toupeiras cyber antes que elas escapem!

### ✨ Tema Cyberpunk
- 🎨 Visual neon com cores vibrantes (Cyan, Magenta, Lime)
- ⚡ Efeitos de brilho e animações dinâmicas
- 📺 Scanlines animadas estilo CRT
- 🤖 Toupeiras robóticas futuristas

---

## 🎯 Features

### 🎮 Gameplay
- ✅ 9 tocas interativas com toupeiras robóticas
- ✅ Sistema de pontuação em tempo real
- ✅ Timer com contagem regressiva
- ✅ 4 níveis de dificuldade (LEVE, NORMAL, EXTREMO, INSANO)
- ✅ Animações fluidas e responsivas

### 🎨 Visual
- ✅ Tema cyberpunk completo com neon colors
- ✅ Efeitos de glow e text-shadow
- ✅ Scanlines animadas
- ✅ Animação de pulse ao acertar
- ✅ Modal de Game Over estilizada
- ✅ Design 100% responsivo (mobile, tablet, desktop)

---

## 🚀 Instalação

### Pré-requisitos
- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)

### Passo a Passo

1. **Clone o repositório:**
```bash
git clone https://github.com/seu-usuario/cyber-mole.git
cd cyber-mole
```

2. **Instale as dependências:**
```bash
pip install -r requirements.txt
```

3. **Execute o jogo:**
```bash
python app.py
```

4. **Abra no navegador:**
```
http://localhost:5000
```

### Alternativa: Executar com Script
**Windows:**
```bash
RUN_GAME.bat
```

---

## 🎮 Como Jogar

1. **Selecione a dificuldade:**
   - 🟢 **LEVE** (40s) - Ideal para iniciantes
   - 🟡 **NORMAL** (30s) - Balanceado
   - 🟠 **EXTREMO** (20s) - Desafiador
   - 🔴 **INSANO** (15s) - Apenas para mestres cyber!

2. **Clique em "► INICIAR JOGO ◄"**

3. **Elimine as toupeiras:**
   - Clique nas toupeiras robóticas quando aparecerem
   - Cada acerto = +1 ponto
   - Seja rápido! Elas desaparecem rapidamente

4. **Veja sua pontuação final:**
   - Modal mostra quantas unidades você destruiu
   - Tente superar seu próprio recorde!

---

## 🛠️ Tecnologias

### Backend
- **Python 3.8+** - Linguagem principal
- **Flask 2.3.3** - Framework web minimalista
- **Werkzeug 2.3.7** - WSGI utilities

### Frontend
- **HTML5** - Estrutura semântica
- **CSS3** - Animações e efeitos neon
- **JavaScript (Vanilla)** - Lógica do jogo
- **CSS Grid** - Layout responsivo

---

## 📁 Estrutura do Projeto

```
cyber-mole/
├── app.py                          # Aplicação Flask completa
├── requirements.txt                # Dependências Python
├── RUN_GAME.bat                   # Script de execução Windows
├── .gitignore                     # Arquivos ignorados pelo Git
├── README.md                      # Este arquivo
│
├── .github/
│   └── ISSUE_TEMPLATE/
│       └── melhoria-visual-toupeira.md  # Template de issue
│
└── docs/
    ├── CYBERPUNK_THEME.md         # Detalhes do tema
    ├── GITHUB_ISSUES_LABELS.md    # Issues e labels planejadas
    ├── GITHUB_MCP_SETUP.md        # Setup GitHub MCP + Copilot
    └── ... (documentação adicional)
```

---

## 🗺️ Roadmap

### ✅ v1.0 - Core Features (Completo)
- [x] Mecânica básica do jogo
- [x] Sistema de pontuação
- [x] Timer e níveis de dificuldade
- [x] Tema cyberpunk completo
- [x] Design responsivo

### 🚧 v1.1 - Engajamento (Em Planejamento)
- [ ] 🎵 Sistema de som e música cyberpunk
- [ ] 🏆 Leaderboard com persistência
- [ ] 📊 Sistema de conquistas
- [ ] 🐛 Correções de bugs

### 📋 v1.2 - Conteúdo (Futuro)
- [ ] 💥 Efeitos de partículas
- [ ] 🎯 Toupeiras especiais (Turbo, Bônus, Fantasma, Bomba)
- [ ] 🎨 Skins e temas customizáveis
- [ ] 🤖 Melhorar visual da toupeira

---

## 🤝 Como Contribuir

Contribuições são muito bem-vindas! 🎉

1. Fork o projeto
2. Crie uma branch (`git checkout -b feature/nova-feature`)
3. Commit suas mudanças (`git commit -m 'feat: adiciona nova feature'`)
4. Push para a branch (`git push origin feature/nova-feature`)
5. Abra um Pull Request

### Padrão de Commits
- `feat:` Nova funcionalidade
- `fix:` Correção de bug
- `docs:` Documentação
- `refactor:` Refatoração
- `test:` Testes

---

## 📄 Licença

Este projeto está sob a licença **MIT**.

---

<div align="center">

**⚡ CYBER MOLE | 2026 ⚡**

Feito com Python 🐍 + Flask ⚗️ + GitHub Copilot 🤖

</div>### Quantidade de Tocas
- Procure por `const numHoles = 9;`
- Altere o número para mais ou menos tocas

### Duração do Jogo
- Procure por `gameState.timeLeft = 30;` (para cada dificuldade)
- Altere os valores conforme desejar

### Porta do Servidor
- No arquivo `app.py`, mude `app.run(debug=True, port=5000)`
- Altere o número 5000 para a porta desejada

## Dicas de Jogo

- 🎯 Prepare-se para clicar rapidamente no nível Expert
- 👀 Mantenha os olhos em toda a tela
- ⚡ No nível Expert, o tempo é seu maior inimigo
- 💪 Pratique para melhorar seu recorde!

## Notas

- O jogo é totalmente funcional no navegador
- Compatível com desktop e dispositivos mobile
- Sem dependências externas além do Flask (muito leve!)
- Ideal para aprender Flask, JavaScript e design web
- **Roda sem problemas em Windows, Mac e Linux**

## Desenvolvido com ❤️ em Python

Divirta-se jogando! 🎉
