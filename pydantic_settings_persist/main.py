from fastapi import FastAPI

from .config import get_settings

app = FastAPI()


@app.get("/config")
def get_config():
    settings = get_settings()
    return {
        "app": "pydantic-settings Example",
        "debug": settings.debug,
        "max_connections": settings.max_connections,
        "meaning_of_life": str(settings.meaning_of_life),
        "singularity": settings.singularity.strftime("%d/%m/%Y"),
    }
