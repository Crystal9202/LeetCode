# Write your MySQL query statement below

with cte as 
(
select customer_id ,min(order_date) as minDay
from Delivery
group by customer_id)
select  round(sum(d.order_date=d.customer_pref_delivery_date) /count( c.minDay)*100,2) as immediate_percentage
from cte as c join Delivery as d   on c.customer_id = d.customer_id  and c.minDay=d.order_date  ;
             