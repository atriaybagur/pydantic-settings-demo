from pydantic import PositiveInt
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    debug: bool = False
    max_connections: PositiveInt


settings = Settings()
