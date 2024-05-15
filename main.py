import logging

from telegram.ext import CommandHandler, MessageHandler, filters

from src import handlers
from src.bot import application
from src.config import settings
# from src.gpt_commands import evlampiy_command
from src.speech import from_voice_to_text

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.DEBUG if settings.debug else logging.INFO,
)
trash_loggers = ["httpcore", "httpx", "telegram.ext.ExtBot", ]
for logger_name in trash_loggers:
    logging.getLogger(logger_name).setLevel(logging.WARNING)

logger = logging.getLogger(__name__)

COMMAND_HANDLERS = {
    "start": handlers.start,
    "help": handlers.help_info,
    # "evlampiy": evlampiy_command,
}


if not settings.telegram_bot_token:
    raise ValueError("need TELEGRAM_BOT_TOKEN env variables")


def main():
    for command_name, command_handler in COMMAND_HANDLERS.items():
        application.add_handler(CommandHandler(command_name, command_handler))

    application.add_handler(MessageHandler(filters.VOICE, from_voice_to_text))

    application.run_polling()


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        logger.exception("Error: %s", exc)
