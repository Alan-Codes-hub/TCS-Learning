Hands On 1

select D.deptName,count(E.eId) from Departments D left join Employees E on D.deptId=E.deptId group by (D.deptName) order by count(E.eId) desc;

Hands On 2

select Dept_Id,Dept_Name from Department where Dept_Location='Ground Floor';

Hands On 3

select distinct Dept_name from Departments,Employees where Departments.Dept_Id=Employees.Emp_Dept_Id and Dept_name not in (select distinct Dept_name from Departments,Employees where Departments.Dept_Id=Employees.Emp_Dept_Id and Emp_skill like 'Programmer');

Hands On 4

select distinct Dept_name,Emp_skill from Departments,Employees where Dept_ID=Emp_Dept_Id order by Dept_Name desc,Emp_Skill;

Hands On 5

select distinct Item_Name from Items where Item_id not in(select distinct Item_Id from orders);

​
