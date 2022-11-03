class FoodItem():
    def __init__(self,id,name,category,price):
        self.item_id=id
        self.item_name=name
        self.item_category=category
        self.item_price=price
    
    def provideDiscount(self,Percentage):
        self.item_price-=self.item_price*Percentage/100
        
class Restauarant():
    def __init__(self,restaurant_name,fooditem_list):
        self.restaurant_name=restaurant_name
        self.fooditem_list=fooditem_list
        
    def retieveUpdatedPrice(self,item_id,Percentage):
        for food in fooditem_list:
            if food.item_id==item_id:
                food.provideDiscount(Percentage)
                return food
            
            
        return None


if __name__=='__main__':
    num=int(input())
    fooditem_list=[]
    for i in range(num):
        item_id=int(input())
        item_name=input()
        item_category=input()
        item_price=int(input())
        
        obj=FoodItem(item_id,item_name,item_category,item_price)
        fooditem_list.append(obj)
    
    
    
    item_id=int(input())
    Percentage=int(input())
    Rest=Restauarant("Restaurant1",fooditem_list)
    
    upd=Rest.retieveUpdatedPrice(item_id,Percentage)
    if upd==None:
        print("No food item exists matching the given criteria")
    else:
        print(upd.item_name,"-",upd.item_price)
    
                
                
                
        