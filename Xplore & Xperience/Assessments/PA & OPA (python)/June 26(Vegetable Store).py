import string

class Vegetable():
    def __init__(self,veg_name,price,quantity):
        self.veg_name=veg_name
        self.price=price
        self.quantity=quantity
class Store():
    def __init__(self,storeName,Veg_list):
        self.storeName=storeName
        self.Veg_list=Veg_list
    def categorizeVegetablesAlphabetically(self):
        self.Veg_list.sort(key=lambda x:x.veg_name)
        a=list(string.ascii_lowercase)
        for i in a:
            temp=[]
            for j in self.Veg_list:
                if i==j.veg_name[0]:
                    temp.append(j.veg_name)
            if len(temp)>0:
                veg_dict[i]=tuple(temp)
        return veg_dict
    def filterVegetablesForPriceRange(self,min_price,max_price):
        for  f in self.Veg_list:
            if f.price>=min_price and f.price<=max_price:
                Veg_list_Price.append(f.veg_name)
        return sorted(Veg_list_Price)

if __name__=='__main__':
    Veg_list=[]
    veg_dict={}
    Veg_list_Price=[]
    count=int(input())
    for c in range(count):
        veg_name=input()
        price=float(input())
        quantity=int(input())
        obj=Vegetable(veg_name,price,quantity)
        Veg_list.append(obj)
    storeName=input()
    min_price=float(input())
    max_price=float(input())
    store_obj=Store(storeName,Veg_list)
    alpha_result=store_obj.categorizeVegetablesAlphabetically()
    price_result=store_obj.filterVegetablesForPriceRange(min_price,max_price)

    for key,value in sorted(alpha_result.items()):
        print(key)
        for v in value:
            print(v)

    print(min_price,"-",max_price)

    for s in price_result:
        print(s)


        
