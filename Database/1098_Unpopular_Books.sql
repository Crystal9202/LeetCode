# Write your MySQL query statement below

select b.book_id , b.name 
from Books as b  left join Orders as o  on b.book_id = o.book_id 
where b.available_from <= "2019-05-23"
group by b.book_id
having sum(case when o.dispatch_date between "2018-06-23" and "2019-06-23" then quantity else 0 end) < 10 ;