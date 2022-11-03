class Payslip():
    def __init__(self,basicSalary,hra,ita):
        self.basicSalary=basicSalary
        self.hra=hra
        self.ita=ita
        
class PayslipDemo():
    def __init__(self):
        maxp=0
        
    def getHighestPF(self,obj_list):
        lst=[]
        self.obj_list=obj_list
        for i in self.obj_list:
            PF=i.basicSalary*(12/100)
            lst.append(PF)
        return max(lst)
        
if __name__=='__main__':
    obj_list=[]
    count=int(input())
    for c in range(count):
        basicSalary=int(input())
        hra=int(input())
        ita=int(input())
        obj=Payslip(basicSalary,hra,ita)
        obj_list.append(obj)
    
    demo_obj=PayslipDemo()
    pf_res=demo_obj.getHighestPF(obj_list)
    print(pf_res)
    
    