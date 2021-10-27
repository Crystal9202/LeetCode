# Write your MySQL query statement below

select round(count(delivery_id) /  (select count(delivery_id) from Delivery)*100,2) as immediate_percentage
from Delivery 
where order_date = customer_pref_delivery_date ;