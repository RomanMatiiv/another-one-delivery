FROM python:3.12-slim
LABEL authors="matiiv"

    # python:
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONIOENCODING=UTF-8 \
    # pip:
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    # poetry:
    POETRY_VERSION=1.2.2 \
    POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_CACHE_DIR='/var/cache/pypoetry' \
    PATH="$PATH:/root/.poetry/bin" \
    # OS
    LC_ALL=C.UTF-8 \
    LANG=C.UTF-8

WORKDIR /app

RUN apt-get -y update \
    && rm -rf /var/lib/apt/lists/*

RUN pip install -U pip \
    && pip install poetry==$POETRY_VERSION

COPY ./pyproject.toml ./poetry.lock /app/

RUN poetry install --no-dev --no-ansi \
    && rm -rf "$POETRY_CACHE_DIR"

COPY . /app/
