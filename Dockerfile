FROM python:3.11.4-slim-bullseye

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

# install dependencies
RUN apt-get update && apt-get install --no-install-recommends -y \
    python3-dev \
    libpq-dev \
    gcc \
    && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install "psycopg[binary]"

COPY . .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]