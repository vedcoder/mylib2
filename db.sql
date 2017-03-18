CREATE DATABASE mylib;

USE mylib;

CREATE TABLE users (id INT NOT NULL AUTO_INCREMENT,
	firstname VARCHAR(50) NOT NULL, lastname VARCHAR(400) NOT NULL,
    email VARCHAR(120) NOT NULL, pwdhash VARCHAR(180) NOT NULL,
    primary key (id)
    );

CREATE TABLE books (id INT NOT NULL AUTO_INCREMENT,
	name VARCHAR(50) NOT NULL, author VARCHAR(50) NOT NULL,
    story VARCHAR(100) NOT NULL, link VARCHAR(400) NOT NULL,
    price DECIMAL(5,2) NOT NULL,
    primary key (id)
    );
CREATE TABLE toys (id INT NOT NULL AUTO_INCREMENT,
	name VARCHAR(50) NOT NULL, brand VARCHAR(50) NOT NULL,
		description VARCHAR(500) NOT NULL, link VARCHAR(400) NOT NULL,
		price DECIMAL(5,2) NOT NULL,
		primary key (id)
		);
