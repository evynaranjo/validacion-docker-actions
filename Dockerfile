# syntax=docker/dockerfile:1

FROM python:3.12-slim

WORKDIR /app

COPY app.py .

RUN python -m py_compile app.py

CMD ["python", "app.py"]
