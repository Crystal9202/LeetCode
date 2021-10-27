# Write your MySQL query statement below

select d.dept_name , ifnull(count(s.student_id),0)  as student_number 
from Department as d left join Student as s   on d.dept_id =  s.dept_id
group by d.dept_id 
order by student_number desc , d.dept_name  ;