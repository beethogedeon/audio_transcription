import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

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
