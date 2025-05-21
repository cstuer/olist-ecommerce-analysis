-- Create schema 
CREATE SCHEMA IF NOT EXISTS olist;
SET search_path TO olist;

-- Create customers table
CREATE TABLE customers (
  customer_id VARCHAR PRIMARY KEY,
  customer_unique_id VARCHAR,
  customer_zip_code_prefix INTEGER,
  customer_city VARCHAR,
  customer_state VARCHAR(2)
);

-- Create geolocation table
CREATE TABLE geolocation (
  geolocation_zip_code_prefix INTEGER,
  geolocation_lat NUMERIC(10, 6),
  geolocation_lng NUMERIC(10, 6),
  geolocation_city VARCHAR,
  geolocation_state VARCHAR(2)
);

-- Create product category name translation table
CREATE TABLE product_category_name_translation (
  product_category_name VARCHAR PRIMARY KEY,
  product_category_name_english VARCHAR
);

-- Create products table
CREATE TABLE products (
  product_id VARCHAR PRIMARY KEY,
  product_category_name VARCHAR,
  product_name_lenght INTEGER,
  product_description_lenght INTEGER,
  product_photos_qty INTEGER,
  product_weight_g NUMERIC(10, 2),
  product_length_cm NUMERIC(10, 2),
  product_height_cm NUMERIC(10, 2),
  product_width_cm NUMERIC(10, 2),
  FOREIGN KEY (product_category_name) REFERENCES product_category_name_translation(product_category_name)
);

-- Create sellers table
CREATE TABLE sellers (
  seller_id VARCHAR PRIMARY KEY,
  seller_zip_code_prefix INTEGER,
  seller_city VARCHAR,
  seller_state VARCHAR(2)
);

-- Create orders table
CREATE TABLE orders (
  order_id VARCHAR PRIMARY KEY,
  customer_id VARCHAR,
  order_status VARCHAR,
  order_purchase_timestamp TIMESTAMP,
  order_approved_at TIMESTAMP,
  order_delivered_carrier_date TIMESTAMP,
  order_delivered_customer_date TIMESTAMP,
  order_estimated_delivery_date TIMESTAMP,
  FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

-- Create order_items table
CREATE TABLE order_items (
  order_id VARCHAR,
  order_item_id INTEGER,
  product_id VARCHAR,
  seller_id VARCHAR,
  shipping_limit_date TIMESTAMP,
  price NUMERIC(10, 2),
  freight_value NUMERIC(10, 2),
  FOREIGN KEY (order_id) REFERENCES orders(order_id),
  FOREIGN KEY (product_id) REFERENCES products(product_id),
  FOREIGN KEY (seller_id) REFERENCES sellers(seller_id)
);

-- Create order_payments table
CREATE TABLE order_payments (
  order_id VARCHAR,
  payment_sequential INTEGER,
  payment_type VARCHAR,
  payment_installments INTEGER,
  payment_value NUMERIC(10, 2),
  FOREIGN KEY (order_id) REFERENCES orders(order_id)
);

-- Create order_reviews table
CREATE TABLE order_reviews (
  review_id VARCHAR PRIMARY KEY,
  order_id VARCHAR,
  review_score INTEGER,
  review_comment_title TEXT,
  review_comment_message TEXT,
  review_creation_date DATE,
  review_answer_timestamp TIMESTAMP,
  FOREIGN KEY (order_id) REFERENCES orders(order_id)
);
