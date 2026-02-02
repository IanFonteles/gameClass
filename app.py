from flask import Flask, render_template_string, jsonify, request
import json

app = Flask(__name__)

# Armazena dados da sessão do jogo
game_scores = {}

# Template HTML inline
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Whack-a-Mole - Jogo</title>
  <style>
    * {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
    }

    body {
      font-family: 'Courier New', 'Consolas', monospace;
      background: linear-gradient(135deg, #0a0e27 0%, #1a1a2e 50%, #16213e 100%);
      background-attachment: fixed;
      min-height: 100vh;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 20px;
      position: relative;
      overflow: hidden;
    }

    body::before {
      content: '';
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      background: repeating-linear-gradient(
        0deg,
        rgba(0, 255, 255, 0.03),
        rgba(0, 255, 255, 0.03) 1px,
        transparent 1px,
        transparent 2px
      );
      pointer-events: none;
      animation: scanlines 8s linear infinite;
      z-index: 1;
    }

    @keyframes scanlines {
      0% {
        transform: translateY(0);
      }
      100% {
        transform: translateY(10px);
      }
    }

    .container {
      width: 100%;
      max-width: 900px;
      background: linear-gradient(135deg, rgba(10, 25, 47, 0.95) 0%, rgba(26, 26, 46, 0.95) 100%);
      border-radius: 0px;
      border: 3px solid #00ffff;
      box-shadow: 0 0 40px rgba(0, 255, 255, 0.5), 
                  inset 0 0 40px rgba(255, 0, 255, 0.1),
                  0 0 20px rgba(255, 0, 200, 0.3);
      padding: 40px;
      text-align: center;
      position: relative;
      z-index: 2;
    }

    .container::before {
      content: '';
      position: absolute;
      top: -3px;
      left: -3px;
      right: -3px;
      bottom: -3px;
      background: linear-gradient(45deg, #00ffff, #ff00ff, #00ffff);
      border-radius: 0px;
      z-index: -1;
      opacity: 0;
      animation: neonBorder 3s ease-in-out infinite;
    }

    @keyframes neonBorder {
      0%, 100% { opacity: 0; }
      50% { opacity: 0.3; }
    }

    h1 {
      color: #00ffff;
      margin-bottom: 10px;
      font-size: 2.8em;
      text-shadow: 0 0 10px #00ffff, 0 0 20px #00ffff, 0 0 30px #ff00ff;
      letter-spacing: 3px;
      font-weight: bold;
      animation: glitch 3s ease-in-out infinite;
    }

    @keyframes glitch {
      0%, 100% {
        text-shadow: 0 0 10px #00ffff, 0 0 20px #00ffff, 0 0 30px #ff00ff;
      }
      50% {
        text-shadow: 0 0 20px #00ffff, 0 0 30px #ff00ff, 0 0 40px #00ff00;
      }
    }

    .subtitle {
      color: #00ff00;
      margin-bottom: 30px;
      font-size: 1.1em;
      text-shadow: 0 0 10px #00ff00;
      letter-spacing: 1px;
    }

    .stats {
      display: flex;
      justify-content: space-around;
      margin-bottom: 30px;
      flex-wrap: wrap;
      gap: 20px;
    }

    .stat-box {
      background: linear-gradient(135deg, rgba(0, 255, 255, 0.1) 0%, rgba(255, 0, 200, 0.1) 100%);
      color: #00ffff;
      padding: 20px 40px;
      border-radius: 0px;
      min-width: 150px;
      border: 2px solid #ff00ff;
      box-shadow: 0 0 20px rgba(0, 255, 255, 0.5), inset 0 0 20px rgba(255, 0, 200, 0.2);
      position: relative;
      overflow: hidden;
    }

    .stat-box::before {
      content: '';
      position: absolute;
      top: -50%;
      left: -50%;
      width: 200%;
      height: 200%;
      background: linear-gradient(45deg, transparent 30%, rgba(0, 255, 255, 0.1) 50%, transparent 70%);
      animation: shine 3s infinite;
    }

    @keyframes shine {
      0% {
        transform: translateX(-100%) translateY(-100%) rotate(45deg);
      }
      100% {
        transform: translateX(100%) translateY(100%) rotate(45deg);
      }
    }

    .stat-label {
      font-size: 0.9em;
      opacity: 0.8;
      margin-bottom: 5px;
      color: #00ff00;
      text-transform: uppercase;
      letter-spacing: 1px;
    }

    .stat-value {
      font-size: 2.5em;
      font-weight: bold;
      color: #00ffff;
      text-shadow: 0 0 10px #00ffff;
    }

    .game-board {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(100px, 1fr));
      gap: 15px;
      margin-bottom: 30px;
      max-width: 500px;
      margin-left: auto;
      margin-right: auto;
    }

    .mole-hole {
      width: 100px;
      height: 100px;
      border-radius: 0px;
      background: linear-gradient(135deg, #1a1a2e 0%, #0a0e27 100%);
      border: 3px solid #ff00ff;
      cursor: pointer;
      position: relative;
      overflow: hidden;
      transition: all 0.2s;
      box-shadow: 0 0 15px rgba(255, 0, 200, 0.5), inset 0 0 15px rgba(0, 255, 255, 0.2);
    }

    .mole-hole:hover {
      transform: scale(1.1);
      border-color: #00ffff;
      box-shadow: 0 0 25px rgba(0, 255, 255, 0.8), inset 0 0 25px rgba(0, 255, 255, 0.3);
    }

    .mole-hole.active {
      animation: cyberPulse 0.3s ease;
    }

    @keyframes cyberPulse {
      0% {
        transform: scale(1) rotateX(0deg);
        box-shadow: 0 0 15px rgba(255, 0, 200, 0.5);
      }
      50% {
        transform: scale(0.95) rotateX(10deg);
        box-shadow: 0 0 25px rgba(0, 255, 255, 0.8);
      }
      100% {
        transform: scale(1) rotateX(0deg);
        box-shadow: 0 0 15px rgba(255, 0, 200, 0.5);
      }
    }

    .mole {
      width: 80px;
      height: 80px;
      background: linear-gradient(135deg, #00ffff 0%, #ff00ff 100%);
      border-radius: 50%;
      position: absolute;
      top: 10px;
      left: 10px;
      display: flex;
      align-items: center;
      justify-content: center;
      opacity: 0;
      transform: translateY(100px) scale(0) rotateZ(0deg);
      transition: all 0.3s cubic-bezier(0.68, -0.55, 0.265, 1.55);
      box-shadow: 0 0 20px #00ffff, 0 0 40px #ff00ff;
      border: 2px solid #00ff00;
    }

    .mole-hole.show .mole {
      opacity: 1;
      transform: translateY(0) scale(1) rotateZ(360deg);
    }

    .mole::before {
      content: '';
      width: 14px;
      height: 14px;
      background: #000;
      border-radius: 50%;
      position: absolute;
      top: 24px;
      left: 16px;
      box-shadow: inset 0 0 5px #00ffff;
    }

    .mole::after {
      content: '';
      width: 14px;
      height: 14px;
      background: #000;
      border-radius: 50%;
      position: absolute;
      top: 24px;
      right: 16px;
      box-shadow: inset 0 0 5px #00ffff;
    }

    .mole-smile {
      width: 24px;
      height: 12px;
      border: 2px solid #000;
      border-top: none;
      border-radius: 0 0 24px 24px;
      position: absolute;
      bottom: 12px;
      box-shadow: 0 0 5px #00ff00;
    }

    .controls {
      margin-bottom: 20px;
    }

    button {
      background: linear-gradient(135deg, #00ffff 0%, #ff00ff 100%);
      color: #000;
      border: 2px solid #00ff00;
      padding: 15px 40px;
      font-size: 1.1em;
      border-radius: 0px;
      cursor: pointer;
      margin: 10px;
      transition: all 0.3s;
      box-shadow: 0 0 20px rgba(0, 255, 255, 0.5);
      font-weight: bold;
      text-transform: uppercase;
      letter-spacing: 1px;
      font-family: 'Courier New', monospace;
    }

    button:hover {
      transform: translateY(-3px);
      box-shadow: 0 0 30px rgba(0, 255, 255, 0.8), 0 0 15px rgba(255, 0, 200, 0.6);
      text-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
    }

    button:active {
      transform: translateY(-1px);
      box-shadow: 0 0 20px rgba(255, 0, 200, 0.8);
    }

    button:disabled {
      opacity: 0.5;
      cursor: not-allowed;
      transform: none;
    }

    .game-over {
      display: none;
      position: fixed;
      top: 0;
      left: 0;
      right: 0;
      bottom: 0;
      background: rgba(0, 0, 0, 0.9);
      align-items: center;
      justify-content: center;
      z-index: 1000;
    }

    .game-over.show {
      display: flex;
    }

    .game-over-content {
      background: linear-gradient(135deg, #0a0e27 0%, #1a1a2e 100%);
      padding: 40px;
      border-radius: 0px;
      text-align: center;
      min-width: 300px;
      border: 3px solid #00ffff;
      box-shadow: 0 0 40px rgba(0, 255, 255, 0.5), 
                  0 0 20px rgba(255, 0, 200, 0.4);
      animation: slideUp 0.4s cubic-bezier(0.68, -0.55, 0.265, 1.55);
    }

    @keyframes slideUp {
      from {
        transform: translateY(30px) scale(0.9);
        opacity: 0;
      }
      to {
        transform: translateY(0) scale(1);
        opacity: 1;
      }
    }

    .game-over-content h2 {
      color: #00ffff;
      margin-bottom: 20px;
      font-size: 2.2em;
      text-shadow: 0 0 20px #00ffff;
      text-transform: uppercase;
      letter-spacing: 2px;
    }

    .game-over-content p {
      color: #00ff00;
      margin-bottom: 30px;
      font-size: 1.2em;
      text-shadow: 0 0 10px #00ff00;
    }

    .final-score {
      font-size: 4em;
      color: #ff00ff;
      font-weight: bold;
      margin-bottom: 30px;
      text-shadow: 0 0 20px #ff00ff, 0 0 40px #00ffff;
      text-transform: uppercase;
      letter-spacing: 2px;
    }

    .difficulty-selector {
      margin-bottom: 30px;
      background: rgba(0, 255, 255, 0.05);
      padding: 20px;
      border: 2px solid #ff00ff;
      border-radius: 0px;
      box-shadow: inset 0 0 15px rgba(0, 255, 255, 0.1);
    }

    .difficulty-selector label {
      margin: 0 10px;
      cursor: pointer;
      font-weight: 600;
      color: #00ff00;
      text-transform: uppercase;
      letter-spacing: 1px;
      display: inline-block;
      padding: 5px 10px;
      border-radius: 0px;
      transition: all 0.2s;
    }

    .difficulty-selector label:hover {
      color: #00ffff;
      text-shadow: 0 0 10px #00ffff;
    }

    .difficulty-selector input[type="radio"] {
      margin-right: 5px;
      cursor: pointer;
      accent-color: #00ffff;
    }

    @media (max-width: 600px) {
      .container {
        padding: 20px;
      }

      h1 {
        font-size: 1.8em;
      }

      .stats {
        gap: 10px;
      }

      .stat-box {
        padding: 15px 25px;
        min-width: 120px;
      }

      .game-board {
        gap: 10px;
      }

      .mole-hole {
        width: 80px;
        height: 80px;
      }

      .mole {
        width: 65px;
        height: 65px;
        top: 7px;
        left: 7px;
      }
    }
  </style>
</head>
<body>
  <div class="container">
    <h1>⚡ CYBER MOLE ⚡</h1>
    <p class="subtitle">Elimine as toupeiras robóticas antes que escapem!</p>
    
    <div class="stats">
      <div class="stat-box">
        <div class="stat-label">⚡ PONTOS CYBER ⚡</div>
        <div class="stat-value" id="score">0</div>
      </div>
      <div class="stat-box">
        <div class="stat-label">⏱ TEMPO RESTANTE</div>
        <div class="stat-value" id="timeLeft">30</div>
      </div>
    </div>

    <div class="difficulty-selector">
      <label>
        <input type="radio" name="difficulty" value="easy" id="easy"> LEVE (40s)
      </label>
      <label>
        <input type="radio" name="difficulty" value="normal" id="normal" checked> NORMAL (30s)
      </label>
      <label>
        <input type="radio" name="difficulty" value="hard" id="hard"> EXTREMO (20s)
      </label>
      <label>
        <input type="radio" name="difficulty" value="expert" id="expert"> INSANO (15s)
      </label>
    </div>

    <div class="game-board" id="gameBoard"></div>

    <div class="controls">
      <button id="startBtn">► INICIAR JOGO ◄</button>
    </div>
  </div>

  <div class="game-over" id="gameOver">
    <div class="game-over-content">
      <h2>⚡ MISSÃO FINALIZADA ⚡</h2>
      <p>Toupeiras Eliminadas:</p>
      <div class="final-score" id="finalScore">0</div>
      <p>UNIDADES DESTRUÍDAS</p>
      <button id="restartBtn">► REINICIAR JOGO ◄</button>
    </div>
  </div>

  <script>
    const gameState = {
      isRunning: false,
      score: 0,
      timeLeft: 30,
      difficulty: 'normal',
      moleShowTime: 600,
      gameInterval: null,
      moleIntervals: []
    };

    const elements = {
      score: document.getElementById('score'),
      timeLeft: document.getElementById('timeLeft'),
      startBtn: document.getElementById('startBtn'),
      gameBoard: document.getElementById('gameBoard'),
      gameOver: document.getElementById('gameOver'),
      finalScore: document.getElementById('finalScore'),
      restartBtn: document.getElementById('restartBtn'),
      difficultyRadios: document.querySelectorAll('input[name="difficulty"]')
    };

    function initializeGame() {
      gameState.isRunning = false;
      gameState.score = 0;
      gameState.timeLeft = 30;
      gameState.moleShowTime = 600;
      
      elements.score.textContent = '0';
      elements.timeLeft.textContent = '30';
      elements.gameOver.classList.remove('show');
      
      document.querySelectorAll('.mole-hole').forEach(hole => {
        hole.classList.remove('show');
      });
      
      clearAllIntervals();
    }

    function clearAllIntervals() {
      if (gameState.gameInterval) clearInterval(gameState.gameInterval);
      gameState.moleIntervals.forEach(interval => clearInterval(interval));
      gameState.moleIntervals = [];
    }

    function startGame() {
      const difficulty = document.querySelector('input[name="difficulty"]:checked').value;
      gameState.difficulty = difficulty;
      
      switch(difficulty) {
        case 'easy':
          gameState.moleShowTime = 1000;
          gameState.timeLeft = 40;
          break;
        case 'normal':
          gameState.moleShowTime = 600;
          gameState.timeLeft = 30;
          break;
        case 'hard':
          gameState.moleShowTime = 400;
          gameState.timeLeft = 20;
          break;
        case 'expert':
          gameState.moleShowTime = 300;
          gameState.timeLeft = 15;
          break;
      }

      gameState.score = 0;
      gameState.isRunning = true;
      
      elements.score.textContent = '0';
      elements.timeLeft.textContent = gameState.timeLeft;
      elements.startBtn.disabled = true;
      elements.difficultyRadios.forEach(radio => radio.disabled = true);
      
      gameState.gameInterval = setInterval(updateTimer, 1000);
      showRandomMole();
    }

    function updateTimer() {
      gameState.timeLeft--;
      elements.timeLeft.textContent = gameState.timeLeft;
      
      if (gameState.timeLeft <= 0) {
        endGame();
      }
    }

    function showRandomMole() {
      if (!gameState.isRunning) return;
      
      const holes = document.querySelectorAll('.mole-hole');
      const randomHole = holes[Math.floor(Math.random() * holes.length)];
      
      randomHole.classList.add('show');
      
      const timeoutId = setTimeout(() => {
        randomHole.classList.remove('show');
        if (gameState.isRunning) {
          setTimeout(showRandomMole, Math.random() * 300 + 100);
        }
      }, gameState.moleShowTime);
      
      gameState.moleIntervals.push(timeoutId);
    }

    function whackMole(e) {
      if (!gameState.isRunning) return;
      
      const hole = e.currentTarget;
      if (!hole.classList.contains('show')) return;
      
      hole.classList.add('active');
      hole.classList.remove('show');
      gameState.score++;
      elements.score.textContent = gameState.score;
      
      setTimeout(() => {
        hole.classList.remove('active');
      }, 100);
    }

    function endGame() {
      gameState.isRunning = false;
      clearAllIntervals();
      
      elements.startBtn.disabled = false;
      elements.difficultyRadios.forEach(radio => radio.disabled = false);
      elements.startBtn.textContent = '► REINICIAR JOGO ◄';
      
      document.querySelectorAll('.mole-hole').forEach(hole => {
        hole.classList.remove('show');
      });
      
      elements.finalScore.textContent = gameState.score;
      elements.gameOver.classList.add('show');
    }

    function setupMoleHoles() {
      const numHoles = 9;
      elements.gameBoard.innerHTML = '';
      
      for (let i = 0; i < numHoles; i++) {
        const hole = document.createElement('div');
        hole.className = 'mole-hole';
        hole.addEventListener('click', whackMole);
        
        const mole = document.createElement('div');
        mole.className = 'mole';
        mole.innerHTML = '<div class="mole-smile"></div>';
        
        hole.appendChild(mole);
        elements.gameBoard.appendChild(hole);
      }
    }

    elements.startBtn.addEventListener('click', startGame);
    elements.restartBtn.addEventListener('click', () => {
      initializeGame();
      startGame();
    });

    setupMoleHoles();
    initializeGame();
  </script>
</body>
</html>
'''

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE)

@app.route('/api/score', methods=['POST'])
def save_score():
    data = request.get_json()
    session_id = data.get('session_id')
    score = data.get('score', 0)
    
    if session_id:
        game_scores[session_id] = score
    
    return jsonify({'success': True, 'message': 'Score salvo'})

@app.route('/api/score/<session_id>', methods=['GET'])
def get_score(session_id):
    score = game_scores.get(session_id, 0)
    return jsonify({'score': score})

if __name__ == '__main__':
    print("=" * 60)
    print("🔨 WHACK-A-MOLE - Jogo em Python com Flask 🔨")
    print("=" * 60)
    print("\n✅ Servidor iniciando...")
    print("📱 Abra seu navegador e acesse: http://localhost:5000")
    print("🎮 Pressione Ctrl+C para parar o servidor\n")
    print("=" * 60)
    
    app.run(debug=True, port=5000, use_reloader=False)
