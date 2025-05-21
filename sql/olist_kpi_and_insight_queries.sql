-- Top 5 products that appear most often in order_items

select product_id, COUNT(*) as appearances
from olist.order_items
GROUP BY product_id
order by appearances DESC
limit 5;

-- Avg. review score from order_reviews

select AVG(review_score)
from olist.order_reviews;

-- Top 5 States by # of Customers

select customer_state, COUNT(*) as "customer_count"
from olist.customers c
group by customer_state 
order by "customer_count" DESC
limit 5;

--Avg. review score per seller

select oi.seller_id, avg(orv.review_score) as avg_review_score
from olist.order_items oi
join olist.order_reviews orv on oi.order_id = orv.order_id
group by oi.seller_id;

--Distinct payment types

select distinct payment_type 
from olist.order_payments;