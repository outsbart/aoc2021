FROM python:3.10-slim

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE 1

RUN apt-get update && apt-get install -y

RUN addgroup --system app && adduser --system --group app

USER app

WORKDIR /app

RUN python -m pip install --upgrade pip --no-warn-script-location

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD python main.py
