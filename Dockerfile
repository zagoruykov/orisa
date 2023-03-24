FROM python:3.9.6-alpine

WORKDIR /usr/src/orisa_api

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


# install dependencies
RUN apk add --update --no-cache --virtual .tmp-build-deps \
    gcc libc-dev linux-headers postgresql-dev \
    && apk add libffi-dev
RUN pip install --upgrade pip
RUN pip install poetry

COPY pyproject.toml poetry.lock ./

RUN poetry install

# copy entrypoint.sh
COPY ./entrypoint.sh ./
RUN sed -i 's/\r$//g' /usr/src/orisa_api/entrypoint.sh
RUN chmod +x /usr/src/orisa_api/entrypoint.sh

# copy project
COPY . .

# run entrypoint.sh
ENTRYPOINT ["sh", "/usr/src/orisa_api/entrypoint.sh"]


