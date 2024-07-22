from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

from src.bot import send_response
from src.localization import get_translate
from src.mongo import get_user_language, set_user_language


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # user_id = update.message.from_user.id
    user_id = update.effective_user.id
    language = get_user_language(user_id)
    await update.message.reply_text(
        f"I translate a voice message to text!\n"
        f" Your current language are:\n"
        f"Voice Language: {language}")
    # await send_response(update, context, response="I translate a voice message to text")


async def help_info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await send_response(
        update,
        context,
        response="/start - Start the bot\n"
                 "/set_voice_language - Set the voice language\n"
                 "/help - Show this help message\n"
                 "/evlampiy - Command for gpt",
    )


async def choose_language(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Русский", callback_data="set_lang_ru")],
        [InlineKeyboardButton("English", callback_data="set_lang_en")],
        [InlineKeyboardButton("Español", callback_data="set_lang_es")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "Please choose your preferred language:",
        reply_markup=reply_markup,
    )


async def lang_buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id

    lang_code = query.data.split('_')[-1]
    await query.edit_message_text(text=get_translate("choose_language", lang_code))
    set_user_language(user_id, lang_code)
