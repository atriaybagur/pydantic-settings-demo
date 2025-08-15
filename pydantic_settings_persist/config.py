import datetime

from pydantic import FutureDate, PositiveInt, Secret
from pydantic_settings import BaseSettings, SettingsConfigDict

# Define a type for SecretInt to use in settings
SecretInt = Secret[int]


class Settings(BaseSettings):
    debug: bool = False
    max_connections: PositiveInt
    meaning_of_life: SecretInt = 42

    singularity: FutureDate = datetime.date(year=2045, month=1, day=1)

    model_config = SettingsConfigDict(env_file=".env.development")


_settings = Settings()


def get_settings() -> Settings:
    return _settings
