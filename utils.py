import whisper
import torch

DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

model = whisper.load_model("base", device=DEVICE)


def transcribe(audio: str) -> str:
    result = model.transcribe(audio, fp16=False)
    return result["text"]
