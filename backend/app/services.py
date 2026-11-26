from dotenv import load_dotenv
from openai import OpenAI
from .models import Query
from functools import lru_cache
from fastapi import Depends


load_dotenv()

class AIService:
    def __init__(self, client: OpenAI):
        self.client = client
    
    def answer(self, body: Query) -> dict:
        response = self.client.responses.create(
            model="gpt-6.2-astra",
            reasoning={"effort": "low"},
            input=[{"role": "user", "content": body.query}]
        )
        return {"answer": response.output_text}


@lru_cache
def get_openai_client() -> OpenAI:
    return OpenAI()

def get_ai_service(client: OpenAI = Depends(get_openai_client)) -> AIService:
    return AIService(client)