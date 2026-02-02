# 🤖 Guia: Instalação e Uso de Agentes Personalizados do Copilot

## 📚 O que são Agentes Personalizados?

**Agentes personalizados** (Custom Agents) são extensões especializadas do GitHub Copilot que fornecem experiências interativas focadas em domínios específicos, como:
- Frameworks específicos (React, Vue, Angular)
- Linguagens (Python, Rust, Go)
- Práticas (Testing, Security, Performance)
- Domínios (Game Dev, Web3, AI/ML)

---

## 🌟 Awesome Copilot Collection

A **Awesome Copilot** é uma coleção curada de agentes e extensões personalizadas para GitHub Copilot.

### 📍 Repositório Oficial
```
https://github.com/cedrickchee/awesome-github-copilot
```

### 🎯 Categorias Populares
- **Web Development** - React, Vue, Next.js
- **Backend** - Node.js, Python, Rust
- **DevOps** - Docker, Kubernetes, CI/CD
- **Testing** - Jest, Pytest, Playwright
- **Security** - Code scanning, vulnerability detection
- **Game Development** - Unity, Unreal, Godot
- **AI/ML** - TensorFlow, PyTorch, scikit-learn

---

## 🚀 Instalação de Agente Personalizado

### Método 1: Via VS Code Extensions

#### Passo 1: Pesquisar no Marketplace
1. Abra VS Code
2. Clique no ícone de **Extensions** (`Ctrl+Shift+X`)
3. Pesquise por: `"copilot agent"` ou `"copilot extension"`

#### Passo 2: Instalar Agente
Exemplos de agentes úteis para Cyber Mole:

##### 1. **Python Copilot Agent**
```
Nome: Python Copilot
ID: ms-python.vscode-copilot-python
Foco: Flask, FastAPI, testes Python
```

##### 2. **Web Development Agent**
```
Nome: HTML CSS Support Copilot
ID: ecmel.vscode-html-css-copilot
Foco: HTML5, CSS3, animações
```

##### 3. **Game Development Agent**
```
Nome: Game Dev Copilot
ID: gamedev.copilot-gamedev
Foco: Lógica de jogos, física, animações
```

#### Passo 3: Configurar Agente
Após instalar, configure em `settings.json`:

```json
{
  "github.copilot.advanced": {
    "customAgents": {
      "python-dev": {
        "enabled": true,
        "model": "gpt-4",
        "context": ["Flask", "Python 3.8+", "REST API"]
      },
      "game-dev": {
        "enabled": true,
        "model": "gpt-4",
        "context": ["JavaScript games", "animations", "cyberpunk theme"]
      }
    }
  }
}
```

---

### Método 2: Criar Agente Personalizado

#### Estrutura de Agente Custom

##### 1. Criar Diretório
```bash
mkdir .github/copilot-agents
cd .github/copilot-agents
```

