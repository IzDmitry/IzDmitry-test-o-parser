# Используем базовый образ Python
FROM python:3.9

# Устанавливаем зависимости
RUN pip install --upgrade pip
COPY requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt

# Копируем файлы проекта в контейнер
COPY . /app
WORKDIR /app

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/app/entrypoint.sh"]

# Запускаем Gunicorn
#CMD ["gunicorn", "--bind", "0.0.0.0:8000", "backend.wsgi"]

# Добавляем Celery
#CMD ["celery", "-A", "backend", "worker", "--loglevel=info"]


#docker build -t django-backend .
#docker run -p 8000:8000 django-backend