import os

from dotenv import load_dotenv
from fastapi import FastAPI

# Load .env file from project root into environment variables
# Note: If a variable is already set in the environment (os.environ), load_dotenv() will not overwrite it.
load_dotenv(dotenv_path=".env.development")

DEBUG = os.getenv("DEBUG", "false").lower() == "true"

raw_value = os.getenv("MAX_CONNECTIONS")

# Validation of MAX_CONNECTIONS environment variable
MAX_CONNECTIONS = int(raw_value)

if MAX_CONNECTIONS <= 0:
    raise ValueError(f"MAX_CONNECTIONS must be > 0 (got {MAX_CONNECTIONS})")

app = FastAPI(title="os.getenv Example")


@app.get("/config")
def get_config():
    return {
        "app": "os.getenv + load_dotenv Example",
        "debug": DEBUG,
        "max_connections": MAX_CONNECTIONS,
    }
