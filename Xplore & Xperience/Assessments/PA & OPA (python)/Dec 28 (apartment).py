class Apartment():
    def __init__(self,flat_number, owner_name, electicitybillamount):
        self.flat_number=flat_number
        self.owner_name=owner_name
        self.electicitybillamount=electicitybillamount
        
class apartment_demo():
    def __init__(self):
        #p=0
        pass
    
    def getSecondMiniBill(self,apartment_list):
        self.apartment_list=apartment_list
        apartment_list.sort(key=lambda x:x.electicitybillamount,reverse=True)
        return apartment_list[1].electicitybillamount
        
if __name__=='__main__':
    apartment_list=[]
    count=int(input())
    for c in range(count):
        flat_number=int(input())
        owner_name=input()
        electicitybillamount=int(input())
        Apartment_obj=Apartment(flat_number, owner_name, electicitybillamount)
        apartment_list.append(Apartment_obj)
        
    demo_obj=apartment_demo()
    result=demo_obj.getSecondMiniBill(apartment_list)
    print(result)
        
