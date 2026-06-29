FROM python:3.11-slim

WORKDIR /app

# Install dependencies first — layer is cached unless requirements.txt changes
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source (venv, .env, and *.db are excluded by .dockerignore)
COPY *.py ./
COPY tests/ ./tests/

# Ollama runs on the host; host.docker.internal resolves on Docker Desktop
# Override with -e OLLAMA_HOST=... if your setup differs
ENV OLLAMA_HOST=http://host.docker.internal:11434
ENV OLLAMA_MODEL=mistral
ENV DB_PATH=/data/study.db

# Mount a named volume here to persist the database across container restarts
VOLUME ["/data"]

EXPOSE 8000

# Default: run the API server
# For the CLI instead: docker run -it --rm -v csa-data:/data csa-study-engine python cli.py
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]
