from typing import Optional

from telegram import InlineKeyboardMarkup, Update
from telegram.ext import ContextTypes
from telegram.constants import ParseMode

from src.speech import transcribe_audio


async def send_response(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
    response: str,
    keyboard: Optional[InlineKeyboardMarkup] = None
) -> None:
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=response,
        parse_mode=ParseMode.HTML,
        disable_web_page_preview=True,
        reply_markup=keyboard
    )


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await send_response(update, context, response="I translate a voice message to text")


async def help_info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await send_response(update, context, response="/start - Start the bot\n/help - Show this help message")


async def from_voice_to_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    translate voice message to text
    """
    translated_text = transcribe_audio(await update.message.voice.get_file())
    await send_response(update, context, response=translated_text)
