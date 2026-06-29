import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

OLLAMA_HOST: str = os.getenv("OLLAMA_HOST", "http://localhost:11434")
OLLAMA_MODEL: str = os.getenv("OLLAMA_MODEL", "mistral")
DB_PATH: Path = Path(os.getenv("DB_PATH", "./study.db"))
