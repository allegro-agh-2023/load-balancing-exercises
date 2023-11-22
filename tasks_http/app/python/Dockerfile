# syntax=docker/dockerfile:1

# source: https://docs.docker.com/language/python/build-images/

FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD ["gunicorn", "-w", "1", "-b", "0.0.0.0:5000", "main:app"]
