# Write your MySQL query statement below

select max(num) as num
from my_numbers
where num not in 
(
select num
from my_numbers
group by num
having count(num) > 1
 ) ;