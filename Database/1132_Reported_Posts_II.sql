select round(avg(perc)*100,2) as average_daily_percent
from
(select  a.action_date ,count(distinct r.post_id)/count(distinct a.post_id) as perc
from Actions as a left join Removals as r 
on a.post_id = r.post_id 
where action ='report' and extra= 'spam'
group by a.action_date
) as tab  ;
