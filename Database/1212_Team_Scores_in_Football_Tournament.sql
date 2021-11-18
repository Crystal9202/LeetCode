# Write your MySQL query statement below

with cte as 
(
select  host_team as team, host_goals as host , guest_goals as guest  
    from Matches 

union all
    
select  guest_team as team , guest_goals as host , host_goals as guest 
    from Matches
)

select  t.team_id  ,
        t.team_name ,
        sum(case when c.host > c.guest  then 3 
             when c.host = c.guest  then 1  
             else 0  end ) as num_points 
from Teams as t  left join cte as c   on t.team_id = c.team
group by t.team_id ,t.team_name 
order by num_points desc ,team_id ;