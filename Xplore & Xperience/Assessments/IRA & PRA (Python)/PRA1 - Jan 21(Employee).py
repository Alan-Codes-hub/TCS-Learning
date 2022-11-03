class Employee():
    def __init__(self,employeeId,employeeName,status,ageInRole):
        self.employeeId=employeeId
        self.employeeName=employeeName
        self.status=status
        self.ageInRole=ageInRole

class Organization():
    def __init__(self,employeeList):
        self.employeeList=employeeList

    def updateEmployeeStatus(self,NoOfYears):
        for emp in self.employeeList:
            if emp.ageInRole>NoOfYears:
                emp.status="Retirement Due"

    def countEmployees(self):
        count=0
        for emp in self.employeeList:
            if emp.status=="Retirement Due":
                count+=1
        return count

if __name__=='__main__':
    employeeList=[]
    num=int(input())
    for c in range(num):
        employeeId=int(input())
        employeeName=input()
        ageInRole=int(input())
        Emp_obj=Employee(employeeId,employeeName,"In Service",ageInRole)
        employeeList.append(Emp_obj)
    NoOfYears=int(input())
    Org_obj=Organization(employeeList)
    Org_obj.updateEmployeeStatus(NoOfYears)
    count=Org_obj.countEmployees()
    if count==0:
        print("No employee updated.")
    else:
        print("Count of employee updated= ",count)
    for emp in employeeList:
        print(emp.employeeId,emp.employeeName,emp.status)
