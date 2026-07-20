from crewai import LLM
# from config import MODEL, BASE_URL
from src.config import MODEL, BASE_URL

llm = LLM(
    model=f"ollama/{MODEL}",
    base_url=BASE_URL,
)