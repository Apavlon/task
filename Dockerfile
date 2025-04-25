FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

RUN mkdir -p /app/staticfiles && chown -R root:root /app/staticfiles
RUN python manage.py collectstatic --noinput --verbosity 2

EXPOSE 8000
CMD ["daphne", "-b", "0.0.0.0", "-p", "8000", "store.asgi:application"]
