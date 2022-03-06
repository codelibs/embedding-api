FROM python:3.8 as builder


RUN pip install poetry==1.1.13

COPY ./app /tmp/app
WORKDIR /tmp/app/
RUN poetry export -f requirements.txt --output requirements.txt --without-hashes

FROM python:3.8

COPY --from=builder /tmp/app/requirements.txt /code/requirements.txt
RUN pip install --upgrade pip==22.0.3 && \
    pip install --no-cache-dir --upgrade -r /code/requirements.txt && \
    python -m spacy download en_core_web_trf && \
    python -c "import spacy;spacy.load('ja_ginza_electra')"

COPY ./app /code/app
WORKDIR /code/app/

CMD ["uvicorn", "fess_text_vectorizer.app:app", "--host", "0.0.0.0", "--port", "8900"]
