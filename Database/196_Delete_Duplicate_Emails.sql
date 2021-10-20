# Write your MySQL query statement below

delete p2
from Person as p1  join Person as p2 on p1.Email  = p2.Email and p1.Id < p2.Id ; 