# Write your MySQL query statement below

(select u.name as results
from Users as u   join Movie_Rating as m  on u.user_id = m.user_id 
group by u.user_id 
order by count(*) desc ,u.name 
limit 1)

union 

(select m1.title as results 
from Movies as m1 join Movie_Rating as m2 on m1.movie_id = m2.movie_id
where m2.created_at between "2020-02-01" and "2020-02-29"
group by m1.movie_id
order by avg(m2.rating) desc ,m1.title
limit 1 );