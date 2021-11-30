# Write your MySQL query statement below

with cte as (
select caller_id as id  ,duration
from Calls 
union all
select callee_id as id , duration
from Calls 
)
select c1.name as country 
from cte as c join Person as p   on c.id = p.id 
              join Country as c1  on substring(p.phone_number, 1,3) = c1.country_code
              group by c1.name
              having avg(c.duration) > (select avg(duration)from Calls)   ;