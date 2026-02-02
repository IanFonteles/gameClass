# 🏷️ GitHub Issues & Labels - CYBER MOLE

## 📋 Sistema de Rótulos (Labels)

### 🎨 Por Categoria

#### Tipo de Trabalho
- 🐛 **bug** `#d73a4a` - Algo não está funcionando
- ✨ **enhancement** `#a2eeef` - Nova funcionalidade ou melhoria
- 📚 **documentation** `#0075ca` - Melhorias ou adições à documentação
- 🔧 **maintenance** `#fbca04` - Manutenção de código ou refatoração
- 🧪 **testing** `#1d76db` - Adicionar ou melhorar testes
- 🚀 **performance** `#e99695` - Otimização de performance

#### Prioridade
- 🔥 **priority: critical** `#b60205` - Precisa ser resolvido imediatamente
- ⚡ **priority: high** `#d93f0b` - Alta prioridade
- 📌 **priority: medium** `#fbca04` - Prioridade média
- 💤 **priority: low** `#0e8a16` - Baixa prioridade

#### Dificuldade
- 🌱 **difficulty: easy** `#7057ff` - Bom para iniciantes
- 🌿 **difficulty: medium** `#008672` - Requer conhecimento moderado
- 🌳 **difficulty: hard** `#d4c5f9` - Desafio técnico complexo

#### Área do Projeto
- 🎮 **area: gameplay** `#c5def5` - Mecânicas do jogo
- 🎨 **area: ui/ux** `#bfdadc` - Interface e experiência do usuário
- ⚙️ **area: backend** `#d4c5f9` - Lógica do servidor Flask
- 🌐 **area: frontend** `#fef2c0` - HTML/CSS/JavaScript
- 📱 **area: mobile** `#bfd4f2` - Responsividade mobile

#### Status
- 🚧 **status: in progress** `#fbca04` - Trabalho em andamento
- 🔍 **status: needs review** `#0e8a16` - Aguardando revisão
- ⏸️ **status: blocked** `#b60205` - Bloqueado por outro issue
- ✅ **status: ready** `#0075ca` - Pronto para desenvolvimento

---

## 🎯 Issues Planejadas

### Issue #1: 🎵 Adicionar Sistema de Som e Música

**Labels:** `enhancement`, `priority: high`, `area: gameplay`, `difficulty: medium`

**Descrição:**
Implementar sistema completo de áudio para tornar o jogo mais imersivo com tema cyberpunk.

**Requisitos:**
- [ ] Música de fundo cyberpunk (loop infinito)
- [ ] Efeito sonoro ao acertar toupeira (som eletrônico)
- [ ] Som ao errar o clique (som de erro digital)
- [ ] Som de contagem regressiva nos últimos 5 segundos
- [ ] Som de vitória ao finalizar jogo
- [ ] Controles de volume (mute/unmute)
- [ ] Toggle para música de fundo separado de efeitos sonoros

**Implementação Sugerida:**
```javascript
const sounds = {
    hit: new Audio('/static/sounds/cyber_hit.mp3'),
    miss: new Audio('/static/sounds/error.mp3'),
    bgMusic: new Audio('/static/sounds/cyberpunk_bg.mp3'),
    countdown: new Audio('/static/sounds/countdown.mp3'),
    gameOver: new Audio('/static/sounds/victory.mp3')
};

// Loop música de fundo
sounds.bgMusic.loop = true;
sounds.bgMusic.volume = 0.3;
```

**Recursos Necessários:**
- Arquivos de áudio (.mp3 ou .ogg)
- Biblioteca de sons cyberpunk royalty-free
- Pasta `/static/sounds/` no projeto

**Critérios de Aceitação:**
- ✅ Sons tocam no momento correto
- ✅ Controles de volume funcionam
- ✅ Performance não é afetada
- ✅ Sons são temáticos (cyberpunk)

---

### Issue #2: 🏆 Sistema de Leaderboard e High Score

**Labels:** `enhancement`, `priority: high`, `area: backend`, `area: ui/ux`, `difficulty: hard`

**Descrição:**
Criar sistema persistente de ranking com top 10 melhores pontuações.

