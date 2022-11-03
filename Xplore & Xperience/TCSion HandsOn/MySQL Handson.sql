handon 1 - Employee count in each Department


select Departments.deptName,count(*) as count

from Departments

inner join Employees on Employees.deptId = Departments.deptId

group by Departments.deptName;


handson 2 - Find Names of Employees


select ename from employees
where deptid = (select deptid from employees
where eid=108);

handson 3 - Find ordered items


select itemname from items
where itemid = (select itemid from orders
where orderid=4499);
