# Write your MySQL query statement below

select e1.business_id
from Events as e1 join 
(select event_type ,avg(occurences) as avgoc
from Events
group by event_type) as e2  on e1.event_type = e2.event_type
where e1.occurences > e2.avgoc
group by e1.business_id 
having count(e1.event_type) > 1 ;