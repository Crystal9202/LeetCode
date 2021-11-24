# Write your MySQL query statement below

select i.invoice_id ,c.customer_name , i.price ,
     count(c1.user_id ) as contacts_cnt ,
     sum(case when c1.contact_name in (select customer_name from Customers)  then 1  else 0  end) as trusted_contacts_cnt
from  Invoices as i  left join Customers as c   on i.user_id = c.customer_id
                     left join Contacts as c1  on i.user_id = c1.user_id      
group by i.invoice_id
order by i.invoice_id ;