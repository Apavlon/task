FROM python:3.11-slim
WORKDIR /app
RUN python -m venv /app/venv
ENV PATH="/app/venv/bin:$PATH"
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
RUN python manage.py collectstatic --noinput
RUN python manage.py migrate
EXPOSE 8000
CMD ["daphne", "-b", "0.0.0.0", "-p", "8000", "store.asgi:application"]