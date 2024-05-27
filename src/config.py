from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        case_sensitive=False,
        # env_file=".env",
    )

    debug: bool = True
    environment: str = "dev"
    default_language: str = "ru"
    telegram_bot_token: str = ""
    telegram_bot_command: str = "кузьма"

    local_auth_db: str = ""
    echo_sql: bool = False

    gpt_token: str = ""

    wit_ru_token: str = ""
    wit_en_token: str = ""
    wit_es_token: str = ""
    wit_de_token: str = ""

    throttle_limit: int = 100               # 100 attempts per 60 sec
    throttle_window: int = 60


settings: Settings = Settings()

LANGUAGES = ("ru", "en", "es", "de", )
if settings.default_language not in LANGUAGES:
    raise ValueError(f"default_language should be one of {LANGUAGES}")
