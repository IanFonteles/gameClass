# Usar imagem oficial Python slim
FROM python:3.11-slim

# Metadados
LABEL maintainer="Cyber Mole Team"
LABEL description="Jogo Whack-a-Mole futurista com tema cyberpunk"
LABEL version="1.0.0"

# Diretório de trabalho
WORKDIR /app

# Copiar requirements primeiro (cache layer)
COPY requirements.txt .

# Instalar dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copiar código da aplicação
COPY app.py .

# Expor porta
EXPOSE 5000

# Variáveis de ambiente
ENV FLASK_APP=app.py
ENV FLASK_ENV=production
ENV PYTHONUNBUFFERED=1

# Health check
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
  CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:5000')"

# Comando para iniciar
CMD ["python", "app.py"]
