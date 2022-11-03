class HouseForSale():
    def __init__(self,HouseNumber,HouseType,SalePrice,AreaInSqft,isFurnished):
        self.HouseNumber=HouseNumber
        self.HouseType=HouseType
        self.SalePrice=SalePrice
        self.AreaInSqft=AreaInSqft
        self.isFurnished=isFurnished

    def calculateNewPrice(self,new_rate):
        if self.isFurnished.lower()=="semi furnished":
            self.SalePrice=self.AreaInSqft*new_rate+self.AreaInSqft*new_rate*0.1
        elif self.isFurnished.lower()=="fully furnished":
            self.SalePrice=self.AreaInSqft*new_rate+self.AreaInSqft*new_rate*0.2

class Realtor():
    def __init__(self,realtorId,newRate,HouseList):
        self.realtorId=realtorId
        self.newRate=newRate
        self.HouseList=HouseList
    def getAvailableHouses(self,SalePrice_in,HouseType_in):
        temp=[]
        for house in self.HouseList:
            house.calculateNewPrice(newRate)
        for house in self.HouseList:
            if house.HouseType.lower()==HouseType_in.lower():
                if house.SalePrice<=SalePrice_in:
                    temp.append(house)
        return temp

if __name__=='__main__':
    HouseList=[]
    count=int(input())
    for c in range(count):
        HouseNumber=int(input())
        HouseType=input()
        SalePrice=int(input())
        AreaInSqft=int(input())
        isFurnished=input()
        House_obj=HouseForSale(HouseNumber,HouseType,SalePrice,AreaInSqft,isFurnished)
        HouseList.append(House_obj)
    newRate=float(input())
    HouseType_in=input()
    SalePrice_in=int(input())
    Realtor_obj=Realtor(45,newRate,HouseList)
    new_list=Realtor_obj.getAvailableHouses(SalePrice_in,HouseType_in)
    if len(new_list)==0:
        print("Preffered House Not Available")
    else:
        for house in new_list:
            print(house.HouseNumber,house.HouseType,house.AreaInSqft,house.SalePrice)
