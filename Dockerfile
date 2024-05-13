FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y ffmpeg build-essential libffi-dev libssl-dev \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir poetry

COPY pyproject.toml ./

RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi

COPY . .

CMD ["python", "main.py"]
