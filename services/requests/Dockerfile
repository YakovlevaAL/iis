# Используем официальный Python образ
FROM python:3.11-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем requirements.txt
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем код приложения
COPY request_sender.py .

# Запускаем приложение
CMD ["python", "request_sender.py"]

# Команды для сборки и запуска (закомментированы)
# docker build -t requests-service:1 .
# docker run --network host requests-service:1
