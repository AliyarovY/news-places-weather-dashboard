FROM python:3.11-slim

WORKDIR /code

RUN apt-get update && apt-get install -y gcc libjpeg-dev libpq-dev

RUN pip install poetry

COPY ./pyproject.toml /code/pyproject.toml

RUN poetry install --no-cache-dir --no-root --file /code/pyproject.toml

COPY . .

CMD make run