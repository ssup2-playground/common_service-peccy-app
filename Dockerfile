FROM python:3.9-slim-buster

WORKDIR /app

RUN apt-get update && apt-get install default-libmysqlclient-dev gcc -y
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "run.py"]