class Stock():
    def __init__(self,StockName,StockSector,StockValue):
        self.StockName=StockName
        self.StockSector=StockSector
        self.StockValue=StockValue

class StockDemo():
    def __init__(self):
        m=0
    def getStockList(self,stock_list,sector_in):
        lst=[]
        self.stock_list=stock_list
        self.sector_in=sector_in
        for i in self.stock_list:
            if i.StockSector==self.sector_in and i.StockValue>500:
                lst.append(i)
        return lst
if __name__=='__main__':
    stock_list=[]
    count=int(input())
    for c in range(count):
        StockName=input()
        StockSector=input()
        StockValue=int(input())
        
        stock_obj=Stock(StockName,StockSector,StockValue)
        stock_list.append(stock_obj)
    
    sector_in=input()    
    demo_obj=StockDemo()
    result=demo_obj.getStockList(stock_list,sector_in)
    if len(result)!=0:
        for j in result:
            print(j.StockName)
    else:
        print("No records found")