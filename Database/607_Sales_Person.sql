#Write your MySQL query statement below

select s.name 
from salesperson as s 
where  s.name not in 

(select s.name 
from salesperson as s left join orders as o   on s.sales_id = o.sales_id  
                            join company as c  on o.com_id  = c.com_id 
 where c.name ="RED" 
)  ;