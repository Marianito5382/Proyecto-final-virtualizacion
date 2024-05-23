FROM python:3.8-slim

WORKDIR /app

COPY control_stock.py .
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "control_stock.py"]

