CREATE DATABASE venta_vehiculos;
USE  venta_vehiculos;
-- Creando tabla

CREATE TABLE canal(
	idCanal INT NOT NULL AUTO_INCREMENT,
    tipoCanal varchar (20),
    canal varchar (60),
	PRIMARY KEY(idCanal)
);
-- introduciondo datos a las tablas
 LOAD DATA INFILE 'D:\\CURSOS DE UNI\\CURSO DE PLATZI\\HENRRY\\proyectos personales\\mini proyecto\\data\\canal.csv' 
 -- cargar datos en el  tabla  canal _de ...
 INTO TABLE canal
 -- compas terminados por 
 FIELDS TERMINATED BY ',' 
 -- encerrrados por ninguncaracter especial
 ENCLOSED BY '' ESCAPED BY ''
 -- lienas estan terminadas por 
 -- ignora la primera fila 
 LINES TERMINATED BY '\n' IGNORE 1 ROWS;

CREATE TABLE calendario(
	fecha DATE ,
    anio  YEAR,
    semana INT ,
    mes VARCHAR(20),
    numMes INT,
    idCalendario INT NOT NULL ,
    PRIMARY KEY (idCalendario)
);

LOAD DATA INFILE 'D:\\CURSOS DE UNI\\CURSO DE PLATZI\\HENRRY\\proyectos personales\\mini proyecto\\data\\calendario.csv'
INTO TABLE calendario
FIELDS TERMINATED BY ','
ENCLOSED BY '' ESCAPED BY ''
lINES TERMINATED BY '\n' IGNORE 1 ROWS ;

CREATE TABLE clientes(
	idClientes INT NOT NULL AUTO_INCREMENT,
    Nombre varchar (150),
    PRIMARY KEY(idClientes)
);

LOAD DATA INFILE 'D:\\CURSOS DE UNI\\CURSO DE PLATZI\\HENRRY\\proyectos personales\\mini proyecto\\data\\cliente.csv'
INTO TABLE clientes
FIELDS TERMINATED BY','
LINES TERMINATED BY'\n' IGNORE 1 ROWS ;

CREATE TABLE vehiculo(
	idVehiculo INT NOT NULL AUTO_INCREMENT,
    marcaVehiculo VARCHAR(20),
    modelo VARCHAR(20),
    tipo VARCHAR(20),
    anio YEAR ,
    PRIMARY KEY (idVehiculo)
);

LOAD DATA INFILE 'D:\\CURSOS DE UNI\\CURSO DE PLATZI\\HENRRY\\proyectos personales\\mini proyecto\\data\\vehiculo.csv'
INTO TABLE vehiculo
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n' IGNORE 1 ROWS;

SHOW TABLES ;

CREATE TABLE sede (
	idSede INT NOT NULL AUTO_INCREMENT,
    nombre VARCHAR(50),
    ubicacion  VARCHAR(200),
    PRIMARY KEY (idSede)
);
LOAD DATA INFILE 'D:\\CURSOS DE UNI\\CURSO DE PLATZI\\HENRRY\\proyectos personales\\mini proyecto\\data\\sede.csv'
INTO TABLE sede
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n' IGNORE 1 ROWS ;

CREATE TABLE vendedor(
	idVendedor INT NOT NULL AUTO_INCREMENT,
    nombre VARCHAR (50),
    fechaNacimiento DATE ,
    Foto TEXT,
	PRIMARY KEY(idVendedor)
);
LOAD DATA INFILE 'D:\\CURSOS DE UNI\\CURSO DE PLATZI\\HENRRY\\proyectos personales\\mini proyecto\\data\\Vendedor.csv'
INTO TABLE vendedor
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n' IGNORE 1 ROWS ;

CREATE TABLE factura(
	idFactura INT NOT NULL ,
    idCalendario INT NOT NULL,
    idCanal INT NOT NULL ,
    idCliente INT NOT NULL,
    segmento VARCHAR(10),
    idVehiculo INT NOT NULL,
    costoVehiculo FLOAT,
    precioSinIgv  FLOAT ,
    igv FLOAT,
    idSede INT NOT NULL ,
    idVendedor INT NOT NULL,
    PRIMARY KEY(idFactura),
    FOREIGN KEY (idCalendario) REFERENCES calendarios(idCalendario),
    FOREIGN KEY (idCanal) REFERENCES canal(idCanal),
    FOREIGN KEY (idCliente) REFERENCES cliente(idCliente),
    FOREIGN KEY (idVehiculo) REFERENCES vehiculo(idVehiculo),
    FOREIGN KEY (idSede) REFERENCES sede(idSede),
    FOREIGN KEY (idVendedor) REFERENCES vendedor(idVendedor)
);

LOAD DATA INFILE 'D:\\CURSOS DE UNI\\CURSO DE PLATZI\\HENRRY\\proyectos personales\\mini proyecto\\data\\facturas.csv'
INTO TABLE factura
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n' IGNORE 1 ROWS;