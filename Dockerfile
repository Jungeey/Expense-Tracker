
FROM python:3.11-slim AS builder

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

FROM python:3.11-slim

WORKDIR /app

COPY --from=builder /install /usr/local

COPY app.py .
COPY templates/ templates/
COPY static/ static/

RUN useradd --create-home appuser \
    && chown -R appuser:appuser /app

ENV PYTHONUNBUFFERED=1
ENV PORT=80

EXPOSE 80

USER appuser

CMD ["python", "app.py"]
