import random
import time

from pydantic import PositiveFloat, SecretStr
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    learning_rate: PositiveFloat  # must be > 0
    api_key: SecretStr  # required


settings = Settings()


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
    maybe_heavy_setup()

    # Simulate a long run
    for epoch in range(1, 7):
        train_one_epoch(epoch)

        # We wait until epoch 3 to use the learning rate for a new optimizer
        if epoch == 3:
            print("⚙️  Rebuilding optimizer with LEARNING_RATE from env...")
            print(f"✅ Set learning rate: {settings.learning_rate}")

    # End-of-run logging with API_KEY
    print("🧾 Finalizing... pushing metrics")
    log_to_service(settings.api_key, {"final_loss": random.random()})
    print("🎉 Training completed successfully")


if __name__ == "__main__":
    main()
