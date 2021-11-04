# Write your MySQL query statement below

select minDay as login_date , count(user_id) as user_count
from 
(
select user_id , min(activity_date) as minDay
from Traffic 
where activity = 'login'
group by user_id ) as tab
where datediff("2019-06-30" , minDay) <= 90  
group by minDay  ;