**Requisitos:**
- [ ] Banco de dados para armazenar scores (SQLite ou JSON)
- [ ] Tela de leaderboard acessível do menu
- [ ] Input para nome do jogador ao bater recorde
- [ ] Top 10 scores com nome, pontos e data
- [ ] Filtro por dificuldade (LEVE/NORMAL/EXTREMO/INSANO)
- [ ] Animação neon ao entrar no top 10
- [ ] Badge especial para 1º lugar

**Estrutura de Dados:**
```python
# models.py
leaderboard_entry = {
    'id': 1,
    'player_name': 'CYBER_PLAYER',
    'score': 25,
    'difficulty': 'EXTREMO',
    'date': '2026-02-02',
    'timestamp': 1738454400
}
```

**Endpoints da API:**
- `GET /api/leaderboard` - Retorna top 10
- `GET /api/leaderboard/<difficulty>` - Filtrado por dificuldade
- `POST /api/leaderboard` - Adiciona novo score
- `GET /api/player-rank/<session_id>` - Posição do jogador atual

**Interface:**
```
╔════════════════════════════════════════╗
║      ⚡ TOP 10 CYBER MOLES ⚡         ║
╠════╦═══════════════╦══════╦═══════════╣
║ #  ║ JOGADOR       ║ PTS  ║ NÍVEL     ║
╠════╬═══════════════╬══════╬═══════════╣
║ 🥇 ║ NEON_MASTER   ║  45  ║ INSANO    ║
║ 🥈 ║ CYBER_ACE     ║  38  ║ EXTREMO   ║
║ 🥉 ║ DIGITAL_PRO   ║  35  ║ EXTREMO   ║
╚════╩═══════════════╩══════╩═══════════╝
```

**Critérios de Aceitação:**
- ✅ Scores persistem após fechar o jogo
- ✅ Interface neon cyberpunk
- ✅ Performance com 1000+ entradas
- ✅ Validação de nomes (3-15 caracteres)

---

### Issue #3: 💥 Efeitos de Partículas ao Acertar

**Labels:** `enhancement`, `priority: medium`, `area: frontend`, `difficulty: medium`

**Descrição:**
Adicionar explosão de partículas neon quando acertar uma toupeira.

**Requisitos:**
- [ ] Explosão de 10-15 partículas ao acertar
- [ ] Partículas em cores cyan/magenta/lime
- [ ] Animação de dispersão radial
- [ ] Fade out gradual das partículas
- [ ] Performance otimizada (Canvas ou CSS)

**Implementação Sugerida:**
```javascript
function createParticles(x, y) {
    const colors = ['#00ffff', '#ff00ff', '#00ff00'];
    for (let i = 0; i < 12; i++) {
        const particle = document.createElement('div');
        particle.className = 'particle';
        particle.style.left = x + 'px';
        particle.style.top = y + 'px';
        particle.style.background = colors[Math.floor(Math.random() * 3)];
        
        const angle = (Math.PI * 2 * i) / 12;
        const velocity = 100;
        const dx = Math.cos(angle) * velocity;
        const dy = Math.sin(angle) * velocity;
        
        particle.style.setProperty('--dx', dx + 'px');
        particle.style.setProperty('--dy', dy + 'px');
        
        document.body.appendChild(particle);
        
        setTimeout(() => particle.remove(), 600);
    }
}
```

**CSS:**
```css
.particle {
    position: absolute;
    width: 8px;
    height: 8px;
    border-radius: 50%;
    pointer-events: none;
    animation: particleExplode 0.6s ease-out forwards;
    box-shadow: 0 0 10px currentColor;
}

@keyframes particleExplode {
    to {
        transform: translate(var(--dx), var(--dy));
        opacity: 0;
        scale: 0;
    }
}
```

---

### Issue #4: 🎯 Tipos Especiais de Toupeiras

**Labels:** `enhancement`, `priority: medium`, `area: gameplay`, `difficulty: hard`

**Descrição:**
Adicionar variedade ao gameplay com toupeiras especiais com comportamentos diferentes.

**Tipos de Toupeiras:**

#### 🚀 **Toupeira Turbo** (Verde Neon)
- Aparece e desaparece 2x mais rápido
- Vale 3 pontos
- Probabilidade: 15%

