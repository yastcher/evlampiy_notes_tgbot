import logging
from io import BytesIO

import wit
from pydub import AudioSegment
from telegram import Update
from telegram.ext import ContextTypes

from src.bot import send_response
from src.config import settings

logger = logging.getLogger(__name__)


async def from_voice_to_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Translate voice message to text by processing it in 20 second chunks.
    """
    if update.message.voice:
        voice_file = await update.message.voice.get_file()
        file_data = await voice_file.download_as_bytearray()
        audio_stream = BytesIO(file_data)
        audio = AudioSegment.from_file(audio_stream, format="ogg")

        chunk_length_ms = 19500  # < 20 sec
        chunks = [
            audio[i:i + chunk_length_ms]
            for i in range(0, len(audio), chunk_length_ms)
        ]

        full_translated_text = ""
        for i, chunk in enumerate(chunks):
            converted_stream = BytesIO()
            chunk.export(converted_stream, format="mp3")
            converted_stream.seek(0)
            response = voice_translator.speech(
                audio_file=converted_stream,
                headers={"Content-Type": "audio/mpeg3"}
            )
            text = response["text"] if "text" in response else "\n"
            full_translated_text += text + "\n"

        if full_translated_text.lower().startswith(settings.telegram_bot_command):
            await send_response(
                update,
                context,
                response=f"Command {settings.telegram_bot_command} detected in the voice message."
                         f"\nAsk GPT for: {full_translated_text[len(settings.telegram_bot_command):]}",
            )
            return

        await send_response(
            update,
            context,
            response=full_translated_text,
            reply_to_message_id=update.message.message_id,
        )


voice_translator = wit.Wit(settings.wit_ru_token)
