## Installation

```bash
git clone https://github.com/yastcher/evlampiy_notes_tgbot.git
cd evlampiy_notes_tgbot
pip install uv
uv sync
```

## Configuration

Create `.env` file:

```env
TELEGRAM_BOT_TOKEN=your_bot_token
MONGO_URI=mongodb://localhost:27017/

WIT_RU_TOKEN=your_wit_ru_token
WIT_EN_TOKEN=your_wit_en_token
WIT_ES_TOKEN=your_wit_es_token
WIT_DE_TOKEN=your_wit_de_token

GPT_TOKEN=your_openai_token
GPT_MODEL=gpt-3.5-turbo
```

## Usage

### Local

```bash
uv run python main.py
```

### Docker

```bash
docker compose up -d
```

## Development

```bash
# Install dev dependencies
uv sync --group dev

# Run linter
uv run ruff check

# Run tests
uv run pytest
```
