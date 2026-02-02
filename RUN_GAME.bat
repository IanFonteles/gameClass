@echo off
echo.
echo ========================================
echo   WHACK-A-MOLE - Jogo em Python
echo ========================================
echo.

REM Verificar se Python está instalado
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERRO] Python não foi encontrado!
    echo Instale Python de https://www.python.org
    pause
    exit /b 1
)

echo [OK] Python encontrado!
echo.
echo [1/3] Instalando dependências...
pip install -r requirements.txt >nul 2>&1

if errorlevel 1 (
    echo [ERRO] Falha ao instalar dependências
    pause
    exit /b 1
)

echo [OK] Dependências instaladas!
echo.
echo ========================================
echo   Iniciando servidor...
echo ========================================
echo.
echo   Acesse: http://localhost:5000
echo   Pressione Ctrl+C para parar
echo.
echo ========================================
echo.

python app.py
pause
