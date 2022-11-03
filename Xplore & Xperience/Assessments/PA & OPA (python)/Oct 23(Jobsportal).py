class Job():
    def __init__(self,job_id,company,job_role,start_salary,high_salary):
        self.job_id=job_id
        self.company=company
        self.job_role=job_role
        self.start_salary=start_salary
        self.high_salary=high_salary

class Jobsportal():
    def __init__(self,portal_name,job_list):
        self.portal_name=portal_name
        self.job_list=job_list
    
    def get_bestjobbyrole(self,jobb_role):
        self.jobb_role=jobb_role
        
        for i in job_list:
            if self.jobb_role.lower()==i.job_role.lower():
                max_salary.append(i.start_salary)
            
        if len(max_salary)!=0:
            maximum=max(max_salary)
            for h in job_list:
                if h.start_salary==maximum:
                    bestjobby_role.append(h)
           
        return bestjobby_role
            
        
    def jobswithsalary(self,salary):
        self.salary=salary
        for j in job_list:
            if self.salary>=j.start_salary and self.salary<=j.high_salary:
                job_dict[j.job_id]=j.company
           
        return job_dict

if __name__=='__main__':
    job_list=[]
    bestjobby_role=[]
    max_salary=[]
    job_dict={}
    
    count=int(input())
    for k in range(count):
        job_id=int(input())
        company=input()
        job_role=input()
        start_salary=int(input())
        high_salary=int(input())
        obj=Job(job_id,company,job_role,start_salary,high_salary)
        job_list.append(obj)
    jobb_role=input()
    salary=int(input())
    Portal=Jobsportal("ABC",job_list)
    role_result=Portal.get_bestjobbyrole(jobb_role)
    salary_result=Portal.jobswithsalary(salary)
    if len(role_result)==0:
        print("No jobs found for the given role")
    else:
        for s in role_result:
            print(s.job_id," ",s.company," ",s.start_salary)
        
    if len(salary_result)==0:
        print("No jobs matching the given salary")
    else:
        for k in sorted(salary_result):
            print(k," ",salary_result[k])
        
    