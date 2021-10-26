# Write your MySQL query statement below

select round(ifnull(count(distinct session_id) / count(distinct user_id),0),2)  as average_sessions_per_user
from Activity 
where activity_date between subdate("2019-07-27" , interval 29 day) and "2019-07-27" ;