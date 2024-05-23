CREATE DATABASE Base_clientes;

\c Base_clientes

CREATE TABLE Clientes (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL
);
