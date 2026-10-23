CREATE DATABASE shop_db;

USE shop_db;

CREATE TABLE product(
id INT PRIMARY KEY AUTO_INCREMENT,
name VARCHAR(100),
category VARCHAR(50),
price DECIMAL(10,2),
quantity INT,
manufacturer VARCHAR(100)
);




