# Write your MySQL query statement below

select distinct  c2.seat_id 
from cinema as c1  join cinema as c2  
on abs(c2.seat_id - c1.seat_id)  = 1 
where c1.free = 1 and c2.free= 1  ;