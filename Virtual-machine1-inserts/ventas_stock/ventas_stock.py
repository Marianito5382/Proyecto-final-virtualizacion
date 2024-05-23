import psycopg2
import random
import time
from datetime import datetime

DB_HOST_CLIENTES = "192.168.1.51"
DB_PORT_CLIENTES = "5432"
DB_USER_CLIENTES = "elcliente"
DB_PASS_CLIENTES = "123abc"
DB_CLIENTES = "Base_clientes"

DB_HOST_VENTAS = "192.168.1.51"
DB_PORT_VENTAS = "5433"
DB_USER_VENTAS = "elvendedor"
DB_PASS_VENTAS = "123abc"
DB_VENTAS = "Base_ventas"

def generate_random_cliente_id():
    conn = psycopg2.connect(
        host=DB_HOST_CLIENTES,
        port=DB_PORT_CLIENTES,
        user=DB_USER_CLIENTES,
        password=DB_PASS_CLIENTES,
        database=DB_CLIENTES
    )
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM clientes ORDER BY RANDOM() LIMIT 1")
    cliente_id = cursor.fetchone()[0]
    cursor.close()
    conn.close()
    return cliente_id

def generate_random_producto_id():
    conn = psycopg2.connect(
        host=DB_HOST_VENTAS,
        port=DB_PORT_VENTAS,
        user=DB_USER_VENTAS,
        password=DB_PASS_VENTAS,
        database=DB_VENTAS
    )
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM productos ORDER BY RANDOM() LIMIT 1")
    producto_id = cursor.fetchone()[0]
    cursor.close()
    conn.close()
    return producto_id

def generate_random_cantidad():
    return random.randint(1, 5)

def insert_venta():
    cliente_id = generate_random_cliente_id()
    producto_id = generate_random_producto_id()
    cantidad = generate_random_cantidad()
    
    conn = psycopg2.connect(
        host=DB_HOST_VENTAS,
        port=DB_PORT_VENTAS,
        user=DB_USER_VENTAS,
        password=DB_PASS_VENTAS,
        database=DB_VENTAS
    )
    cursor = conn.cursor()

    cursor.execute("SELECT precio FROM productos WHERE id = %s", (producto_id,))
    precio_unitario = cursor.fetchone()[0]
    subtotal = precio_unitario * cantidad

    query_venta = "INSERT INTO ventas (fechaventa, clienteid, total) VALUES (%s, %s, %s) RETURNING id"
    cursor.execute(query_venta, (datetime.now(), cliente_id, subtotal))
    venta_id = cursor.fetchone()[0]

    query_detalle = "INSERT INTO detalleventas (ventaid, productoid, cantidad, preciounitario, subtotal) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(query_detalle, (venta_id, producto_id, cantidad, precio_unitario, subtotal))

    query_update_stock = "UPDATE productos SET stock = stock - %s WHERE id = %s"
    cursor.execute(query_update_stock, (cantidad, producto_id))

    conn.commit()
    cursor.close()
    conn.close()
    print(f"Venta insertada: Cliente ID {cliente_id}, Producto ID {producto_id}, Cantidad {cantidad}, Total {subtotal}")

while True:
    insert_venta()
    time.sleep(10)

