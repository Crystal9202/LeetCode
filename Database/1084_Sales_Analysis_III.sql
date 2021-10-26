# Write your MySQL query statement below

select p.product_id ,p.product_name
from Product as p join Sales as s   on p.product_id = s.product_id 
where p.product_id not in 
(
    select  product_id
    from Sales 
    where sale_date < "2019-01-01"  or sale_date > "2019-03-31" 
)
group by p.product_id  ;