---
name: Melhorar Visual da Toupeira
about: Tornar a toupeira mais realista e parecida com uma toupeira de verdade
title: '🎨 Melhorar visual da toupeira para parecer mais realista'
labels: 'enhancement, priority-medium, area-ui-ux, difficulty-medium'
assignees: ''
---

## 🎯 Objetivo

Redesenhar a toupeira robótica para que tenha características visuais mais próximas de uma toupeira real, mantendo o tema cyberpunk futurista.

## 🔍 Problema Atual

A toupeira atual é representada por:
- Círculo com gradient cyan-magenta
- Olhos simples (círculos pretos)
- Sorriso básico
- **Falta características distintivas de uma toupeira**

## 💡 Solução Proposta

### Características de Toupeira para Adicionar:

#### 1. **Focinho Proeminente**
```css
.mole-snout {
  position: absolute;
  bottom: 20%;
  left: 50%;
  transform: translateX(-50%);
  width: 25px;
  height: 15px;
  background: linear-gradient(180deg, #ff00ff 0%, #00ffff 100%);
  border-radius: 50% 50% 40% 40%;
  border: 1px solid #00ff00;
}
```

#### 2. **Nariz Rosa Neon**
```css
.mole-nose {
  width: 8px;
  height: 8px;
  background: #ff1493;
  border-radius: 50%;
  box-shadow: 0 0 10px #ff1493;
  position: absolute;
  bottom: 5px;
  left: 50%;
  transform: translateX(-50%);
}
```

#### 3. **Bigodes Cyber**
```css
.mole-whisker {
  position: absolute;
  height: 1px;
  background: linear-gradient(90deg, transparent, #00ffff, transparent);
  box-shadow: 0 0 3px #00ffff;
}

.mole-whisker-left-1 { width: 30px; left: -30px; top: 45%; }
.mole-whisker-left-2 { width: 25px; left: -25px; top: 55%; }
.mole-whisker-right-1 { width: 30px; right: -30px; top: 45%; }
.mole-whisker-right-2 { width: 25px; right: -25px; top: 55%; }
```

#### 4. **Orelhas Pequenas e Arredondadas**
```css
.mole-ear {
  position: absolute;
  width: 15px;
  height: 20px;
  background: linear-gradient(135deg, #00ffff 0%, #ff00ff 100%);
  border-radius: 50% 50% 0 0;
  border: 1px solid #00ff00;
  top: 10%;
}

.mole-ear-left { left: 10%; transform: rotate(-15deg); }
.mole-ear-right { right: 10%; transform: rotate(15deg); }
```

#### 5. **Patas Dianteiras**
```css
.mole-paw {
  position: absolute;
  width: 20px;
  height: 15px;
  background: linear-gradient(135deg, #00ffff 0%, #ff00ff 100%);
  border-radius: 50% 50% 40% 40%;
  border: 1px solid #00ff00;
  bottom: -5px;
}

.mole-paw-left { left: 15%; transform: rotate(-20deg); }
.mole-paw-right { right: 15%; transform: rotate(20deg); }
```

#### 6. **Textura de Pelagem (opcional)**
```css
.mole::before {
  content: '';
  position: absolute;
  inset: 0;
  border-radius: 50%;
  background: 
    radial-gradient(circle at 30% 30%, rgba(0,255,255,0.1) 0%, transparent 50%),
    radial-gradient(circle at 70% 40%, rgba(255,0,255,0.1) 0%, transparent 50%),
    radial-gradient(circle at 50% 70%, rgba(0,255,0,0.1) 0%, transparent 50%);
}
```

## 🖼️ Referências Visuais

### Características Reais de Toupeira:
- ✅ Focinho alongado e pontudo
- ✅ Nariz rosa/vermelho proeminente
- ✅ Bigodes longos e finos
- ✅ Orelhas pequenas e arredondadas
- ✅ Patas dianteiras grandes (para cavar)
- ✅ Olhos pequenos
- ✅ Corpo arredondado e peludo

### Manter Tema Cyberpunk:
- 💎 Gradient neon (cyan/magenta/lime)
- 💎 Bordas brilhantes
- 💎 Glow effects
- 💎 Elementos robóticos/futuristas

## 📋 Tarefas

- [ ] Adicionar focinho proeminente
- [ ] Adicionar nariz rosa neon
- [ ] Adicionar bigodes cyber (6 linhas)
- [ ] Adicionar orelhas pequenas
- [ ] Adicionar patas dianteiras
- [ ] Adicionar textura de pelagem (opcional)
- [ ] Ajustar proporções dos olhos (menores)
- [ ] Testar em diferentes resoluções
- [ ] Verificar performance das animações

## 🎨 Mockup HTML

```html
<div class="mole show">
    <!-- Orelhas -->
    <div class="mole-ear mole-ear-left"></div>
    <div class="mole-ear mole-ear-right"></div>
    
    <!-- Corpo (existente) -->
    
    <!-- Olhos (reduzir tamanho) -->
    <div class="mole-eye mole-eye-left"></div>
    <div class="mole-eye mole-eye-right"></div>
    
    <!-- Focinho -->
    <div class="mole-snout">
        <div class="mole-nose"></div>
    </div>
    
    <!-- Bigodes -->
    <div class="mole-whisker mole-whisker-left-1"></div>
    <div class="mole-whisker mole-whisker-left-2"></div>
    <div class="mole-whisker mole-whisker-right-1"></div>
    <div class="mole-whisker mole-whisker-right-2"></div>
    
    <!-- Patas -->
    <div class="mole-paw mole-paw-left"></div>
    <div class="mole-paw mole-paw-right"></div>
    
    <!-- Sorriso (manter ou remover) -->
    <div class="mole-smile"></div>
</div>
```

## ✅ Critérios de Aceitação

- ✅ Toupeira possui características reconhecíveis:
  - Focinho alongado
  - Nariz rosa/neon visível
  - Bigodes de ambos os lados
  - Orelhas pequenas
  - Patas dianteiras
- ✅ Mantém tema cyberpunk (neon colors, glow)
- ✅ Animações funcionam corretamente
- ✅ Performance não é afetada
- ✅ Responsivo em mobile e desktop
- ✅ Visual é coerente com o resto do jogo

## 🎯 Versões Alternativas

### Opção A: Realista Cyber
Mais próximo de toupeira real, com detalhes robóticos

### Opção B: Cartoon Futurista  
Estilo mais cartoon mas com elementos neon e tecnológicos

### Opção C: Minimalista Cyber
Silhueta simplificada com características essenciais destacadas

## 📊 Prioridade

**Média** - Melhoria estética que aumenta a identidade visual do jogo

## 🔗 Issues Relacionadas

- #3 - Efeitos de Partículas (coordenar cores)
- #4 - Toupeiras Especiais (usar base melhorada)
- #6 - Skins Customizáveis (considerar variações)

## 💬 Notas Adicionais

- Considerar criar variações de "expressão" para diferentes estados (normal, surpresa, acertada)
- Possibilidade de animação dos bigodes (vibração sutil)
- Testar feedback de usuários sobre qual versão preferem

---

**Labels:** `enhancement`, `priority-medium`, `area-ui-ux`, `difficulty-medium`  
**Milestone:** v1.2 - Conteúdo  
**Estimate:** 3-4 horas
