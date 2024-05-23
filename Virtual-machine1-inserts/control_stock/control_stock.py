import psycopg2
import time

DB_HOST_VENTAS = "192.168.1.51"
DB_PORT_VENTAS = "5433"
DB_USER_VENTAS = "elvendedor"
DB_PASS_VENTAS = "123abc"
DB_VENTAS = "Base_ventas"

def check_and_update_stock():
    conn = psycopg2.connect(
        host=DB_HOST_VENTAS,
        port=DB_PORT_VENTAS,
        user=DB_USER_VENTAS,
        password=DB_PASS_VENTAS,
        database=DB_VENTAS
    )
    cursor = conn.cursor()
    query_select = "SELECT id, stock FROM productos WHERE stock < 5"
    cursor.execute(query_select)
    productos_bajo_stock = cursor.fetchall()

    for producto in productos_bajo_stock:
        producto_id, stock_actual = producto
        nuevo_stock = stock_actual + 20
        query_update = "UPDATE productos SET stock = %s WHERE id = %s"
        cursor.execute(query_update, (nuevo_stock, producto_id))
        print(f"Producto ID {producto_id} stock actualizado a {nuevo_stock}")

    conn.commit()
    cursor.close()
    conn.close()

while True:
    check_and_update_stock()
    time.sleep(5)
