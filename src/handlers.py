from telegram import Update
from telegram.ext import ContextTypes

from src.bot import send_response


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await send_response(update, context, response="I translate a voice message to text")


async def help_info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await send_response(update, context, response="/start - Start the bot\n/help - Show this help message")
