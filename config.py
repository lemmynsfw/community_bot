import os
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    USERNAME: str
    PASSWORD: str
    BOT_ID: int
    INSTANCE: str
    LOCAL: bool
    EMAIL_FUNCTION: bool
    SMTP_SERVER: str
    SMTP_PORT: int
    SENDER_EMAIL: str
    SENDER_PASSWORD: str
    SURVEY_CODE: str
    SLUR_ENABLED: bool
    SLUR_REGEX: str
    SERIOUS_WORDS: str
    MATRIX_FLAG: bool
    MATRIX_API_KEY: str
    MATRIX_ROOM_ID: str
    MATRIX_URL: str
    MATRIX_ACCOUNT: str
    RSS_ENABLED: bool
    GIVEAWAY_ENABLED: bool
    DEBUG_LEVEL: str
    STARTUP_WARNING: bool
    DB_NAME: str
    DB_USER: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_PORT: int
    # DEFAULT_INSTANCE_BLOCKS: str
    
    class Config:
        env_file = ".env"


os.environ.pop("USERNAME", None)
os.environ.pop("PASSWORD", None)

settings = Settings()
