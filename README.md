# pydantic-settings demo

This is a demonstration of using `pydantic-settings` in a FastAPI application, showcasing how to manage configuration settings effectively.

## Tips

To test the API endpoints, you can use the following `curl` commands:

```bash
curl -s http://127.0.0.1:8000/config
curl -s http://127.0.0.1:8000/config | jq
```

## Demo commands

### Motivation

This will assign `DEBUG` the default value, but will error as `MAX_CONNECTIONS` is not set to the environment.

```bash
uv run uvicorn os_env_demo.main:app --reload
```

This will set `MAX_CONNECTIONS` to -1, which is invalid, and will raise ad-hoc error.

```bash
MAX_CONNECTIONS=-1 uv run uvicorn os_env_demo.main:app --reload
```

This will run with valid settings (also test endpoint):

```bash
MAX_CONNECTIONS=5 uv run uvicorn os_env_demo.main:app --reload
```

If we set a truthy value to `DEBUG` (e.g. `DEBUG=1`), it actually evaluates to `false`.

```bash
DEBUG=1 MAX_CONNECTIONS=5 uv run uvicorn os_env_demo.main:app --reload
```

### Pydantic intro

If you want to create a dataclass with input validation, you might do something like this:

```bash
uv run pydantic_intro/main_dataclasses.py
```

Pydantic allows you to define a class with type annotations, and it will validate the input data against those types:

```bash
uv run pydantic_intro/main_pydantic.py
```

### Pydantic-settings (base)

This will assign `DEBUG` the default value, but will error as `MAX_CONNECTIONS` is (required and) not set to the environment. The validation error will be a Pydantic built-in.

```bash
uv run uvicorn pydantic_settings_base.main:app --reload
```

This will set `MAX_CONNECTIONS` to -1, which is invalid, and will raise a Pydantic validation error.

```bash
MAX_CONNECTIONS=-1 uv run uvicorn pydantic_settings_base.main:app --reload
```

This will run with valid settings (also test endpoint):

```bash
MAX_CONNECTIONS=5 uv run uvicorn pydantic_settings_base.main:app --reload
```

If we set a truthy value to `DEBUG`, it will be evaluated correctly:

```bash
DEBUG=1 MAX_CONNECTIONS=5 uv run uvicorn pydantic_settings_base.main:app --reload
```

### Pydantic-settings (read from .env file)

```bash
uv run uvicorn pydantic_settings_env_file.main:app --reload
```

Note pydantic-settings uses the same priority rule as python-dotenv by default: Environment variables take precedence over .env values.

```bash
MAX_CONNECTIONS=-1 uv run uvicorn pydantic_settings_env_file.main:app --reload
```

### Pydantic-settings (with more types)

```bash
uv run uvicorn pydantic_settings_more_types.main:app --reload
```

Try date in the past and use the reload feature to see validation error.

### Pydantic-settings (persist config)

```bash
uv run uvicorn pydantic_settings_persist.main:app --reload
```

## Training example

### `os.getenv()`

```bash
# Invalid learning rate value; app runs for ~3 epochs and then crashes
LEARNING_RATE=fast uv run python train_example/train_osenv.py
```

```bash
# Valid learning rate but missing API key; even later failure during final logging
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
