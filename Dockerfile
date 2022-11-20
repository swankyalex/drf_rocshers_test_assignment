FROM python:3.10

RUN apt install --no-install-recommends --yes \
    bash \
    curl \
    g++ \
    make


RUN apt clean && rm -rf /var/lib/apt/lists/* && rm -rf /var/cache/apt/archives

WORKDIR /app

COPY poetry.lock pyproject.toml ./

RUN pip install poetry

RUN poetry install

COPY ./ ./
