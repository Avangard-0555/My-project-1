from fastapi import FastAPI, HTTPException
from services import ask_openai, transcribe_audio
from db import init_db, save_question
import uvicorn

app = FastAPI()

# Инициализация базы данных
init_db()

@app.get("/")
def home():
    return {"message": "Голосовой помощник для программистов"}

@app.post("/ask")
def ask_question(question: str):
    """Получает текстовый вопрос и возвращает ответ от AI"""
    try:
        answer = ask_openai(question)
        save_question(question, answer)
        return {"question": question, "answer": answer}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/voice")
def voice_command(audio_file: bytes):
    """Обрабатывает голосовой ввод и возвращает ответ"""
    try:
        text = transcribe_audio(audio_file)
        answer = ask_openai(text)
        save_question(text, answer)
        return {"question": text, "answer": answer}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)















