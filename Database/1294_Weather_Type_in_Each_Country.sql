# Write your MySQL query statement below

select c.country_name , 
        (case when  avg(w.weather_state) <=15  then 'Cold'
             when    avg(w.weather_state) >=25  then 'Hot'
             else "Warm"  end  )  weather_type
from Countries as c  join Weather as w  on c.country_id = w.country_id  
where w.day between "2019-11-01" and "2019-11-30"
group by w.country_id  ;
