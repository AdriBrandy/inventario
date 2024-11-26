
SHOW DATABASES;

CREATE DATABASE TP_LABORATORIO_BDD;

USE TP_LABORATORIO_BDD;

-- -------------------------------------------------------------------------------------------------
-- CREACION DE LAS TABLAS
-- ------------------------------------------------------------------------------------------------

DROP TABLE IF EXISTS marcas;
DROP TABLE IF EXISTS linea_productos;
DROP TABLE IF EXISTS productos;

CREATE TABLE marcas (
    ID_Marcas_PK INT AUTO_INCREMENT PRIMARY KEY,
    Descripcion_Marcas VARCHAR(255) NOT NULL
);

CREATE TABLE linea_productos (
    ID_linea_productos_PK INT AUTO_INCREMENT PRIMARY KEY,
    Descripcion_linea_productos VARCHAR(255) NOT NULL
);

CREATE TABLE productos (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    PRODUCTO VARCHAR(255) NOT NULL,
    ID_LINEA_PRODUCTO_FK INT,
    CANTIDAD INT NOT NULL,
    PRECIO_UNITARIO DECIMAL(10, 2) NOT NULL,
    COLOR VARCHAR(50),
    COSTO_UNITARIO DECIMAL(10, 2) NOT NULL,
    ID_MARCAS_FK INT,  
    FOREIGN KEY (ID_MARCAS_FK) REFERENCES marcas(ID_Marcas_PK),
    FOREIGN KEY (ID_LINEA_PRODUCTO_FK) REFERENCES linea_productos(ID_linea_productos_PK)
);


-- -------------------------------------------------------------------------------------------------
-- INSERCIONES DE LAS TABLAS
-- ------------------------------------------------------------------------------------------------
INSERT INTO marcas (Descripcion_Marcas) 
VALUES 
('Coca-Cola'), 
('Baggio'), 
('Samsung'), 
('Yogurísimo'), 
('Bagley'), 
('Quilmes'), 
('SanCor');

INSERT INTO linea_productos (Descripcion_linea_productos) 
VALUES 
('Hogar'), 
('Electrodomésticos');

INSERT INTO productos (PRODUCTO, ID_LINEA_PRODUCTO_FK, CANTIDAD, PRECIO_UNITARIO, COLOR, COSTO_UNITARIO, ID_MARCAS_FK) 
VALUES 
('Aspiradora', 1, 20, 150.00, 'Rojo', 100.00, 2),
('Licuadora', 1, 15, 80.00, 'Negro', 50.00, 2),
('Televisor', 2, 10, 500.00, 'Plata', 400.00, 1),
('Microondas', 1, 25, 120.00, 'Blanco', 80.00, 3),
('Refrigerador', 2, 5, 800.00, 'Negro', 600.00, 1),
('Plancha', 1, 30, 40.00, 'Rojo', 25.00, 2),
('Cafetera', 1, 12, 60.00, 'Blanco', 35.00, 3),
('Horno Eléctrico', 2, 8, 200.00, 'Negro', 150.00, 1),
('Aire Acondicionado', 2, 4, 1200.00, 'Blanco', 900.00, 1),
('Batidora', 1, 18, 70.00, 'Rojo', 45.00, 2);









