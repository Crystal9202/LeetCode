# Write your MySQL query statement below

select w2.id
from Weather as w1  join Weather as w2 on adddate(w1.RecordDate ,interval 1 day)  = w2.RecordDate
where w2.Temperature > w1.Temperature ;