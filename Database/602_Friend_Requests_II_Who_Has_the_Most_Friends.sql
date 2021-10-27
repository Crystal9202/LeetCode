# Write your MySQL query statement below

with cte as 
(select requester_id as id  ,accept_date
from RequestAccepted
union all
select accepter_id as id  ,accept_date
from RequestAccepted)
 
select id , count(id) as num
from cte 
group by id 
order by count(id) desc
limit 1 ;
