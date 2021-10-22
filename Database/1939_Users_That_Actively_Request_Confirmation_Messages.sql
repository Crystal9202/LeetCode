# Write your MySQL query statement below

select  distinct c1.user_id 
from Confirmations as c1  join Confirmations as c2  on c1.user_id = c2.user_id 
and c2.time_stamp > c1.time_stamp  
where date_sub(c2.time_stamp ,interval 24 hour) <= c1.time_stamp ;