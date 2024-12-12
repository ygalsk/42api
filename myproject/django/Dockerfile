# Use a Debian/Ubuntu base image
FROM python:3.8.3-slim

WORKDIR /app

# Install system dependencies and Python
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    redis-server \
    python3-venv \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN python3 -m venv env/bin/activate
RUN . env/bin/activate
RUN pip install --no-cache-dir django django-bootstrap5 django-environ psycopg2
COPY . .

# Expose the application port
EXPOSE 8000

# Run the Django application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
