import wit

from src.config import settings


def transcribe_audio(audio_file):
    with open(audio_file, "rb") as f:
        response = client.speech(f, headers={"Content-Type": "audio/wav"})
    return response


client = wit.Wit(settings.wit_ru_token)
