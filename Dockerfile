FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8000
# CMD ["gunicorn", "--bind", "0.0.0.0:8000", "store.asgi:application"]
CMD ["daphne", "-b", "0.0.0.0", "-p", "8000" "store.asgi:application"]