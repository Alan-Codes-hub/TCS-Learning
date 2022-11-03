class Asset():
    def __init__(self,asset_id,asset_holder_name,asset_type,asset_location,asset_price):
        self.asset_id=asset_id
        self.asset_holder_name=asset_holder_name
        self.asset_type=asset_type
        self.asset_location=asset_location
        self.asset_price=asset_price

class AssetManager():
    def __init__(self,manager_name,asset_list):
        self.manager_name=manager_name
        self.asset_list=asset_list
    
    def findAssetByPrice(self,price):
        temp=()
        lst=[]
        for i in self.asset_list:
            if i.asset_price<=price:
                
                temp=(i.asset_id,i.asset_holder_name,i.asset_price)
                
                lst.append(temp)
        return lst
    
    def findAssetSumByLocation(self,pincode):
        sum=0
        for j in self.asset_list:
            if j.asset_location[-6:]==pincode:
                sum+=j.asset_price
        return sum
        
if __name__=='__main__':
    asset_list=[]
    count=int(input())
    for c in range(count):
        asset_id=int(input())
        asset_holder_name=input()
        asset_type=input()
        asset_location=input()
        asset_price=int(input())
        obj=Asset(asset_id,asset_holder_name,asset_type,asset_location,asset_price)
        asset_list.append(obj)
    price=int(input())
    pincode=input()
    manager=AssetManager("Arun",asset_list)
    res1=manager.findAssetByPrice(price)
    res2=manager.findAssetSumByLocation(pincode)
    if len(res1)==0:
        print("No assets found for the given price")
    else:
        for k in res1:
            print(k[0],k[1],k[2])
    
    if res2==0:
        print("No assets found for the given pincode")
    else:
        print(pincode,res2)
    
    
    
    
            
            