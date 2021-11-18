# Write your MySQL query statement below

with cte as 
(select  user2_id as friends 
from Friendship
where user1_id = 1

union all 

select user1_id as friends 
from Friendship 
where user2_id = 1) 

select distinct l.page_id as recommended_page 
from cte as c join Likes as l on c.friends = l.user_id 
where l.page_id  not in (select  page_id  from Likes where user_id = 1)  ;