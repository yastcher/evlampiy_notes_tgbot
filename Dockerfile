FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get install -y ffmpeg build-essential libffi-dev libssl-dev && \
    rm -rf /var/lib/apt/lists/*

COPY . .

RUN pip install uv && uv sync
ENV PATH="/app/.venv/bin:$PATH"

CMD ["python", "main.py"]
