"""Settings."""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Settings."""

    database_url: str = "sqlite:///data/sqlite/database.db"

    model_config = SettingsConfigDict(env_prefix="backend_")


settings: Settings = Settings()
