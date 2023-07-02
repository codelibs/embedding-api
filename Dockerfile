FROM python:3.10 as builder

RUN pip install poetry==1.5.1

COPY ./app /tmp/app
WORKDIR /tmp/app/
RUN poetry export -f requirements.txt --output requirements.txt --without-hashes

FROM python:3.10

COPY --from=builder /tmp/app/requirements.txt /code/requirements.txt
RUN pip install --upgrade pip==23.1.2 && \
    pip install --no-cache-dir --upgrade -r /code/requirements.txt && \
    mkdir -p /code/model

COPY ./app /code/app
WORKDIR /code/app/

CMD ["uvicorn", "embedding_api.app:app", "--host", "0.0.0.0", "--port", "8080"]