#### 💎 **Toupeira Bônus** (Dourada)
- Fica 2x mais tempo
- Vale 5 pontos
- Cura efeito especial visual (sparkle)
- Probabilidade: 8%

#### 👻 **Toupeira Fantasma** (Transparente)
- Aparece semi-transparente
- Vale 4 pontos
- Mais difícil de ver
- Probabilidade: 12%

#### 💣 **Toupeira Bomba** (Vermelha)
- Se acertar: -5 pontos e perde 3 segundos
- Visual com símbolo de caveira
- Probabilidade: 5%

**Estrutura de Dados:**
```javascript
const moleTypes = {
    normal: { points: 1, duration: 800, color: 'default', probability: 60 },
    turbo: { points: 3, duration: 400, color: '#00ff00', probability: 15 },
    bonus: { points: 5, duration: 1600, color: '#ffd700', probability: 8 },
    ghost: { points: 4, duration: 800, color: 'rgba(0,255,255,0.3)', probability: 12 },
    bomb: { points: -5, duration: 1000, color: '#ff0000', probability: 5 }
};
```

**Critérios de Aceitação:**
- ✅ Cada tipo tem visual distinto
- ✅ Probabilidades balanceadas
- ✅ Pontuação funcionando corretamente
- ✅ Toupeira Bomba claramente identificável

---

### Issue #5: 📊 Sistema de Conquistas (Achievements)

**Labels:** `enhancement`, `priority: medium`, `area: ui/ux`, `difficulty: medium`

**Descrição:**
Implementar sistema de conquistas para aumentar engajamento e replay value.

**Conquistas Planejadas:**

🏅 **Iniciante Cibernético**
- Descrição: Acerte 10 toupeiras
- Recompensa: Badge Bronze
- Ícone: 🥉

🏅 **Caçador Digital**
- Descrição: Acerte 50 toupeiras
- Recompensa: Badge Prata
- Ícone: 🥈

🏅 **Mestre Cyber**
- Descrição: Acerte 100 toupeiras (total)
- Recompensa: Badge Ouro
- Ícone: 🥇

⚡ **Velocista**
- Descrição: Acerte 5 toupeiras em 5 segundos
- Recompensa: Título "Relâmpago"
- Ícone: ⚡

🎯 **Precisão Perfeita**
- Descrição: Complete um jogo sem errar um clique
- Recompensa: Título "Sniper"
- Ícone: 🎯

🔥 **Combo Master**
- Descrição: Acerte 8 toupeiras consecutivas
- Recompensa: Efeito especial "Chama Neon"
- Ícone: 🔥

💀 **Sobrevivente**
- Descrição: Complete nível INSANO com 15+ pontos
- Recompensa: Skin especial de toupeira
- Ícone: 💀

**Interface:**
```
┌─────────────────────────────────────┐
│  🏆 CONQUISTAS DESBLOQUEADAS: 4/15  │
├─────────────────────────────────────┤
│  ✅ 🥉 Iniciante Cibernético        │
│  ✅ ⚡ Velocista                     │
│  ✅ 🎯 Precisão Perfeita             │
│  ✅ 🥈 Caçador Digital               │
│  🔒 🥇 Mestre Cyber (73/100)        │
│  🔒 🔥 Combo Master                  │
└─────────────────────────────────────┘
```

**Armazenamento:**
```javascript
localStorage.setItem('achievements', JSON.stringify({
    earned: ['iniciante', 'velocista', 'precisao'],
    progress: {
        mestre: { current: 73, target: 100 },
        combo: { current: 5, target: 8 }
    }
}));
```

---

### Issue #6: 🎨 Skins e Temas Customizáveis

**Labels:** `enhancement`, `priority: low`, `area: ui/ux`, `difficulty: medium`

**Descrição:**
Permitir que jogadores escolham diferentes temas visuais além do cyberpunk.

**Temas Planejados:**

#### 🌸 **Synthwave Retro**
- Cores: Rosa, roxo, laranja
- Estilo: Anos 80, grid neon
- Sol retro no fundo

#### 🌌 **Matrix Code**
- Cores: Verde fosforescente
- Estilo: Código caindo
- Toupeiras com caracteres japoneses

