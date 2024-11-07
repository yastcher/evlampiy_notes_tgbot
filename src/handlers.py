from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes, ConversationHandler

from src.localization import get_translate
from src.mongo import get_user_language, set_user_language, get_user_command, set_user_command

WAITING_FOR_COMMAND = 1


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # user_id = update.message.from_user.id
    user_id = update.effective_user.id
    user_language = await get_user_language(user_id)
    user_command = await get_user_command(user_id)
    await update.message.reply_text(
        f"I can translate a voice message to text!\n"
        f"current language are: {user_language}\n"
        f"current voice command are (you can start voice from): {user_command}\n"
        f"/start - Show this message\n"
        f"/choose_your_language - Set the voice language\n"
        f"/enter_your_command - Enter your command for gpt\n"
        f"/test_gpt - Command for gpt",
    )
    # await send_response(update, context, response="I translate a voice message to text")


async def choose_language(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Русский", callback_data="set_lang_ru")],
        [InlineKeyboardButton("English", callback_data="set_lang_en")],
        [InlineKeyboardButton("Español", callback_data="set_lang_es")],
        [InlineKeyboardButton("Deutsch", callback_data="set_lang_de")],
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
    await query.edit_message_text(text=get_translate("choose_my_language", lang_code))
    await set_user_language(user_id, lang_code)


async def enter_your_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Please enter your command for GPT:")
    return WAITING_FOR_COMMAND


async def handle_command_input(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    user_command = update.message.text
    await set_user_command(user_id, user_command)
    await update.message.reply_text(f"Your command '{user_command}' has been saved.")
    return ConversationHandler.END