##### 2. Criar Configuração do Agente
```yaml
# .github/copilot-agents/cyber-mole-agent.yml

name: "Cyber Mole Game Dev Agent"
description: "Agente especializado em desenvolvimento de jogos cyberpunk"
version: "1.0.0"

capabilities:
  - game-logic
  - animation-optimization
  - cyberpunk-styling
  - performance-tuning

context:
  project_type: "web-game"
  framework: "Flask + Vanilla JS"
  theme: "cyberpunk-neon"
  
  colors:
    primary: "#00ffff"
    secondary: "#ff00ff"
    accent: "#00ff00"

prompts:
  coding_style: |
    Gere código seguindo estas diretrizes:
    - Tema cyberpunk com cores neon
    - Performance 60fps em animações
    - Mobile-first responsive
    - Comentários em português
    
  feature_suggestions: |
    Ao sugerir features:
    - Mantenha coerência com tema cyberpunk
    - Priorize experiência visual imersiva
    - Considere impacto em performance
    - Sugira incrementos testáveis

  code_review: |
    Ao revisar código:
    - Verifique uso correto das cores (#00ffff, #ff00ff, #00ff00)
    - Valide animações usando transform/opacity
    - Confirme responsividade mobile
    - Cheque tratamento de erros

behaviors:
  auto_complete:
    - Sugere nomes de classes com prefixo cyber-
    - Completa propriedades CSS com valores neon
    - Adiciona box-shadow e glow automaticamente
  
  code_generation:
    - Sempre incluir comentários explicativos
    - Adicionar type hints em Python
    - Usar JSDoc em JavaScript complexo
    
  refactoring:
    - Priorizar performance
    - Manter single file quando possível
    - Modularizar apenas quando necessário

examples:
  button_creation: |
    ```css
    .cyber-button {
      background: linear-gradient(135deg, #00ffff 0%, #ff00ff 100%);
      border: 2px solid #00ff00;
      box-shadow: 0 0 20px rgba(0, 255, 255, 0.5);
      color: #000;
      text-transform: uppercase;
      letter-spacing: 1px;
      transition: all 0.3s ease;
    }
    
    .cyber-button:hover {
      transform: translateY(-3px);
      box-shadow: 0 0 30px rgba(0, 255, 255, 0.8);
    }
    ```
  
  animation_creation: |
    ```css
    @keyframes cyberPulse {
      0% { transform: scale(1); box-shadow: 0 0 20px #00ffff; }
      50% { transform: scale(0.95); box-shadow: 0 0 30px #ff00ff; }
      100% { transform: scale(1); box-shadow: 0 0 20px #00ffff; }
    }
    ```

shortcuts:
  - trigger: "cyber-button"
    expansion: "Gera botão cyberpunk completo com hover"
  - trigger: "neon-glow"
    expansion: "Adiciona efeito de brilho neon com múltiplas camadas"
  - trigger: "game-state"
    expansion: "Cria objeto de estado do jogo com getters/setters"
```

##### 3. Ativar Agente
Em `settings.json`:
```json
{
  "github.copilot.advanced": {
    "agents": [
      {
        "name": "cyber-mole-agent",
        "config": ".github/copilot-agents/cyber-mole-agent.yml"
      }
    ]
  }
}
```

---

## 🎮 Usando Agentes no IDE

### 1. Via Chat do Copilot

#### Ativar Agente Específico
```
@cyber-mole-agent crie um botão com tema cyberpunk
```

#### Exemplos de Uso
```
@cyber-mole-agent adicione animação de pulso neon ao elemento
@cyber-mole-agent otimize esta animação para 60fps
@cyber-mole-agent crie toupeira especial com gradient magenta-cyan
@cyber-mole-agent adicione som de acerto com tema futurista
```

### 2. Via Inline Suggestions

#### Autocomplete Contextual
Digite comentário para ativar:
```javascript
// cyber-button com hover effect
// Copilot gerará código completo seguindo instruções do agente
```

### 3. Via Command Palette

#### Invocar Agente
1. `Ctrl+Shift+P`
2. Digite: `Copilot: Select Custom Agent`
3. Escolha: `Cyber Mole Game Dev Agent`
4. Use normalmente - sugestões seguirão contexto do agente

---

## 🎯 Agentes Recomendados para Cyber Mole

### 1. **Python/Flask Agent**

#### Instalação
```bash
code --install-extension ms-python.vscode-copilot-python
```

#### Uso no Projeto
```python
# @agent python-flask
# Criar endpoint para salvar highscore
# O agente sugerirá estrutura completa com validação
```

### 2. **CSS Animation Agent**

#### Instalação
```bash
code --install-extension animation-copilot.css-animations
```

#### Uso no Projeto
```css
/* @agent css-animation */
/* Criar animação de entrada da toupeira com rotação 360° */
```

### 3. **Game Logic Agent**

#### Criar Agente Custom
```yaml
# .github/copilot-agents/game-logic.yml
name: "Game Logic Agent"
focus: 
  - State management
  - Event handling
  - Collision detection
  - Score calculation
```

#### Uso
```javascript
// @agent game-logic
// Adicionar sistema de combo para pontos extras
```

---

## 🔧 Configuração Avançada

### Multi-Agent Setup

#### Combinar Múltiplos Agentes
```json
{
  "github.copilot.advanced": {
    "activeAgents": [
      "cyber-mole-agent",
      "python-flask",
      "css-animation",
      "game-logic"
    ],
    "agentPriority": {
      "*.py": ["python-flask", "cyber-mole-agent"],
      "*.css": ["css-animation", "cyber-mole-agent"],
      "*.js": ["game-logic", "cyber-mole-agent"]
    }
  }
}
```

### Context Sharing

#### Compartilhar Contexto Entre Agentes
```yaml
# shared-context.yml
project:
  name: "Cyber Mole"
  theme: "cyberpunk-neon"
  
  colors:
    primary: "#00ffff"
    secondary: "#ff00ff"
    accent: "#00ff00"
  
  stack:
    backend: "Flask 2.3.3"
    frontend: "Vanilla JS"
    styling: "CSS3"
  
  guidelines:
    - "Mobile-first responsive"
    - "60fps animations"
    - "Neon glow effects"
    - "Uppercase labels"
```

---

## 📊 Exemplos Práticos

### Exemplo 1: Criar Sistema de Som

#### Com Agente Python
```
@python-flask crie endpoint /api/sounds para gerenciar sons do jogo
```

**Resultado:**
```python
from flask import jsonify, request

@app.route('/api/sounds', methods=['GET'])
def get_sounds():
    """
    Retorna lista de sons disponíveis
    
    Returns:
        JSON com lista de sons cyberpunk
    """
    sounds = {
        'hit': '/static/sounds/cyber_hit.mp3',
        'miss': '/static/sounds/error_beep.mp3',
        'background': '/static/sounds/cyberpunk_ambient.mp3'
    }
    return jsonify({'status': 'success', 'sounds': sounds})
```

### Exemplo 2: Criar Toupeira Especial

#### Com Agente Game Logic
```
@game-logic crie classe para toupeira "Turbo" com velocidade 2x
```

**Resultado:**
```javascript
class TurboMole extends Mole {
    constructor(holeElement) {
        super(holeElement);
        this.speed = 2;
        this.points = 3;
        this.color = '#00ff00';
        this.duration = 400; // metade do tempo normal
    }
    
    show() {
        super.show();
        this.element.classList.add('turbo-mole');
        this.element.style.background = `linear-gradient(135deg, ${this.color} 0%, #00ffff 100%)`;
    }
    
    hide() {
        super.hide();
        this.element.classList.remove('turbo-mole');
    }
}
```

### Exemplo 3: Animação de Partículas

#### Com Agente CSS Animation
```
@css-animation crie explosão de partículas neon ao acertar toupeira
```

**Resultado:**
```css
@keyframes particleExplode {
    0% {
        transform: translate(0, 0) scale(1);
        opacity: 1;
    }
    100% {
        transform: translate(var(--dx), var(--dy)) scale(0);
        opacity: 0;
    }
}

.particle {
    position: absolute;
    width: 8px;
    height: 8px;
    border-radius: 50%;
    background: var(--particle-color);
    box-shadow: 0 0 10px var(--particle-color);
    animation: particleExplode 0.6s ease-out forwards;
}
```

---

## 🎨 Customizar Agente para Cyber Mole

### Prompts Especializados

#### Criar `.github/copilot-prompts/cyberpunk.md`
```markdown
# Cyberpunk Coding Prompts

## Button Creation
Sempre que criar botão, use:
- Gradient cyan→magenta
- Border lime 2px
- Uppercase text
- Letter-spacing 1px
- Hover: translateY(-3px)

## Animation Creation
Animações devem:
- Usar transform e opacity (GPU)
- Duração 0.3s padrão
- Ease timing function
- Incluir fallback para browsers antigos

## Color Usage
- Texto importante: cyan (#00ffff)
- Backgrounds: dark gradient (#0a0e27 → #1a1a2e)
- Borders: magenta (#ff00ff) ou lime (#00ff00)
- Shadows: sempre com glow neon
```

### Vincular ao Copilot
```json
{
  "github.copilot.advanced": {
    "customPrompts": [
      ".github/copilot-prompts/cyberpunk.md"
    ]
  }
}
```

---

## 🧪 Testar Agente

### 1. Validar Sugestões
```javascript
// Teste: digitar "criar botão"
// Agente deve sugerir código com:
// ✅ Gradient cyan-magenta
// ✅ Border lime
// ✅ Box-shadow com glow
// ✅ Uppercase text
```

### 2. Verificar Contexto
```python
# Teste: digitar "criar endpoint"
# Agente deve sugerir:
# ✅ Docstring em português
# ✅ Try-except com logging
# ✅ Return JSON padronizado
# ✅ Type hints
```

### 3. Confirmar Performance
```css
/* Teste: digitar "animação de entrada"
   Agente deve evitar:
   ❌ width/height animado
   ❌ top/left animado
   
   Agente deve usar:
   ✅ transform
   ✅ opacity
   ✅ will-change quando necessário
*/
```

---

## 📚 Recursos Adicionais

### Documentação Oficial
- [GitHub Copilot Extensibility](https://docs.github.com/en/copilot/customizing-copilot)
- [Custom Agents Guide](https://code.visualstudio.com/docs/copilot/copilot-extensibility)

### Community Agents
- [Awesome Copilot](https://github.com/cedrickchee/awesome-github-copilot)
- [Copilot Extensions Marketplace](https://marketplace.visualstudio.com/search?term=copilot&target=VSCode)

### Tutoriais
- [Creating Custom Copilot Agents](https://www.youtube.com/watch?v=example)
- [Best Practices for Agent Configuration](https://blog.github.com/copilot-agents)

---

## 🎯 Próximos Passos

1. **Instalar Agentes Básicos:**
   - Python/Flask Agent
   - CSS Animation Agent
   - Game Logic Agent

2. **Configurar Cyber Mole Agent:**
   - Criar `cyber-mole-agent.yml`
   - Configurar prompts especializados
   - Testar sugestões contextuais

3. **Experimentar no Desenvolvimento:**
   - Usar `@cyber-mole-agent` no Chat
   - Testar autocomplete inline
   - Validar qualidade das sugestões

4. **Iterar e Melhorar:**
   - Coletar feedback das sugestões
   - Ajustar prompts conforme necessário
   - Adicionar mais exemplos ao agente

---

**CYBER MOLE | Custom Agents Setup | 2026** 🤖⚡
