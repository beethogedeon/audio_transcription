import whisper
import os
import torch
import subprocess


DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

model = whisper.load_model("base", device=DEVICE)


def transcribe(audio: str) -> str:
    result = model.transcribe(audio)
    return result["text"]
