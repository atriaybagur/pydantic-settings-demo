import random
import time

from pydantic import PositiveFloat, SecretStr, ValidationError
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    learning_rate: PositiveFloat  # must be > 0
    api_key: SecretStr  # required


def maybe_heavy_setup():
    print("🔧 Heavy setup...")
    time.sleep(1)


def train_one_epoch(epoch):
    print(f"🧠 Epoch {epoch} running...")
    time.sleep(1)


def log_to_service(api_key: SecretStr, metrics: dict):
    # Send request with api_key.get_secret_value()
    print(f"📡 Logged metrics with API key: {api_key}")


def main():
    print("🚀 Starting training (pydantic-settings, fail-fast)...")
    try:
        # VALIDATES IMMEDIATELY at startup (fail-fast)
        settings = Settings()
    except ValidationError as e:
        print("❌ Configuration error at startup — refusing to train:")
        print(e)
        return

    maybe_heavy_setup()

    for epoch in range(1, 4):
        train_one_epoch(epoch)

    print("🧾 Finalizing... pushing metrics")
    log_to_service(settings.api_key, {"final_loss": random.random()})
    print("🎉 Training completed successfully")


if __name__ == "__main__":
    main()
