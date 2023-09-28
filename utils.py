import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")


def transcribe(audio: str) -> str:
    audio_file = open(audio, "rb")
    transcript = openai.Audio.transcribe("whisper-1", audio_file, response_format="text")
    return transcript
