release: django-admin migrate --noinput && python manage.py init_data
web: gunicorn betterreads.wsgi:application