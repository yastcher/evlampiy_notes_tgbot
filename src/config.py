import os

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        case_sensitive=False,
        env_file=".env",
    )

    debug: bool = True
    environment: str = "dev"
    default_language: str = "ru"
    telegram_bot_token: str = ""
    telegram_bot_command: str = "evlampiy"

    local_auth_db: str = ""
    echo_sql: bool = False

    throttle_limit: int = 100               # 100 attempts per 60 sec
    throttle_window: int = 60


settings: Settings = Settings()

LANGUAGES = ("ru", "en", "es", "de", )

if settings.default_language not in LANGUAGES:
    raise ValueError(f"default_language should be one of {LANGUAGES}")

for lang in LANGUAGES:
    env_token_name = f"WIT_{lang.upper()}_TOKEN"
    env_token_value = os.getenv(env_token_name, "")
    globals()[env_token_name] = env_token_value
    if lang == settings.default_language and not env_token_value:
        raise ValueError(f"Default language token {env_token_name} should be initialized")
