CREATE OR REPLACE VIEW olist_sales_view AS
SELECT 
    o.order_id,
    o.customer_id,
    c.customer_state,
    o.order_purchase_timestamp,
    pr.product_id,
    pr.product_category_name,
    oi.price AS product_price,
    oi.freight_value,
    op.payment_type,
    op.payment_value,
    orv.review_score
FROM olist.orders o
JOIN olist.order_items oi ON o.order_id = oi.order_id
JOIN olist.products pr ON oi.product_id = pr.product_id
JOIN olist.order_payments op ON o.order_id = op.order_id
JOIN olist.customers c ON o.customer_id = c.customer_id
LEFT JOIN olist.order_reviews orv ON o.order_id = orv.order_id;

select *
from olist_sales_view;

SELECT count(*)
FROM olist_sales_view osv
WHERE order_purchase_timestamp >= '2016-12-01'
  AND order_purchase_timestamp <  '2017-01-01';
