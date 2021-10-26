# Write your MySQL query statement below

select  round(count(tab.player_id) / (select count(distinct player_id)  from Activity),2)  as  fraction
from 
(select player_id ,min(event_date) as minDay 
from Activity
group by player_id ) as tab  join Activity as a on tab.player_id = a.player_id  and tab.minDay +1 = a.event_date ;