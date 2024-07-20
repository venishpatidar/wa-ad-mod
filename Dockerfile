FROM python:3

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . /app

FROM openwa/wa-automate
ENTRYPOINT []


CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "7860"]
