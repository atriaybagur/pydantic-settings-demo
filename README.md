# pydantic-settings demo

This is a demonstration of using `pydantic-settings` in a FastAPI application, showcasing how to manage configuration settings effectively.

## Tips

To test the API endpoints, you can use the following `curl` commands:

```bash
curl -s http://127.0.0.1:8000/config
curl -s http://127.0.0.1:8000/config | jq
```

## Demo commands

Motivation:

```bash
uv run uvicorn os_env_demo.main:app --reload
MAX_CONNECTIONS=-1 uv run uvicorn os_env_demo.main:app --reload
MAX_CONNECTIONS=5 uv run uvicorn os_env_demo.main:app --reload
```

Truthy value to DEBUG (actually evaluates to `false`):

```bash
DEBUG=1 MAX_CONNECTIONS=5 uv run uvicorn os_env_demo.main:app --reload
```

Pydantic-settings base

```bash
uv run uvicorn pydantic_settings_base.main:app --reload
MAX_CONNECTIONS=-1 uv run uvicorn pydantic_settings_base.main:app --reload
MAX_CONNECTIONS=5 uv run uvicorn pydantic_settings_base.main:app --reload
```

Pydantic-settings with env file

```bash
uv run uvicorn pydantic_settings_env_file.main:app --reload
```

Note pydantic-settings uses the same priority rule as python-dotenv by default: Environment variables take precedence over .env values.

```bash
MAX_CONNECTIONS=-1 uv run uvicorn pydantic_settings_env_file.main:app --reload
```

Pydantic-settings with more types

```bash
uv run uvicorn pydantic_settings_more_types.main:app --reload
```

Try date in the past and use reload to see validation error

Pydantic-settings with persistence

## Training example

###  `os.getenv()`

```bash
# BAD lr value; app runs for ~3 epochs and then crashes late
LEARNING_RATE=fast uv run python train_example/train_osenv.py
```

```bash
# Valid LR but missing API key; late failure during final logging
LEARNING_RATE=0.001 uv run python train_example/train_osenv.py
```

### `pydantic-settings`

```bash
# Invalid learning rate and no API key -> immediate ValidationError
LEARNING_RATE=fast uv run python train_example/train_pydantic.py
```

```bash
# Runs to completion
LEARNING_RATE=0.001 API_KEY=abcd1234 uv run python train_example/train_pydantic.py
```