#### ⚡ **Neon City**
- Cores: Azul, roxo, rosa
- Estilo: Cidade noturna
- Arranha-céus ao fundo

#### 🤖 **Industrial Dark**
- Cores: Cinza, laranja, vermelho
- Estilo: Fábrica robótica
- Metal e engrenagens

**Seletor de Temas:**
```html
<div class="theme-selector">
    <button data-theme="cyberpunk">⚡ Cyberpunk</button>
    <button data-theme="synthwave">🌸 Synthwave</button>
    <button data-theme="matrix">🌌 Matrix</button>
    <button data-theme="neon-city">🌃 Neon City</button>
    <button data-theme="industrial">🤖 Industrial</button>
</div>
```

**Implementação:**
```javascript
function applyTheme(themeName) {
    document.body.className = `theme-${themeName}`;
    localStorage.setItem('selectedTheme', themeName);
}
```

---

### Issue #7: 📱 PWA e Instalação no Mobile

**Labels:** `enhancement`, `priority: medium`, `area: mobile`, `difficulty: medium`

**Descrição:**
Transformar o jogo em Progressive Web App para instalação em dispositivos móveis.

**Requisitos:**
- [ ] Manifest.json com ícones e metadados
- [ ] Service Worker para cache offline
- [ ] Ícones em múltiplas resoluções (192x192, 512x512)
- [ ] Splash screen customizada
- [ ] Funcionar 100% offline após primeira visita
- [ ] Otimizações touch para mobile

**manifest.json:**
```json
{
  "name": "Cyber Mole - Whack-a-Mole Futurista",
  "short_name": "Cyber Mole",
  "description": "Jogo de reflexos com tema cyberpunk",
  "start_url": "/",
  "display": "standalone",
  "background_color": "#0a0e27",
  "theme_color": "#00ffff",
  "orientation": "portrait",
  "icons": [
    {
      "src": "/static/icons/icon-192.png",
      "sizes": "192x192",
      "type": "image/png"
    },
    {
      "src": "/static/icons/icon-512.png",
      "sizes": "512x512",
      "type": "image/png"
    }
  ]
}
```

---

### Issue #8: 🐛 Bug: Toupeira Aparece Duas Vezes na Mesma Toca

**Labels:** `bug`, `priority: high`, `area: gameplay`, `difficulty: easy`

**Descrição:**
Ocasionalmente, duas toupeiras aparecem na mesma toca simultaneamente, causando comportamento inesperado.

**Passos para Reproduzir:**
1. Iniciar jogo em nível INSANO
2. Jogar por ~10 segundos
3. Observar que às vezes 2 toupeiras ocupam mesmo espaço

**Comportamento Esperado:**
Apenas uma toupeira por toca por vez.

**Comportamento Atual:**
Múltiplas toupeiras podem sobrepor na mesma toca.

**Causa Provável:**
```javascript
// Problema: Não verifica se buraco já está ocupado
function randomHole(holes) {
    const idx = Math.floor(Math.random() * holes.length);
    return holes[idx]; // Pode retornar buraco ocupado
}
```

**Solução Proposta:**
```javascript
function randomHole(holes) {
    const availableHoles = holes.filter(hole => 
        !hole.classList.contains('occupied')
    );
    if (availableHoles.length === 0) return null;
    const idx = Math.floor(Math.random() * availableHoles.length);
    return availableHoles[idx];
}
```

---

### Issue #9: 🔧 Refatorar JavaScript em Módulos Separados

**Labels:** `maintenance`, `priority: medium`, `area: frontend`, `difficulty: medium`

**Descrição:**
Separar JavaScript monolítico em módulos ES6 para melhor organização e manutenibilidade.

**Estrutura Proposta:**
```
/static/js/
├── game.js           # Lógica principal do jogo
├── ui.js             # Manipulação de interface
├── audio.js          # Sistema de som
├── particles.js      # Efeitos visuais
├── leaderboard.js    # Sistema de ranking
├── achievements.js   # Sistema de conquistas
└── main.js           # Entry point
```

