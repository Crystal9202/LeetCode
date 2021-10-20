# Write your MySQL query statement below

select E1.Name as Employee 
from Employee as e1  join Employee as e2 on e1.ManagerId = e2.Id 
where e1.Salary > e2.Salary ;