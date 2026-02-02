# Instruções Personalizadas - GitHub Copilot

## 🎯 Contexto do Projeto

Este é o **CYBER MOLE**, um jogo Whack-a-Mole futurista com tema cyberpunk e toupeiras robóticas. O projeto foca em criar uma experiência visual impressionante mantendo código limpo e performático.

---

## 🎨 Estilo Visual e Design

### Paleta de Cores Obrigatória
- **Primária**: `#00ffff` (Cyan) - Elementos principais, bordas, texto destaque
- **Secundária**: `#ff00ff` (Magenta) - Acentos, bordas alternativas
- **Terciária**: `#00ff00` (Lime) - Labels, UI elements
- **Background**: `#0a0e27`, `#1a1a2e`, `#16213e` - Gradientes escuros

### Efeitos Visuais Requeridos
Sempre incluir ao criar novos elementos:
- Box-shadow com glow neon (múltiplas camadas)
- Text-shadow para texto importante
- Border com cores neon
- Transições suaves (0.3s ease)
- Animações cyberpunk quando apropriado

**Exemplo obrigatório de botão:**
```css
button {
    background: linear-gradient(135deg, #00ffff 0%, #ff00ff 100%);
    border: 2px solid #00ff00;
    box-shadow: 0 0 20px rgba(0, 255, 255, 0.5);
    color: #000;
    text-transform: uppercase;
    letter-spacing: 1px;
}
```

---

## 💻 Estilo de Codificação

### Python/Flask

#### Convenções
- Use **snake_case** para variáveis e funções
- Use **PascalCase** para classes
- Docstrings obrigatórias em funções públicas
- Type hints sempre que possível

#### Estrutura de Rotas
```python
@app.route('/api/<recurso>', methods=['GET', 'POST'])
def nome_descritivo():
    """Docstring explicando o propósito."""
    # Validação de entrada
    # Lógica de negócio
    # Retorno com JSON
    return jsonify({'status': 'success', 'data': resultado})
```

#### Tratamento de Erros
Sempre use try-except com logs:
```python
try:
    # operação
except Exception as e:
    print(f"Erro em <função>: {e}")
    return jsonify({'status': 'error', 'message': str(e)}), 500
```

### HTML/CSS

#### Estrutura HTML
- Use **tags semânticas** (`<section>`, `<article>`, `<nav>`)
- Classes descritivas com kebab-case: `.mole-hole`, `.cyber-button`
- IDs apenas quando necessário para JavaScript
- Atributos `data-*` para dados dinâmicos

#### CSS
- **Mobile-first**: Media queries para telas maiores
- **BEM naming** quando aplicável: `.block__element--modifier`
- Prefira **CSS Grid** e **Flexbox** sobre floats
- Animações com `@keyframes` nomeadas descritivamente
- Variáveis CSS para cores repetidas (considerar adicionar)

**Template de nova seção:**
```html
<section class="nova-secao">
    <div class="nova-secao__container">
        <h2 class="nova-secao__titulo">⚡ TÍTULO ⚡</h2>
        <div class="nova-secao__conteudo">
            <!-- conteúdo -->
        </div>
    </div>
</section>
```

### JavaScript

#### Convenções
- Use **camelCase** para variáveis e funções
- Use **PascalCase** para classes/constructors
- Prefira `const` e `let` sobre `var`
- Funções arrow quando apropriado
- Comentários JSDoc para funções complexas

#### Estrutura de Código
```javascript
/**
 * Descrição da função
 * @param {string} param1 - Descrição
 * @returns {boolean} Descrição do retorno
 */
function nomeFuncao(param1) {
    // Implementação
}
```

#### Event Listeners
Sempre use delegação quando possível:
```javascript
document.addEventListener('click', (e) => {
    if (e.target.matches('.cyber-button')) {
        // handler
    }
});
```

---

## 🏗️ Arquitetura e Organização

### Estrutura Atual (Single-File)
O projeto usa uma **arquitetura monolítica simplificada** com tudo em `app.py`. Para features novas:

#### Pequenas Adições
- Adicione diretamente no `app.py`
- Mantenha seções comentadas claramente

#### Features Médias/Grandes
Considere modularizar:
```
cyber-mole/
├── app.py                 # Entry point
├── static/
│   ├── css/
│   │   └── styles.css    # CSS separado
│   ├── js/
│   │   ├── game.js       # Lógica do jogo
│   │   ├── ui.js         # Interface
│   │   └── audio.js      # Sistema de som
│   └── sounds/
├── templates/
│   └── index.html        # HTML separado
└── models/
    └── leaderboard.py    # Modelos de dados
```