**Exemplo de Módulo:**
```javascript
// game.js
export class Game {
    constructor(config) {
        this.score = 0;
        this.timeLeft = config.duration;
        this.difficulty = config.difficulty;
    }
    
    start() { /* ... */ }
    end() { /* ... */ }
    hit(mole) { /* ... */ }
}

// main.js
import { Game } from './game.js';
import { UI } from './ui.js';
import { AudioManager } from './audio.js';

const game = new Game({ difficulty: 'NORMAL', duration: 30 });
```

---

### Issue #10: 🧪 Adicionar Testes Automatizados

**Labels:** `testing`, `priority: high`, `difficulty: hard`

**Descrição:**
Implementar suite de testes para garantir qualidade e prevenir regressões.

**Tipos de Testes:**

#### Unit Tests (pytest)
```python
# test_app.py
def test_score_endpoint():
    response = client.get('/api/score/test-session')
    assert response.status_code == 200
    assert 'score' in response.json

def test_leaderboard_sorting():
    scores = get_leaderboard()
    assert scores[0]['score'] >= scores[1]['score']
```

#### E2E Tests (Playwright/Selenium)
```javascript
// test_gameplay.spec.js
test('deve aumentar score ao clicar na toupeira', async ({ page }) => {
    await page.goto('http://localhost:5000');
    await page.click('button:has-text("► INICIAR JOGO ◄")');
    
    // Espera toupeira aparecer
    await page.waitForSelector('.mole.show');
    await page.click('.mole.show');
    
    const score = await page.textContent('.stat-value');
    expect(parseInt(score)).toBeGreaterThan(0);
});
```

#### Performance Tests
```python
# test_performance.py
def test_response_time():
    start = time.time()
    response = client.get('/')
    duration = time.time() - start
    assert duration < 0.1  # < 100ms
```

**Cobertura Alvo:**
- Backend: 80%+
- Frontend: 70%+
- Critical paths: 100%

---

## 📈 Roadmap de Desenvolvimento

### Fase 1: Core Features (v1.0) ✅
- [x] Mecânica básica do jogo
- [x] Sistema de pontuação
- [x] Timer e dificuldades
- [x] Tema cyberpunk visual

### Fase 2: Engajamento (v1.1) 🚧
- [ ] Issue #1: Sistema de som
- [ ] Issue #2: Leaderboard
- [ ] Issue #5: Conquistas
- [ ] Issue #8: Correção de bugs

### Fase 3: Conteúdo (v1.2) 📋
- [ ] Issue #3: Efeitos de partículas
- [ ] Issue #4: Toupeiras especiais
- [ ] Issue #6: Temas customizáveis

### Fase 4: Polimento (v1.3) 🔮
- [ ] Issue #7: PWA mobile
- [ ] Issue #9: Refatoração
- [ ] Issue #10: Testes automatizados
- [ ] Otimizações de performance
- [ ] Acessibilidade (WCAG 2.1)

---

## 🤝 Como Contribuir

### Escolhendo uma Issue
1. Procure issues com label `difficulty: easy` se é iniciante
2. Verifique se não está marcada como `status: in progress`
3. Comente na issue que você vai trabalhar nela

### Workflow
```bash
# 1. Fork e clone o repositório
git clone https://github.com/seu-usuario/cyber-mole.git

# 2. Crie uma branch
git checkout -b feature/issue-1-sound-system

# 3. Faça suas alterações
# ... código ...

# 4. Commit com mensagem descritiva
git commit -m "feat: adiciona sistema de som (#1)"

# 5. Push e crie Pull Request
git push origin feature/issue-1-sound-system
```

### Padrão de Commits
```
feat: nova funcionalidade (#issue)
fix: correção de bug (#issue)
docs: documentação (#issue)
style: formatação, sem mudança de código
refactor: refatoração de código
test: adição de testes
chore: tarefas de manutenção
```

---

## 📞 Contato e Suporte

- 🐛 **Reportar Bug:** Abra uma issue com label `bug`
- 💡 **Sugerir Feature:** Abra uma issue com label `enhancement`
- 📖 **Documentação:** Veja `/docs` no repositório
- 💬 **Discussões:** Use GitHub Discussions

---

**CYBER MOLE | GitHub Issues & Labels | 2026**
