from google.cloud import speech

def transcribe_audio(audio_file: bytes) -> str:
    """Расшифровывает голосовой ввод в текст"""
    client = speech.SpeechClient()
    audio = speech.RecognitionAudio(content=audio_file)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        language_code="ru-RU"
    )
    response = client.recognize(config=config, audio=audio)
    return response.results[0].alternatives if[0].transcript
















