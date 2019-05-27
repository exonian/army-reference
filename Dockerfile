FROM python:3.7-alpine3.9

RUN \
  apk --no-cache add bash bash-completion curl postgresql-libs && \
  apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev

ADD . /code
WORKDIR /code

RUN pip install -r requirements.txt

RUN adduser -D app
USER app
WORKDIR /code/armyref

CMD ["gunicorn", "armyref.wsgi", "--bind=0.0.0.0:8000"]
