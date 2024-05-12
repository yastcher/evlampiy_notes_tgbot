from io import BytesIO

import wit
from pydub import AudioSegment
from telegram import Update
from telegram.ext import ContextTypes

from src.bot import send_response
from src.config import settings


async def from_voice_to_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    translate voice message to text
    """
    if update.message.voice:
        voice_file = await update.message.voice.get_file()
        file_data = await voice_file.download_as_bytearray()
        audio_stream = BytesIO(file_data)
        audio = AudioSegment.from_file(audio_stream, format="ogg")
        converted_stream = BytesIO()
        audio.export(converted_stream, format="wav")
        converted_stream.seek(0)
        response = client.speech(converted_stream, headers={"Content-Type": "audio/wav"})
        translated_text = response["text"] if "text" in response else "Could not transcribe the audio."
        await send_response(
            update,
            context,
            response=translated_text,
            reply_to_message_id=update.message.message_id,
        )


client = wit.Wit(settings.wit_ru_token)
