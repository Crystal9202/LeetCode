# Write your MySQL query statement below

select u.name , sum(t.amount) as balance
from Users as u  join Transactions as t    on u.account = t.account 
group by t.account
having sum(t.amount) > 10000  ;
