class Bill():
    def __init__(self,mob_number,payBill):
        self.mob_number=mob_number
        self.payBill=payBill

class Mobile():
    def __init__(self,serviceProvider,mob_number,dataUsed,paymentMethod):
        self.serviceProvider=serviceProvider
        self.mob_number=mob_number
        self.dataUsed=dataUsed
        self.paymentMethod=paymentMethod

    def calculateBil(self,obj_list):
        total=0
        due=0
        temp=[]
        #self.obj_list=obj_list
        for i in obj_list:
            if i.serviceProvider=='jio':
                total=i.dataUsed*10
            elif i.serviceProvider=='airtel' and i.paymentMethod=='paytm':
                total=i.dataUsed*9.9
            elif i.serviceProvider=='airtel' and i.paymentMethod!='paytm':
                total=i.dataUsed*11
            temp.append(Bill(i.mob_number,int(total)))
        return temp

if __name__=='__main__':
    obj_list=[]
    count=int(input())
    for c in range(count):
        serviceProvider=input()
        mob_number=int(input())
        dataUsed=int(input())
        paymentMethod=input()
        obj=Mobile(serviceProvider,mob_number,dataUsed,paymentMethod)
        obj_list.append(obj)
    demo=Mobile("",0,0,"")
    output=demo.calculateBil(obj_list)
    if len(output)==0:
        print("No data found")
    else:
        for j in output:
            print("(",j.mob_number,",",j.payBill,")")
