FROM python:3.7-alpine3.9

RUN apk --no-cache add bash bash-completion curl

ADD . /code
WORKDIR /code

RUN pip install -r requirements.txt

# TODO remove to a job
RUN armyref/manage.py migrate

CMD ["armyref/manage.py", "runserver", "0.0.0.0:8000"]
