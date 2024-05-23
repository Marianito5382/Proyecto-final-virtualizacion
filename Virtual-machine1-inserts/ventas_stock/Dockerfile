FROM python:3.8-slim

WORKDIR /app

COPY ventas_stock.py .
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "ventas_stock.py"]

