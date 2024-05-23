import psycopg2
import random
import time

DB_HOST_CLIENTES = "192.168.1.51"
DB_USER_CLIENTES = "elcliente"
DB_PASS_CLIENTES = "123abc"
DB_CLIENTES = "Base_clientes"
DB_PORT_CLIENTES = "5432"

DB_HOST_VENTAS = "192.168.1.51"
DB_USER_VENTAS = "elvendedor"
DB_PASS_VENTAS = "123abc"
DB_VENTAS = "Base_ventas"
DB_PORT_VENTAS = "5433"

def generate_random_nombre():
    letras = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return ''.join(random.choice(letras) for _ in range(8))

def generate_random_precio():
    return round(random.uniform(1, 1000), 2)

def insert_cliente():
    nombre = generate_random_nombre()
    conn = psycopg2.connect(
        host=DB_HOST_CLIENTES,
        port=DB_PORT_CLIENTES,
        user=DB_USER_CLIENTES,
        password=DB_PASS_CLIENTES,
        database=DB_CLIENTES
    )
    cursor = conn.cursor()
    query = "INSERT INTO clientes (nombre) VALUES (%s)"
    cursor.execute(query, (nombre,))
    conn.commit()
    cursor.close()
    conn.close()
    print(f"Cliente insertado: {nombre}")

def insert_producto():
    nombre = generate_random_nombre()
    precio = generate_random_precio()
    stock = 20
    conn = psycopg2.connect(
        host=DB_HOST_VENTAS,
        port=DB_PORT_VENTAS,
        user=DB_USER_VENTAS,
        password=DB_PASS_VENTAS,
        database=DB_VENTAS
    )
    cursor = conn.cursor()
    query = "INSERT INTO productos (nombre, precio, stock) VALUES (%s, %s, %s)"
    cursor.execute(query, (nombre, precio, stock))
    conn.commit()
    cursor.close()
    conn.close()
    print(f"Producto insertado: {nombre}, Precio: {precio}, Stock: {stock}")

while True:
    insert_cliente()
    insert_producto()
    time.sleep(2)
