class employee():
    def __init__(self,emp_id,emp_name,emp_role,emp_salary):
        self.emp_id=emp_id
        self.emp_name=emp_name
        self.emp_role=emp_role
        self.emp_salary=emp_salary
    def increment_salary(self,num):
        self.emp_salary+=self.emp_salary*(num/100)

class Organisation():
    def __init__(self,org_name,emp_list):
        self.org_name=org_name
        self.emp_list=emp_list

    def calculate_salary(self,string_in,num):
        temp=[]
        for i in self.emp_list:
            if i.emp_role==string_in:
                i.increment_salary(num)
                temp.append(i)
        return temp

if __name__=='__main__':
    emp_list=[]
    count=int(input())
    for c in range(count):
        emp_id=int(input())
        emp_name=input()
        emp_role=input()
        emp_salary=int(input())
        obj=employee(emp_id,emp_name,emp_role,emp_salary)
        emp_list.append(obj)
    string_in=input()
    num=int(input())
    org_obj=Organisation("ABC",emp_list)
    output=org_obj.calculate_salary(string_in,num)
    for j in output:
        print(j.emp_name)
        print(j.emp_salary)
