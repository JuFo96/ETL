DROP DATABASE IF EXISTS integrated_db;
CREATE DATABASE integrated_db;
USE integrated_db;

DROP TABLE IF EXISTS customers;
DROP TABLE IF EXISTS order_items;
DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS staffs;
DROP TABLE IF EXISTS stores;
DROP TABLE IF EXISTS brands;
DROP TABLE IF EXISTS categories;
DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS stocks;


CREATE TABLE customers (
    customer_id INT NOT NULL PRIMARY KEY,
    first_name VARCHAR(40),
    last_name VARCHAR(40),
    phone VARCHAR(40),
    email VARCHAR(40),
    street VARCHAR(40),
    city VARCHAR(100),
    state VARCHAR(100),
    zip_code INT
);


/*
NEEDS some sort of feature enginering for a new primary key column maybe transaction_id?
*/
CREATE TABLE order_items (
    order_id INT, 
    item_id INT,
    product_id INT,
    quantity INT,
    list_price DECIMAL(10, 2),
    discount DECIMAL(10,6) constraint check_discount check (discount between 0 and 1),
    PRIMARY KEY (order_id, item_id)
);

CREATE TABLE orders (
    order_id INT NOT NULL PRIMARY KEY,
    customer_id INT,
    order_status INT,
    order_date VARCHAR(255),
    required_date VARCHAR(255),
    shipped_date VARCHAR(255),
    store VARCHAR(255),
    staff_name VARCHAR(255)
);


CREATE TABLE staffs (
    staff_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(255),
    phone VARCHAR(50),
    active BOOLEAN,
    store_name VARCHAR(100),
    street VARCHAR(100),
    manager_id INT
);


CREATE TABLE stores (
    name VARCHAR(50) PRIMARY KEY,
    phone VARCHAR(50),
    email VARCHAR(255),
    street VARCHAR(100),
    city VARCHAR(100),
    state VARCHAR(100),
    zip_code INT
);

CREATE TABLE brands (
    brand_id INT NOT NULL PRIMARY KEY,
    brand_name VARCHAR(100)
);

CREATE TABLE categories (
    category_id INT NOT NULL PRIMARY KEY,
    category_name VARCHAR(100)
);


CREATE TABLE products (
    product_id INT NOT NULL PRIMARY KEY,
    product_name VARCHAR(100),
    brand_id INT, 
    category_id INT, 
    model_year INT,
    list_price DECIMAL(10,2) 
);


CREATE TABLE stocks (
    stock_id INT AUTO_INCREMENT PRIMARY KEY,
    store_name VARCHAR(100),
    product_id INT, 
    quantity INT
);


ALTER TABLE order_items ADD CONSTRAINT FK_order_items_products FOREIGN KEY (product_id) REFERENCES products(product_id);
ALTER TABLE order_items ADD CONSTRAINT FK_order_items_orders FOREIGN KEY (order_id) REFERENCES orders(order_id);

ALTER TABLE orders ADD CONSTRAINT FK_orders_customers FOREIGN KEY (customer_id) REFERENCES customers(customer_id);
ALTER TABLE orders ADD CONSTRAINT FK_orders_store FOREIGN KEY (store) REFERENCES stores(name);

ALTER TABLE products ADD CONSTRAINT FK_products_brands FOREIGN KEY (brand_id) REFERENCES brands(brand_id);
ALTER TABLE products ADD CONSTRAINT FK_products_categories FOREIGN KEY (category_id) REFERENCES categories(category_id);

ALTER TABLE stocks ADD CONSTRAINT FK_stocks_products FOREIGN KEY (product_id) REFERENCES products(product_id);
ALTER TABLE stocks ADD CONSTRAINT FK_stocks_stores FOREIGN KEY (store_name) REFERENCES stores(name); 

