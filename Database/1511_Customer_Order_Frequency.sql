# Write your MySQL query statement below

select customer_id , name
from Customers as c 
where customer_id  in 

(select o.customer_id 
 from 
Orders as o  join Product as p  on o.product_id = p.product_id
where o.order_date between "2020-06-01"  and "2020-06-30"
group by o.customer_id 
having sum(o.quantity*p.price) >=100) 

and customer_id in 

(select o.customer_id 
 from
Orders as o  join Product as p  on o.product_id = p.product_id
where o.order_date between "2020-07-01"  and "2020-07-31"
group by o.customer_id 
having sum(o.quantity*p.price) >=100)  ;