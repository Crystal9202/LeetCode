# Write your MySQL query statement below

select  f1.follower , count(distinct f2.follower) as num 
from Follow as f1  join Follow as f2  on f1.follower = f2.followee 
group by f1.follower 
order by f1.follower ;