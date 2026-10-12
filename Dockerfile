FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirement.txt

COPY application.py .
COPY test_app.py .

CMD ["pytest", "-v"]