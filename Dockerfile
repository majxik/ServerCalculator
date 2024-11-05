FROM python:3.11-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

RUN pip install pytest

COPY . .

RUN ["pytest"]

CMD ["python", "app.py"]