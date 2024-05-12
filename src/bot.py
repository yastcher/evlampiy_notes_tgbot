from typing import Optional

from telegram import Update, InlineKeyboardMarkup
from telegram.constants import ParseMode
from telegram.ext import ApplicationBuilder, ContextTypes

from src.config import settings

application = ApplicationBuilder().token(settings.telegram_bot_token).build()


async def send_response(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
    response: str,
    keyboard: Optional[InlineKeyboardMarkup] = None,
    **kwargs,
) -> None:
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=response,
        parse_mode=ParseMode.HTML,
        disable_web_page_preview=True,
        reply_markup=keyboard,
        **kwargs,
    )
