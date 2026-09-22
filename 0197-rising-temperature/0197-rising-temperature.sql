# Write your MySQL query statement below
select t.id 
from weather t
join weather w
where datediff(t.recordDate,w.recordDate)=1 and t.temperature > w.temperature 