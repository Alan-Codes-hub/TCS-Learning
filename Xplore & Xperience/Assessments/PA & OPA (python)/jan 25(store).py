class Item():
    def __init__(self,item_id,item_name,item_price,quantity_available):
        self.item_id=item_id
        self.item_name=item_name
        self.item_price=item_price
        self.quantity_available=quantity_available

    def calculate_price(self,quantity_in):
        price=0
        #self.quantity_in=quantity_in
        if quantity_in>=self.quantity_available:
            price=quantity_in*self.item_price
        return price

class Store():
    def __init__(self,item_list):
        self.item_list=item_list

    def generate_bill(self,item_dict):
        total=0
        #self.item_dict=item_dict
        for k,v in item_dict.items():
            for i in self.item_list:
                if i.item_name==k:
                    total+=i.calculate_price(v)
        return total

if __name__=='__main__':
    item_list=[]
    item_dict={}
    num=int(input())
    for c in range(num):
        item_id=int(input())
        item_name=input()
        item_price=int(input())
        quantity_available=int(input())
        item_obj=Item(item_id,item_name,item_price,quantity_available)
        item_list.append(item_obj)
    num_dic=int(input())
    for n in range(num_dic):
        item_name_n=input()
        quantity_n=int(input())
        item_dict[item_name_n]=quantity_n

    demo_obj=Store(item_list)
    result=demo_obj.generate_bill(item_dict)
    print(result)
