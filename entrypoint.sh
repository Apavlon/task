#!/bin/bash
mkdir -p /app/staticfiles  # На всякий случай создаем директорию
python manage.py migrate
python manage.py collectstatic --noinput --verbosity 2
daphne -b 0.0.0.0 -p 8000 store.asgi:application