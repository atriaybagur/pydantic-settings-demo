from pydantic import PositiveInt
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    debug: bool = False
    max_connections: PositiveInt

    model_config = SettingsConfigDict(env_file=".env.development")


settings = Settings()
