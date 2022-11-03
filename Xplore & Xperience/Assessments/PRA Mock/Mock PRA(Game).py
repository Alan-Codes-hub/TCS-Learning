class Game():
    def __init__(self,game_id,game_name,game_quantity,game_pricePerUnit):
        self.game_id=game_id
        self.game_name=game_name
        self.game_quantity=game_quantity
        self.game_pricePerUnit=game_pricePerUnit

    def apply_discount(self,percentage_in):
        if percentage_in>0:
            self.game_pricePerUnit=self.game_pricePerUnit-self.game_pricePerUnit*(percentage_in/100)
        elif percentage_in<=0:
            self.game_pricePerUnit=self.game_pricePerUnit

class Store():
    def __init__(self,store_name,game_list):
        self.store_name=store_name
        self.game_list=game_list

    def calculate_price(self,percentage_in,quantity_in):
        temp=[]
        for game in self.game_list:
            if game.game_quantity>=quantity_in:
                game.apply_discount(percentage_in)
                temp.append(game)
        temp.sort(key=lambda x:x.game_quantity*game_pricePerUnit,reverse=True)
        return temp

if __name__=='__main__':
    game_list=[]
    count=int(input())
    for c in range(count):
        game_id=int(input())
        game_name=input()
        game_quantity=int(input())
        game_pricePerUnit=int(input())
        game_obj=Game(game_id,game_name,game_quantity,game_pricePerUnit)
        game_list.append(game_obj)
    percentage_in=int(input())
    quantity_in=int(input())
    Store_obj=Store("GAMERS",game_list)
    result=Store_obj.calculate_price(percentage_in,quantity_in)
    if len(result)==0:
        print("No game found")
    else:
        for res in result:
            print(res.game_name,res.game_pricePerUnit*res.game_quantity)
