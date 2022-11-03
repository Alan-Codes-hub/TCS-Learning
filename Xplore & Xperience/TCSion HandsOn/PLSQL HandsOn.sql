Handson-1 Print Customer Details





declare
id Orders.C_ID%type;
i Customers.ID%type;
n Customers.Name%type;
cn Customers.Contact_No%type;
cursor o is select C_ID from Orders where QUANTITY >200; cursor c is select ID, Name, Contact_No from Customers;
begin
dbms_output.put_line('Customer_Id Customer_Name Customer_Phone');
open o;
loop
    fetch o into id;
    exit when o%notfound;
    open c;
    loop
        fetch c into i,n,cn;
        exit when c%notfound;
        if (i=id) then
        dbms_output.put_line(i||' '||n||' '||cn);
        end if;
    end loop;
    close c;
end loop;
close o;
end;
/





Handson -2 Find Total Score

​

​

declare
s Scores.Score%type;
cursor c is select sum(Score) from Scores where Score <100; begin
open c;
fetch c into s;
dbms_output.put_line('Total='||s);
close c;
end;
/





Handson – 3  Find Total Score





Same Answer of Handson-2

​

​

Handson – 4  Display employee grade based on employee salary

​

​

alter table Employees add Grade varchar(255);
update Employees
set Grade='Senior manager' where Salary>=30000;
update Employees
set Grade='Middle manager' where Salary<30000 and Salary>=25000;
update Employees
set Grade='Junior manager' where Salary<25000 and Salary>=20000;
update Employees
set  Grade='Team member' where Salary<20000;
select Name,Grade from Employees;
exit;

​

​

Handson – 5 List Department of se designated employees

​

declare
di Departments.Dept_ID%type;
dn Departments.Dept_Name%type;
cursor e is select distinct D_Id from Employees where Designation='SE';
ei Employees.D_Id%type;
cursor d is select Dept_ID, Dept_Name from Departments;
begin
open e;
loop
    fetch e into ei;
    exit when e%notfound;
    open d;
    loop
        fetch d into di,dn;
        exit when d%notfound;
        if(ei=di) then
        dbms_output.put_line(dn);
        end if;
    end loop;
    close d;
end loop;
close e;
end;
/
exit;

​
