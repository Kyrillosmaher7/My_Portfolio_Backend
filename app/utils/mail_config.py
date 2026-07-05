from pydantic_settings import (
    BaseSettings,
    SettingsConfigDict,
)
from fastapi_mail import ConnectionConfig


class Settings(BaseSettings):

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )

    # Mail
    MAIL_USERNAME: str
    MAIL_FROM: str
    MAIL_PASSWORD: str
    MAIL_PORT: int
    MAIL_HOST: str
    MAIL_STARTTLS: bool
    MAIL_SSL_TLS: bool

    # JWT
    JWT_SECRET_KEY: str
    JWT_ALGORITHM: str = "HS256"

    ACCESS_TOKEN_MINUTES: int = 15
    REFRESH_TOKEN_DAYS: int = 30


settings = Settings()


conf = ConnectionConfig(
    MAIL_USERNAME=settings.MAIL_USERNAME,
    MAIL_PASSWORD=settings.MAIL_PASSWORD,
    MAIL_FROM=settings.MAIL_FROM,
    MAIL_PORT=settings.MAIL_PORT,
    MAIL_SERVER=settings.MAIL_HOST,
    MAIL_STARTTLS=settings.MAIL_STARTTLS,
    MAIL_SSL_TLS=settings.MAIL_SSL_TLS,
    USE_CREDENTIALS=True,
    VALIDATE_CERTS=True,
)