FROM python:3.7-alpine3.9

# RUN apk --no-cache add curl

ADD . /code
WORKDIR /code

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["armyref/manage.py", "runserver", "0.0.0.0:8000"]
