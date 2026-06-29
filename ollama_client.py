import httpx

from config import OLLAMA_HOST, OLLAMA_MODEL


def generate(prompt: str, *, model: str | None = None) -> str:
    """POST a prompt to Ollama and return the response text.

    Raises httpx.HTTPError on non-2xx responses,
    httpx.ConnectError if Ollama is not reachable.
    """
    response = httpx.post(
        f"{OLLAMA_HOST}/api/generate",
        json={"model": model or OLLAMA_MODEL, "prompt": prompt, "stream": False},
        timeout=120.0,
    )
    response.raise_for_status()
    return response.json()["response"]


if __name__ == "__main__":
    print(f"Pinging Ollama at {OLLAMA_HOST} with model {OLLAMA_MODEL} ...")
    text = generate("Reply with exactly three words: OLLAMA IS READY")
    print(f"Response: {text.strip()}")
