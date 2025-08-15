import os

from fastapi import FastAPI

DEBUG = os.getenv("DEBUG", "false").lower() == "true"

raw_value = os.getenv("MAX_CONNECTIONS")

# Validation of MAX_CONNECTIONS environment variable
MAX_CONNECTIONS = int(raw_value)

if MAX_CONNECTIONS <= 0:
    raise ValueError(f"MAX_CONNECTIONS must be > 0 (got {MAX_CONNECTIONS})")

app = FastAPI()


@app.get("/config")
def get_config():
    return {
        "app": "os.getenv Example",
        "debug": DEBUG,
        "max_connections": MAX_CONNECTIONS,
    }
