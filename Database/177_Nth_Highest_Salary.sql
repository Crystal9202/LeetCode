CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN 

  RETURN (
      # Write your MySQL query statement below.  
      select  distinct salary
      from 
      (select dense_rank() over( order by salary desc ) as num ,salary
      from Employee) as tab
      where tab.num = n        
  );
END