class employee():
    def __init__(self,emp_no,emp_name,leaves):
        self.emp_no=emp_no
        self.emp_name=emp_name
        self.leaves=leaves

class Company():
    def __init__(self,cname,emps):
        self.cname=cname
        self.emps=emps

    def leave_available(self,emp_no_in,leave_type):
        for i in self.emps:
            if i.emp_no==emp_no_in:
                return i.leaves[leave_type]

    def leave_permission(self,emp_no_in,leave_type,leave_num):
        lv=self.leave_available(emp_no_in,leave_type)
        if leave_num>=lv:
            return print(lv,"\n","Rejected")
        elif leave_num<=lv:
            return print(lv,"\n","Granted")

if __name__=='__main__':
    emps=[]
    leaves={}
    count=int(input())
    for c in range(count):
        emp_no=int(input())
        emp_name=input()
        leaves["A"]=int(input())
        leaves["B"]=int(input())
        leaves["C"]=int(input())
        obj=employee(emp_no,emp_name,leaves)
        emps.append(obj)
    emp_no_in=int(input())
    leave_type=input()
    leave_num=int(input())

    company_obj=Company("ARK",emps)
    company_obj.leave_permission(emp_no_in,leave_type,leave_num)
