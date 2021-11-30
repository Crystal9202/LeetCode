# Write your MySQL query statement below

with cte as (
select company_id ,max(salary) as maxsal
from Salaries 
group by company_id)

select s.company_id ,s.employee_id ,s.employee_name ,
        round(case when c.maxsal < 1000  then s.salary
              when c.maxsal >=1000 and maxsal <=10000  then s.salary*0.76
              when c.maxsal >10000  then s.salary*0.51
              end)  as salary 
from Salaries as s join cte as c   on s.company_id = c.company_id  ;