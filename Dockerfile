FROM python:3.11-bookworm

WORKDIR /app

ENV PYTHONUNBUFFERED=1 \
    PYTHONPATH=/app \
    DJANGO_SETTINGS_MODULE=betterreads.settings \
    PORT=8000 \
    WEB_CONCURRENCY=2

RUN apt-get update --yes --quiet \
    && apt-get install --yes --quiet --no-install-recommends \
    && apt-get install nodejs -y \
    && apt install npm -y --fix-missing

RUN addgroup --system django \
    && adduser --system --ingroup django django

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

COPY . .

RUN python manage.py tailwind install
RUN python manage.py tailwind build
RUN python manage.py collectstatic --noinput --clear

RUN chown -R django:django /app
USER django

# Uncomment below for development
# RUN python manage.py migrate 

# CMD gunicorn betterreads.wsgi:application --bind 0.0.0.0:5000