import whisper

model = whisper.load_model("large-v2")


def transcribe(audio: str) -> str:
    result = model.transcribe(audio)
    return result["text"]
