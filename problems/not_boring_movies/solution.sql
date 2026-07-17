# Write your MySQL query statement below
select * FROM Cinema WHERE id%2<>0 and description!='boring' ORDER BY rating DESC;