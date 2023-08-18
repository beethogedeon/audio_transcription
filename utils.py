import whisper

model = whisper.load_model("base")


def transcribe(audio: str) -> str:
    result = model.transcribe(audio)
    return result["text"]
