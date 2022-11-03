class Passenger():
    def __init__(self,passenger_id,passenger_name,gender,miles):
        self.passenger_id=passenger_id
        self.passenger_name=passenger_name
        self.gender=gender
        self.miles=miles

class Organisation():
    def __init__(self,name,passenger_list):
        self.name=name
        self.passenger_list=passenger_list

    def Discount(self,id_in,rate):
        for i in self.passenger_list:
            if i.passenger_id==id_in:
                discount=i.miles*(rate/100)
        return discount

if __name__=='__main__':
    passenger_list=[]
    count=int(input())
    for c in range(count):
        passenger_id=int(input())
        passenger_name=input()
        gender=input()
        miles=int(input())
        obj=Passenger(passenger_id,passenger_name,gender,miles)
        passenger_list.append(obj)
    org_obj=Organisation("ARK",passenger_list)
    id_in=int(input())
    rate=int(input())
    result=org_obj.Discount(id_in,rate)
    if result<0:
        print(f"no discount for the passenger {id_in}")
    else:
        print(f"Discount for the passenger {id_in} is {result}")
