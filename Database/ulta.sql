/*
Database for Ulta warehouse
*/

PRAGMA foreign_keys = ON;

DROP TABLE IF EXISTS order_item;
DROP TABLE IF EXISTS inventory;
DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS product;
DROP TABLE IF EXISTS customers;

-- Customers Table
CREATE TABLE customers (
    customer_id INTEGER PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT,
    phone TEXT
);

-- Product Table
CREATE TABLE product (
    product_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    brand TEXT,
    price REAL NOT NULL CHECK (price >= 0),
    category TEXT NOT NULL
);

-- Orders Table
CREATE TABLE orders (
    order_id INTEGER PRIMARY KEY,
    customer_id INTEGER NOT NULL,
    order_date TEXT NOT NULL,
    status TEXT NOT NULL,
    FOREIGN KEY (customer_id)
        REFERENCES customers(customer_id)
);

-- Inventory Table
CREATE TABLE inventory (
    inventory_id INTEGER PRIMARY KEY,
    product_id INTEGER NOT NULL,
    quantity_available INTEGER NOT NULL,
    location TEXT NOT NULL,
    FOREIGN KEY (product_id)
        REFERENCES product(product_id)
);

-- Order Item Table
CREATE TABLE order_item (
    order_item_id INTEGER PRIMARY KEY,
    order_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL CHECK (quantity > 0),
    unit_price REAL NOT NULL,
    FOREIGN KEY (order_id)
        REFERENCES orders(order_id),
    FOREIGN KEY (product_id)
        REFERENCES product(product_id)
);

-- Sample Data: Customers
INSERT INTO customers
(customer_id, first_name, last_name, email, phone)
VALUES
(1, 'Ava', 'Thompson', 'ava.thompson@gmail.com', '317-555-1023'),
(2, 'Liam', 'Rodriguez', 'liam.rodriguez@gmail.com', '317-555-2045'),
(3, 'Sophia', 'Nguyen', 'sophia.nguyen@gmail.com', '317-555-3098'),
(4, 'Noah', 'Patel', 'noah.patel@gmail.com', '317-555-4127'),
(5, 'Emma', 'Johnson', 'emma.johnson@gmail.com', '317-555-5239');

-- Sample Data: Products
INSERT INTO product
(product_id, name, brand, price, category)
VALUES
(1, 'Hydrating Shampoo', 'Redken', 24.99, 'Haircare'),
(2, 'Volumizing Conditioner', 'Biolage', 22.99, 'Haircare'),
(3, 'Matte Lipstick', 'MAC', 19.99, 'Makeup'),
(4, 'Liquid Foundation', 'Fenty Beauty', 36.00, 'Makeup'),
(5, 'Vitamin C Serum', 'The Ordinary', 14.99, 'Skincare');

-- Sample Data: Orders
INSERT INTO orders
(order_id, customer_id, order_date, status)
VALUES
(1, 1, '2026-10-01', 'Delivered'),
(2, 2, '2026-10-02', 'Processing'),
(3, 3, '2026-10-03', 'Delivered'),
(4, 4, '2026-10-04', 'Shipped'),
(5, 5, '2026-10-05', 'Processing');

-- Sample Data: Inventory
INSERT INTO inventory
(inventory_id, product_id, quantity_available, location)
VALUES
(1, 1, 50, 'Indianapolis Warehouse'),
(2, 2, 40, 'Indianapolis Warehouse'),
(3, 3, 35, 'Chicago Warehouse'),
(4, 4, 25, 'Chicago Warehouse'),
(5, 5, 60, 'Indianapolis Warehouse');

-- Sample Data: Order Items
INSERT INTO order_item
(order_item_id, order_id, product_id, quantity, unit_price)
VALUES
(1, 1, 1, 2, 24.99),
(2, 2, 3, 1, 19.99),
(3, 3, 5, 2, 14.99),
(4, 4, 4, 1, 36.00),
(5, 5, 2, 3, 22.99);