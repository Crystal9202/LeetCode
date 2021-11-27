# Write your MySQL query statement below

select distinct l.id ,  a.name
from Logins as l  join Accounts as a  on l.id = a.id
 where (a.id,adddate(l.login_date ,interval 1 day)) in(select id,login_date from Logins) and
       (a.id,adddate(l.login_date ,interval 2 day)) in(select id,login_date from Logins) and
       (a.id,adddate(l.login_date ,interval 3 day)) in(select id,login_date from Logins) and
       (a.id,adddate(l.login_date ,interval 4 day)) in(select id,login_date from Logins)
order by l.id ;