### Padrões Arquiteturais

#### API REST
Siga padrão RESTful:
- `GET /api/resource` - Listar
- `GET /api/resource/:id` - Detalhes
- `POST /api/resource` - Criar
- `PUT /api/resource/:id` - Atualizar
- `DELETE /api/resource/:id` - Deletar

#### Estado do Jogo
Use objeto centralizado:
```javascript
const gameState = {
    score: 0,
    timeLeft: 30,
    isPlaying: false,
    difficulty: 'NORMAL',
    // ... outros estados
};
```

---

## 🎮 Mecânicas do Jogo

### Princípios de Design
1. **Feedback Imediato**: Toda ação do usuário deve ter resposta visual/sonora
2. **Progressive Difficulty**: Dificuldades devem ser claramente diferenciadas
3. **Fair Challenge**: Bugs que prejudiquem jogabilidade são prioridade crítica
4. **Cyberpunk Immersion**: Todas as features devem reforçar o tema

### Implementação de Novas Features

#### Toupeiras Especiais
Sempre seguir estrutura:
```javascript
const moleType = {
    id: 'tipo-unico',
    points: 3,
    duration: 600,
    color: '#cor-neon',
    probability: 15, // porcentagem
    onHit: function() {
        // comportamento especial
    }
};
```

#### Novos Níveis de Dificuldade
Manter progressão lógica:
- Tempo decrescente
- Velocidade das toupeiras aumentando
- Nunca impossível (sempre deve ser skill-based)

---

## ⚡ Performance

### Regras Obrigatórias

#### CSS
- Use `transform` e `opacity` para animações (GPU-accelerated)
- Evite `width`, `height`, `top`, `left` em animações
- Limite uso de `box-shadow` em elementos animados

#### JavaScript
- Use `requestAnimationFrame` para animações complexas
- Debounce/throttle em event listeners de scroll/resize
- Evite manipulação de DOM em loops intensivos

#### Assets
- Imagens: max 200KB cada
- Sons: formato .mp3 ou .ogg, max 100KB
- Lazy load para recursos não críticos

### Métricas Alvo
- **First Contentful Paint**: < 1s
- **Time to Interactive**: < 2s
- **FPS**: 60fps constante em animações
- **Lighthouse Score**: 90+ em Performance

---

## 🧪 Testes e Qualidade

### Antes de Commit
- [ ] Testar em Chrome, Firefox, Edge
- [ ] Testar em mobile (responsive design)
- [ ] Verificar console (sem erros)
- [ ] Validar HTML (W3C validator)
- [ ] Rodar linter (pylint para Python)

### Testes Manuais Obrigatórios
1. Iniciar jogo em cada dificuldade
2. Clicar rapidamente em múltiplas toupeiras
3. Deixar tempo acabar naturalmente
4. Reiniciar jogo 3x consecutivas
5. Redimensionar janela durante jogo

### Coverage Desejado (quando implementar testes)
- Backend: 80%+ coverage
- Frontend: 70%+ coverage
- Critical paths: 100% coverage

---

## 📝 Documentação

### Comentários no Código

#### Python
```python
def funcao_complexa(param):
    """
    Descrição breve.
    
    Args:
        param (tipo): Descrição do parâmetro
        
    Returns:
        tipo: Descrição do retorno
        
    Raises:
        Exception: Quando ocorre X
    """
```

#### JavaScript
```javascript
/**
 * Descrição da função
 * @param {string} param - Descrição
 * @returns {Object} { score: number, time: number }
 */
```

#### CSS
```css
/* ======================
   SEÇÃO: Nome da Seção
   ====================== */

/* Subseção específica */
.classe {
    /* Comentário explicando decisão não óbvia */
}
```

### README Updates
Ao adicionar feature significativa:
1. Atualizar seção de Features
2. Adicionar em Roadmap (marcar como completo)
3. Atualizar screenshots se aplicável
4. Documentar breaking changes

---

## 🐛 Debugging e Troubleshooting

### Logging
Use logging estruturado:
```python
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

logger.info(f"Ação realizada: {detalhes}")
logger.error(f"Erro em <função>: {erro}")
```

### Console Messages
Mantenha console limpo em produção:
```javascript
const DEBUG = false; // ou process.env.NODE_ENV === 'development'

if (DEBUG) {
    console.log('Debug info:', data);
}
```

---

