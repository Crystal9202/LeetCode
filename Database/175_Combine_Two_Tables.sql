# Write your MySQL query statement below

select p.Firstname , p.Lastname , a.City ,a.State
from Person as p left join Address as a 
on p.PersonId = a.PersonId  ;