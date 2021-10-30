# Write your MySQL query statement below

select   tab.student_id ,tab.student_name , tab.subject_name ,count(e.subject_name) as attended_exams 
from 
(select  st.student_id , st.student_name , su.subject_name
from Students as st  join Subjects as su) as tab  left  join Examinations as e  on tab.student_id = e.student_id and tab.subject_name = e.subject_name 
group by  tab.student_id ,tab.subject_name
order  by  tab.student_id ,tab.subject_name ;