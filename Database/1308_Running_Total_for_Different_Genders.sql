# Write your MySQL query statement below

with cte as (
select gender , day , sum(score_points) as total
from Scores
group by gender , day
)

select gender , day , 
        sum(total) over(partition by gender order by day) as total
from cte ;
