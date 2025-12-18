# Базовый образ Python
FROM python:3.11-slim

# Устанавливаем системные зависимости
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    && rm -rf /var/lib/apt/lists/*

# Создаем рабочую директорию
WORKDIR /ml_service

# Копируем файлы сервиса
COPY . .

# Создаем директорию для моделей и делаем её доступной извне
VOLUME /models

# Устанавливаем Python зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Открываем порт
EXPOSE 8000

# Команда запуска сервера
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

# Команда для сборки образа (первая версия):
# docker build -t car-price-predictor:1 .

# Команда для запуска контейнера:
# docker run -p 8000:8000 -v $(pwd)/../models:/models car-price-predictor:1
