# Write your MySQL query statement below

select session_id
from playback p
left join ads a on a.customer_id = p.customer_id and a.timestamp between p.start_time and p.end_time
where a.customer_id is null ;