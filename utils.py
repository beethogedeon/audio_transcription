import whisper

model = whisper.load_model("medium")


def transcribe(audio: str) -> str:
    result = model.transcribe(audio)
    return result["text"]
