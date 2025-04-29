#!/bin/bash
echo "Creating staticfiles directory..."
mkdir -p /app/staticfiles
echo "Setting permissions for staticfiles..."
chmod -R 755 /app/staticfiles
echo "Running migrations..."
python manage.py migrate
echo "Running collectstatic..."
python manage.py collectstatic --noinput --verbosity 2 --traceback
echo "Starting Daphne..."
daphne -b 0.0.0.0 -p 8000 store.asgi:application

#!/bin/bash
echo "Creating staticfiles directory..."
mkdir -p /app/staticfiles
echo "Setting permissions for staticfiles..."
chmod -R 755 /app/staticfiles
echo "Running migrations..."
python manage.py migrate
echo "Running collectstatic..."
python manage.py collectstatic --noinput --verbosity 2 --traceback
echo "Starting Daphne..."
daphne -b 0.0.0.0 -p 8000 store.asgi:application