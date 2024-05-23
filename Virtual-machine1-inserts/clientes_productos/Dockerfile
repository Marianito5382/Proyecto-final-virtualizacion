FROM python:3.8-slim

WORKDIR /app

COPY clientes_productos.py .
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "clientes_productos.py"]