## 🔒 Segurança

### Input Validation
Sempre valide entrada do usuário:
```python
@app.route('/api/score', methods=['POST'])
def save_score():
    data = request.get_json()
    
    # Validação
    if not data or 'score' not in data:
        return jsonify({'error': 'Invalid input'}), 400
    
    score = data['score']
    if not isinstance(score, int) or score < 0 or score > 1000:
        return jsonify({'error': 'Invalid score'}), 400
```

### CORS
Para APIs públicas, configure corretamente:
```python
from flask_cors import CORS
CORS(app, resources={r"/api/*": {"origins": "https://dominio.com"}})
```

### Secrets
NUNCA commite:
- API keys
- Senhas
- Tokens de acesso
- Credenciais de banco de dados

Use variáveis de ambiente:
```python
import os
SECRET_KEY = os.getenv('SECRET_KEY', 'dev-key-only')
```

---

## 🚀 Deploy e Produção

### Checklist Pré-Deploy
- [ ] `DEBUG = False` em produção
- [ ] Environment variables configuradas
- [ ] Requirements.txt atualizado
- [ ] .gitignore configurado
- [ ] README atualizado
- [ ] Testes passando

### Ambientes Recomendados
- **Desenvolvimento**: Python local
- **Staging**: Heroku/Render (grátis)
- **Produção**: Heroku/AWS/Azure

### Configuração de Produção
```python
if os.getenv('FLASK_ENV') == 'production':
    app.config['DEBUG'] = False
    app.config['TESTING'] = False
else:
    app.config['DEBUG'] = True
```

---

## 🎯 Prioridades do Projeto

### Ordem de Importância
1. **Gameplay Fluido** - Sem bugs que quebrem a experiência
2. **Visual Cyberpunk** - Manter coerência estética
3. **Performance** - 60fps em animações
4. **Responsividade** - Mobile-friendly
5. **Features Extras** - Som, leaderboard, etc.

### Issues Prioritárias
- 🔥 **Critical**: Bugs que quebram o jogo
- ⚡ **High**: Features do roadmap v1.1
- 📌 **Medium**: Melhorias visuais
- 💤 **Low**: Nice-to-have

---

## 🤝 Contribuição e Colaboração

### Padrão de Commits
```
tipo(escopo): descrição breve

Descrição detalhada opcional

Fixes #123
```

**Tipos:**
- `feat`: Nova feature
- `fix`: Bug fix
- `docs`: Documentação
- `style`: Formatação
- `refactor`: Refatoração
- `test`: Testes
- `chore`: Manutenção

**Exemplo:**
```
feat(gameplay): adiciona toupeiras especiais com comportamento único

Implementa 4 tipos de toupeiras:
- Turbo (3 pontos, rápida)
- Bônus (5 pontos, lenta)
- Fantasma (4 pontos, transparente)
- Bomba (-5 pontos, penalidade)

Closes #4
```

---

## 💡 Sugestões Específicas do Copilot

### Ao Gerar Código
- Sempre incluir comentários explicativos
- Sugerir otimizações quando relevante
- Mencionar trade-offs de decisões técnicas
- Incluir exemplos de uso quando apropriado

### Ao Revisar Código
- Verificar aderência ao tema cyberpunk
- Validar se cores neon estão corretas
- Checar performance de animações
- Confirmar responsividade

### Ao Sugerir Features
- Manter coerência com roadmap existente
- Priorizar features que aumentem imersão
- Considerar impacto em performance
- Sugerir implementação incremental

---

## 🎨 Recursos e Referências

### Inspiração Visual
- **Jogos**: Cyberpunk 2077, Ghostrunner, Tron
- **Filmes**: Blade Runner 2049, Akira, Ghost in the Shell
- **Arte**: Beeple, James White, Simon Stålenhag

### Ferramentas Recomendadas
- **Design**: Figma, Adobe XD
- **Cores**: Coolors.co, Color Hunt
- **Animações**: LottieFiles, Animate.css
- **Sounds**: Freesound.org, Zapsplat

---

## 📊 Métricas de Sucesso

### KPIs do Projeto
- ⭐ GitHub Stars: Meta 100+
- 🍴 Forks: Meta 50+
- 📈 Uptime: 99.9%
- 🚀 Lighthouse Score: 90+
- 🎮 Engagement: Tempo médio de jogo 5+ minutos

---

**Última Atualização:** 02/02/2026  
**Versão:** 1.0.0  
**Mantenedor:** Cyber Mole Team 🤖⚡
