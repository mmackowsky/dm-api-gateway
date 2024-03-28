FROM python:3.11

EXPOSE 8001

ENV PYTHONUNBUFFERED=1

WORKDIR /dm_api_gateway

COPY pyproject.toml poetry.lock /dm_api_gateway/

RUN pip3 install poetry && poetry install --no-cache

COPY . .
