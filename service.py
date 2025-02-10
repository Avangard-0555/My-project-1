import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def ask_openai(question: str) -> str:
    """Отправляет вопрос в OpenAI API и получает ответ"""
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": question}]
    )
    return response["choices"][0]["message"]["content"]





