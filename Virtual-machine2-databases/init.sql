CREATE DATABASE Base_ventas;

\c Base_ventas

CREATE TABLE productos (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    precio DECIMAL(10, 2) NOT NULL,
    stock INT NOT NULL
);

CREATE TABLE ventas (
    id SERIAL PRIMARY KEY,
    fechaventa TIMESTAMP NOT NULL,
    clienteid INT,
    total DECIMAL(10, 2) NOT NULL
);

CREATE TABLE detalleventas (
    id SERIAL PRIMARY KEY,
    ventaid INT NOT NULL,
    productoid INT NOT NULL,
    cantidad INT NOT NULL,
    preciounitario DECIMAL(10, 2) NOT NULL,
    subtotal DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (ventaid) REFERENCES ventas(id),
    FOREIGN KEY (productoid) REFERENCES productos(id)
);
