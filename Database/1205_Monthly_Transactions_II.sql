with cte as 

(select id , country ,state ,amount , trans_date 
from  Transactions

union

select c.trans_id as id , t.country ,'chargeback' as state , t.amount ,c.trans_date 
from Chargebacks as c left join Transactions as t   on c.trans_id = t.id
)

select date_format(trans_date ,'%Y-%m') as month ,
       country ,
       sum(state ='approved') as approved_count ,
       sum(case when state='approved'  then amount else 0 end ) as   approved_amount ,
       sum(state='chargeback') as chargeback_count ,
       sum(case when state='chargeback'  then amount  else  0  end) as chargeback_amount 
from cte 
group by month ,country  
having approved_count >0 or approved_amount >0 or chargeback_count >0 or chargeback_amount  >0  ;