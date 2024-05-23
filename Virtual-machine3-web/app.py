from flask import Flask, render_template
import pandas as pd
import psycopg2

app = Flask(__name__)

@app.route('/')
def index():
    conn = psycopg2.connect(
        host="192.168.1.51",
        port="5433",
        user="elvendedor",
        password="123abc",
        database="Base_ventas"
    )

    query = """
        SELECT productoid, SUM(cantidad) AS stock
        FROM detalleventas
        GROUP BY productoid
    """

    df = pd.read_sql_query(query, conn)

    productos = df['productoid'].tolist()
    stock = df['stock'].tolist()

    return render_template('index.html', productos=productos, stock=stock)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

