# Write your MySQL query statement below

select min(round(sqrt(power(p2.y-p1.y,2) + power(p2.x - p1.x,2)),2))  as shortest 
from Point2D as p1   join Point2D as p2  
 on p1.x != p2.x or p1.y != p2.y  ;