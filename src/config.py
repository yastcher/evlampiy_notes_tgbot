from pydantic_settings import BaseSettings, SettingsConfigDict

ENGLISH = "en"
RUSSIAN = "ru"
SPAIN = "es"
GERMAN = "de"
LANGUAGES = (ENGLISH, RUSSIAN, SPAIN, GERMAN, )


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        case_sensitive=False,
        env_file=".env",
    )

    debug: bool = True
    environment: str = "dev"
    default_language: str = RUSSIAN
    telegram_bot_token: str = ""
    telegram_bot_command: str = "кузьма"

    mongo_uri: str = "mongodb://mongodb:27017/"

    gpt_token: str = ""
    gpt_model: str = "gpt-3.5-turbo"

    wit_ru_token: str = ""
    wit_en_token: str = ""
    wit_es_token: str = ""
    wit_de_token: str = ""


settings: Settings = Settings()
