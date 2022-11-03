class Passenger():
    def __init__(self,pass_id,pass_name,pass_gender,pass_miles):
        self.pass_id=pass_id
        self.pass_name=pass_name
        self.pass_gender=pass_gender
        self.pass_miles=pass_miles
    
    def Discount(self,rate):
        discount=self.pass_miles*(rate/100)
        return discount
        
class Organizaion():
    def __init__(self,Org_name,Pass_list):
        self.Org_name=Org_name
        self.Pass_list=Pass_list
    
    def Calculate_Discount(self,ID_in,rate):
        lst=[]
        for passenger in self.Pass_list:
            if passenger.pass_id==ID_in:
                result=passenger.Discount(rate)
                lst.append(passenger.pass_id)
                lst.append(result)
        return lst
        
if __name__=='__main__':
    Pass_list=[]
    count=int(input())
    for i in range(count):
        pass_id=input()
        pass_name=input()
        pass_gender=input()
        pass_miles=int(input())
        pass_obj=Passenger(pass_id,pass_name,pass_gender,pass_miles)
        Pass_list.append(pass_obj)
            
    ID_in=input()
    rate=int(input())
    Org_Obj=Organizaion("ABC",Pass_list)
    res=Org_Obj.Calculate_Discount(ID_in,rate)
    print("Discount of the passenger with id {} is: {}".format(res[0],res[1]))
    
                
                
                
                
                
                
                