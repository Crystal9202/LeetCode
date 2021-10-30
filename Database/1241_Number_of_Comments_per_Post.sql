# Write your MySQL query statement below

select   tab.sub_id  as post_id   ,  count(distinct s.sub_id)  as number_of_comments
from
(select sub_id
from Submissions 
where parent_id is null) as tab  left join Submissions as s   on tab.sub_id =  s.parent_id   
group by tab.sub_id ;