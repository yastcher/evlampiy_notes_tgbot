from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

from src.bot import send_response
from src.mongo import get_user_language, set_user_language


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    language = get_user_language(user_id)
    await send_response(update, context, response="I translate a voice message to text")


async def help_info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await send_response(
        update,
        context,
        response="/start - Start the bot\n"
                 "/help - Show this help message\n"
                 "/evlampiy - Command for gpt",
    )


async def choose_language(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [
            InlineKeyboardButton("English", callback_data='set_lang_en'),
            InlineKeyboardButton("Русский", callback_data='set_lang_ru')
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "Please choose your language / Пожалуйста, выберите язык",
        reply_markup=reply_markup,
    )


async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    user_id = query.from_user.id

    if query.data == 'set_lang_en':
        set_user_language(user_id, "en")
        await query.answer()
        await query.edit_message_text(text="Language set to English")
    elif query.data == 'set_lang_ru':
        set_user_language(user_id, 'ru')
        await query.answer()
        await query.edit_message_text(text="Язык установлен на Русский")
