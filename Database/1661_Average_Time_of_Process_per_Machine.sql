# Write your MySQL query statement below

select    machine_id , round(avg(diff),3)  as processing_time 
from(
select machine_id , sum(case when activity_type = 'end'  then timestamp  else -timestamp   end  ) as diff
from Activity 
group by machine_id , process_id) as tab   
group by  machine_id ;