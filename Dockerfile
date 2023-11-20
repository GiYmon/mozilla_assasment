FROM python:3.11.4-slim-bullseye

ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install "psycopg[binary]"

COPY . .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
