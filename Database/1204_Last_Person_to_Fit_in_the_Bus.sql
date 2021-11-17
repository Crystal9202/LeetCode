# Write your MySQL query statement below

select q1.person_name
from Queue as q1 join Queue as q2 on q1.turn >= q2.turn
group by q1.person_id
having sum(q2.weight) <=1000
order by sum(q2.weight) desc 
limit 1;