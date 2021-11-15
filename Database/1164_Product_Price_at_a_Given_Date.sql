# Write your MySQL query statement below

select  distinct p.product_id , 
        (case when tab.maxDate is not null then p.new_price  else 10 end)  as price
from Products as p left join 

                                (select product_id , max(change_date) as maxDate
                                from Products 
                                where change_date <= '2019-08-16'
                                group by product_id )  as tab  on p.product_id = tab.product_id 
                                where p.change_date = tab.maxDate or tab.maxDate is null  ;
