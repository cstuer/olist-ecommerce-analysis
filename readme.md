# Olist E-Commerce Analysis

This project analyzes the Brazilian Olist e-commerce dataset using SQL, Python, and Tableau. It covers raw data cleaning, relational schema design, querying for KPIs and insights, and visualizing trends in product sales, delivery performance, customer geography, and reviews.

## Project Structure

```
olist-ecommerce-analysis/
├── cleaned/                          
├── raw/                            
├── documentation/                  
├── images/                         
├── python/                          
├── sql/                              
├── readme.md                        
```

## Data

Folder: `raw/`

- Contains 9 original CSVs from the public Olist dataset:
  - `olist_customers_dataset.csv`
  - `olist_geolocation_dataset.csv`
  - `olist_order_items_dataset.csv`
  - `olist_order_payments_dataset.csv`
  - `olist_order_reviews_dataset.csv`
  - `olist_orders_dataset.csv`
  - `olist_products_dataset.csv`
  - `olist_sellers_dataset.csv`
  - `product_category_name_translation.csv`

Folder: `cleaned/`

- `olist_order_reviews_clean.csv`: Cleaned using Python to fix encoding issues, remove invalid rows, strip hidden characters, and drop duplicates

Folder: `documentation/`

- `brazilian_ecommerce_data_attributes.txt`: Lists all columns and inferred types for each table

## Python-Based Data Cleaning

Script: `csv_cleaner_advanced.py`

- Reads in messy review data
- Drops malformed rows based on comma count
- Fixes encoding (Latin-1 to UTF-8)
- Removes hidden characters
- Deduplicates `review_id`
- Outputs `olist_order_reviews_clean.csv`

## PostgreSQL Schema and Queries

Script: `create_olist_schema.sql`

- Creates 9 PostgreSQL tables to match the Olist dataset
- Defines primary and foreign key relationships
- Sets up `olist` schema

Script: `olist_sales_view.sql`

- Combines data from orders, products, payments, customers, and reviews
- View is used for simplified querying and Tableau connection

Script: `olist_kpi_and_insight_queries.sql`

- Provides exploratory insights:
  - Top products by order frequency
  - Average review scores (overall and per seller)
  - Customer counts by state
  - Payment types used

## Tableau Dashboard

File: `olist_ecommerce_data.twbx`

Includes:
- Summary KPIs: top categories, avg. review scores, payment breakdowns
- Product sales and shipping analysis
- Freight and delivery patterns
- Customer locations by state

Exported to PDF for quick viewing: `olist_ecommerce_data.pdf`

## Tools Used

- PostgreSQL: Data modeling and querying
- Python (pandas): Data cleaning and preprocessing
- Tableau: Data visualization and dashboard creation
- CSV: Original data input format

## Data Source

Brazilian Olist Public Dataset  
https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce

## Author

Cody Stuerman  
LinkedIn: https://www.linkedin.com/in/codystuerman  
GitHub: https://github.com/cstuer
