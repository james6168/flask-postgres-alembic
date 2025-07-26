FROM python:3.10.18-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /flask-app

COPY /app /flask-app/

RUN pip install --no-cache-dir --upgrade-pip -r requirements.txt

CMD [ "python", "main.py" ]



