FROM python:3.12-slim

# No .pyc: the root filesystem is read-only in the cluster (only /tmp is writable)
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /src

# Runtime dependencies only; dev tools (pytest, black...) stay out of the image
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY main.py .
COPY app ./app

# Numeric non-root user: the cluster enforces runAsNonRoot
USER 10001

# Every container listens on 8080
EXPOSE 8080

CMD ["gunicorn", "--bind", "0.0.0.0:8080", "--workers", "2", "--worker-tmp-dir", "/tmp", "--access-logfile", "-", "main:httpServer"]
