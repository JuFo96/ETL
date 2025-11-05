CREATE TABLE customers (
    customer_id INT NOT NULL PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    phone VARCHAR(255),
    email VARCHAR(255),
    street VARCHAR(255),
    city VARCHAR(255),
    state VARCHAR(255),
    zip_code INT
);


CREATE TABLE order_items (
    transaction_id serial PRIMARY KEY,
    order_id INT, 
    item_id INT,
    product_id INT,
    quantity INT,
    list_price DECIMAL(10, 2),
    discount DECIMAL(10, 6) constraint check_discount check (discount between 0 and 1)
);

CREATE TABLE orders (
    order_id INT NOT NULL PRIMARY KEY,
    customer_id INT,
    order_status INT,
    order_date DATE,
    required_date DATE,
    shipped_date DATE,
    store_id INT,
    staff_name VARCHAR(255)
);


CREATE TABLE staffs (
    staff_id serial PRIMARY KEY,
    name VARCHAR(255),
    last_name VARCHAR(255),
    email VARCHAR(255),
    phone VARCHAR(255),
    active INT,
    store_id INT,
    manager_id real
);


CREATE TABLE stores (
    store_id INT NOT NULL PRIMARY KEY,
    name VARCHAR(255),
    phone VARCHAR(255),
    email VARCHAR(255),
    street VARCHAR(255),
    city VARCHAR(255),
    state VARCHAR(255),
    zip_code INT
);

CREATE TABLE brands (
    brand_id INT NOT NULL PRIMARY KEY,
    brand_name VARCHAR(255)
);

CREATE TABLE categories (
    category_id INT NOT NULL PRIMARY KEY,
    category_name VARCHAR(255)
);


CREATE TABLE products (
    product_id INT NOT NULL PRIMARY KEY,
    product_name VARCHAR(255),
    brand_id INT, 
    category_id INT, 
    model_year INT,
    list_price DECIMAL(10,2) 
);


CREATE TABLE stocks (
    stock_id serial PRIMARY KEY,
    store_id INT,
    product_id INT, 
    quantity INT
);


ALTER TABLE order_items
    ADD CONSTRAINT fk_order_items_products
        FOREIGN KEY (product_id) REFERENCES products (product_id)
        ON DELETE CASCADE;

ALTER TABLE order_items
    ADD CONSTRAINT fk_order_items_orders
        FOREIGN KEY (order_id) REFERENCES orders (order_id)
        ON DELETE CASCADE;

ALTER TABLE orders
    ADD CONSTRAINT fk_orders_customers
        FOREIGN KEY (customer_id) REFERENCES customers (customer_id)
        ON DELETE CASCADE;

ALTER TABLE orders
    ADD CONSTRAINT fk_orders_stores
        FOREIGN KEY (store_id) REFERENCES stores (store_id)
        ON DELETE CASCADE;

ALTER TABLE products
    ADD CONSTRAINT fk_products_brands
        FOREIGN KEY (brand_id) REFERENCES brands (brand_id)
        ON DELETE CASCADE;

ALTER TABLE products
    ADD CONSTRAINT fk_products_categories
        FOREIGN KEY (category_id) REFERENCES categories (category_id)
        ON DELETE CASCADE;

ALTER TABLE stocks
    ADD CONSTRAINT fk_stocks_products
        FOREIGN KEY (product_id) REFERENCES products (product_id)
        ON DELETE CASCADE;

ALTER TABLE stocks
    ADD CONSTRAINT fk_stocks_stores
        FOREIGN KEY (store_id) REFERENCES stores (store_id)
        ON DELETE CASCADE;

ALTER TABLE staffs
    ADD CONSTRAINT fk_staffs_stores
        FOREIGN KEY (store_id) REFERENCES stores (store_id)
        ON DELETE CASCADE;

