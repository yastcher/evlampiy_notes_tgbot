import logging
from io import BytesIO

import wit
from pydub import AudioSegment
from telegram import Update
from telegram.ext import ContextTypes

from src.bot import send_response
from src.config import settings, ENGLISH, RUSSIAN, SPAIN, GERMAN
from src.mongo import get_user_language, get_user_command

logger = logging.getLogger(__name__)


async def from_voice_to_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Translate voice message to text by processing it in 20 second chunks.
    """
    if not update.message.voice:
        return

    voice_file = await update.message.voice.get_file()
    file_data = await voice_file.download_as_bytearray()
    audio_stream = BytesIO(file_data)
    audio = AudioSegment.from_file(audio_stream, format="ogg")

    chunk_length_ms = 19500  # < 20 sec
    chunks = [
        audio[i:i + chunk_length_ms]
        for i in range(0, len(audio), chunk_length_ms)
    ]

    user_id = update.effective_user.id
    user_language = await get_user_language(user_id)
    user_command = await get_user_command(user_id)
    user_voice_translator = voice_translators[user_language]
    full_translated_text = ""
    for i, chunk in enumerate(chunks):
        converted_stream = BytesIO()
        chunk.export(converted_stream, format="mp3")
        converted_stream.seek(0)
        response = user_voice_translator.speech(
            audio_file=converted_stream,
            headers={"Content-Type": "audio/mpeg3"}
        )
        text = response["text"] if "text" in response else ""
        full_translated_text += text

    logger.debug(f"Voice message translation: {full_translated_text}")
    if not full_translated_text:
        logger.debug("Empty voice message.")
        return

    if full_translated_text.lower().startswith(user_command):
        await send_response(
            update,
            context,
            response=f"Command \\*{user_command}* detected in the voice message."
                     f"\nAsk GPT for: {full_translated_text[len(user_command):]}",
        )
        return

    await send_response(
        update,
        context,
        response=full_translated_text,
        reply_to_message_id=update.message.message_id,
    )


voice_translators = {
    ENGLISH: wit.Wit(settings.wit_en_token),
    RUSSIAN: wit.Wit(settings.wit_ru_token),
    SPAIN: wit.Wit(settings.wit_es_token),
    GERMAN: wit.Wit(settings.wit_de_token),
}
