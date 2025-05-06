# Builder stage (optional, but good for caching dependencies if needed later)
FROM python:3.9 AS builder

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Runtime stage
FROM python:3.9-slim

WORKDIR /app

# Install dependencies directly in the runtime stage
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy your application code AND the templates directory
COPY . .

CMD ["python", "app.py"]