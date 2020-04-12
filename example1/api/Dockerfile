FROM python:3.7-alpine3.10

WORKDIR /code

ENV FLASK_APP=app-flask.py \ 
    FLASK_ENV=development

#ENV FLASK_RUN_HOST flask

RUN apk add --no-cache gcc musl-dev linux-headers

COPY .  .

RUN pip install -r requirements.txt


EXPOSE 5000

CMD ["flask", "run"]
