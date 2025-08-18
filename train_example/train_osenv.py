import os
import random
import time

# --- "Bad" config handling with os.getenv" ---
# We delay parsing/validation until deep in the run.
# If LEARNING_RATE is invalid (e.g., "fast"), we won't crash until epoch 3.
# If API_KEY is missing, we won't notice until the very end.


def maybe_heavy_setup():
    print("🔧 Heavy setup...")
    time.sleep(1)


def train_one_epoch(epoch):
    # Simulate compute
    print(f"🧠 Epoch {epoch} running...")
    time.sleep(1)


def log_to_service(api_key: str, metrics: dict):
    # Simulate a metrics push that needs an API key
    if not api_key:
        raise RuntimeError("Missing API_KEY for metrics service")
    print(f"📡 Logged metrics with API key: {api_key}")


def main():
    print("🚀 Starting training (os.getenv approach)...")
    maybe_heavy_setup()

    # We store raw strings from the environment and defer validation
    lr_raw = os.getenv("LEARNING_RATE")
    api_key = os.getenv("API_KEY")  # may be None; we won't check yet

    # Simulate a long run before we finally use the values properly
    for epoch in range(1, 7):
        train_one_epoch(epoch)

        # We (badly) wait until epoch 3 to use the learning rate for a new optimizer
        if epoch == 3:
            print("⚙️  Rebuilding optimizer with LEARNING_RATE from env...")
            # Now we finally validate the value; this can crash late
            lr = float(lr_raw)  # ValueError if lr_raw isn't a float-like string
            print(f"✅ Set learning rate: {lr}")

    # End-of-run logging that finally checks API_KEY
    print("🧾 Finalizing... pushing metrics")
    log_to_service(api_key, {"final_loss": random.random()})
    print("🎉 Training completed successfully")


if __name__ == "__main__":
    main()
