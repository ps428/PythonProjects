from pathlib import Path
from openai import OpenAI
from .main import VoiceRequest
from datetime import datetime


def get_client():
    client = OpenAI()


async def tts(request: VoiceRequest):
    client = get_client()

    speech_file_path = Path(__file__).parent / f"{datetime.now()}speech.mp3"
    response = client.audio.speech.create(
        model="tts-1",
        voice="alloy",
        input="Today is a wonderful day to build something people love!",
    )

    response.stream_to_file(speech_file_path)
