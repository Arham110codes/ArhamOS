from openai import OpenAI
from .config import settings


class LLMClient:
    def __init__(self):
        self.client = OpenAI(
            base_url=settings.OLLAMA_BASE_URL,
            api_key=settings.OLLAMA_API_KEY,
        )

    def ask(self, prompt: str) -> str:
        response = self.client.chat.completions.create(
            model=settings.OLLAMA_MODEL,
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
        )

        return response.choices[0].message.content