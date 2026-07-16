# Write your MySQL query statement below
select e.name, b.bonus from Employee e LEFT JOIN Bonus b on b.empID=E.empID where bonus is null or bonus <1000