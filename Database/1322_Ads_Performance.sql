# Write your MySQL query statement below

select  ad_id , 
        ifnull(round((sum(action = 'Clicked') /  ( sum(action = "Clicked") + sum(action = "Viewed")) )*100,2),0)  as ctr         
from Ads  
group by ad_id 
order by ctr desc , ad_id ;