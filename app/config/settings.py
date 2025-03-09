from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Settings for the Flask application.
    """

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    NAME: str = "@solnustec.com/flask-template"
    DESCRIPTION: str = "Write a simple description"
    VERSION: str = "0.1.0-SNAPSHOT"
    AUTHOR: str = "Solnustec"
    KEYWORDS: list = []

    DEBUG: bool = False
    ENVIRONMENT: str = "production"
    CORS_ORIGINS: list[str] = ["*"]


settings = Settings()
