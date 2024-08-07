# Dockerfile
FROM python:3.9-slim

# Устанавливаем зависимости
RUN pip install --upgrade pip
COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

# Копируем файлы приложения
COPY . /app

# Устанавливаем рабочую директорию
WORKDIR /app

# Запускаем приложение
CMD ["python", "main.py"]
