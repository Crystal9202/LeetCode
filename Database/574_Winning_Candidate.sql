# Write your MySQL query statement below

select c.name
from Candidate as c   join Vote as v   on c.id = v.candidateId   
group by v.candidateId 
order by count(v.id) desc
limit 1 ; 