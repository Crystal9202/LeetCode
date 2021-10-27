# Write your MySQL query statement below

select round(sum(tiv_2016),2) as tiv_2016
from Insurance 
where tiv_2015 in

(select tiv_2015
from Insurance 
group by tiv_2015
having count(tiv_2015) >1)

and (lat,lon) not in 

(select lat ,lon
from Insurance
group by lat,lon
having count(lat) >1)  ;