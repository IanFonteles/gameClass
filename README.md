# 🔨 Whack-a-Mole - Jogo em Python

Um jogo Whack-a-Mole funcional e bem estilizado desenvolvido em Python com Flask, HTML5, CSS3 e JavaScript.

## Características

✨ **Funcionalidades:**
- Jogabilidade fluida e responsiva
- 4 níveis de dificuldade (Fácil, Normal, Difícil, Expert)
- Sistema de pontuação em tempo real
- Moles com animações suaves
- Design moderno e responsivo
- Contador de tempo regressivo
- Interface intuitiva e divertida

🎮 **Níveis de Dificuldade:**
- **Fácil**: 40 segundos, velocidade moderada
- **Normal**: 30 segundos, velocidade normal (padrão)
- **Difícil**: 20 segundos, moles aparecem rápido
- **Expert**: 15 segundos, desafio máximo!

## Instalação

### Pré-requisitos
- Python 3.7+ instalado

### Passos

1. **Clone ou acesse a pasta do projeto:**
   ```bash
   cd c:\Workspaces\gameClass
   ```

2. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

## Executar o Jogo

1. **Inicie o servidor:**
   ```bash
   python app.py
   ```

2. **Abra o navegador e acesse:**
   ```
   http://localhost:5000
   ```

3. **Pronto!** O jogo está pronto para jogar! 🎮

## Como Jogar

1. Selecione o nível de dificuldade desejado
2. Clique no botão "Começar Jogo"
3. Clique nos moles rosa que aparecem nas tocas
4. Quanto mais moles acertar, maior sua pontuação!
5. O jogo termina quando o tempo acaba
6. Clique em "Jogar Novamente" para uma nova rodada

## Tecnologias Utilizadas

- **Backend**: Python + Flask
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **Animações**: CSS Keyframes
- **Responsividade**: CSS Grid e Flexbox

## Estrutura do Projeto

```
gameClass/
├── app.py              # Aplicação principal (Python/Flask)
├── requirements.txt    # Dependências do projeto
└── README.md          # Este arquivo
```

## Customizações Possíveis

Você pode facilmente personalizar:

### Cores
- Edite o CSS no arquivo `app.py` (seção `<style>`)
- Modifique os gradientes e cores hexadecimais

### Velocidade dos Moles
- Procure por `gameState.moleShowTime` no JavaScript
- Reduza o valor para moles aparecerem mais rápido

### Quantidade de Tocas
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
