import os
from openai import OpenAI

client = OpenAI()
# openai.api_key = os.getenv("OPENAI_API_KEY")


def transcribe(audio: str) -> str:
    audio_file = open(audio, "rb")
    transcript = client.audio.transcriptions.create(
        model="whisper-1", 
        file=audio_file,
        response_format="text"
    )
    return transcript
