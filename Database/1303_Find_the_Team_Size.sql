# Write your MySQL query statement below

select  e.employee_id  ,  tab.num as team_size
from 
(select team_id,count(employee_id) as num 
from Employee as e 
group by team_id ) as tab  join Employee as e   on tab.team_id = e.team_id  ;