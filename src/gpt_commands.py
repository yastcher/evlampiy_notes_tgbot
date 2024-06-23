import logging

import openai
from telegram import Update
from telegram.ext import ContextTypes

from src.bot import send_response
from src.config import settings

logger = logging.getLogger(__name__)


client = openai.OpenAI(
    api_key=settings.gpt_token,
)


async def evlampiy_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text

    try:
        chat_response = client.chat.completions.create(
            model=settings.gpt_model,
            messages=[
                {"role": "user", "content": user_message}
            ],
            temperature=0.7,
        )

        gpt_response = chat_response['choices'][0]['message']['content']

        await send_response(
            update,
            context,
            response=gpt_response
        )
    except Exception as e:
        logger.error(f"Error occurred: {e}")
        await send_response(
            update,
            context,
            response=str(e)
        )
