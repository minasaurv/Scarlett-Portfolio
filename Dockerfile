FROM python:3.13-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . /app/

RUN python manage.py collectstatic --noinput

EXPOSE 8000

# Railway provides $PORT; fall back to 8000 for docker-compose
CMD ["sh", "-c", "gunicorn --workers 3 --bind 0.0.0.0:${PORT:-8000} scarlett_portfolio.wsgi:application"]
