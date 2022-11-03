class RTVProduct():
    def __init__(self,sku_nbr,quantity,return_Reason,ship_To_Rlc_Flg,rtv_stat_code):
        self.sku_nbr=sku_nbr
        self.quantity=quantity
        self.return_Reason=return_Reason
        self.ship_To_Rlc_Flg=ship_To_Rlc_Flg
        self.rtv_stat_code=rtv_stat_code

    def assign_status(self):
        if self.return_Reason.lower()=="manufacturer defect" or self.return_Reason.lower()=="repair":
            if ship_To_Rlc_Flg=="True":
                self.rtv_stat_code=100
        else:
            self.rtv_stat_code=500
class Store():
    def __init__(self,rtv_list):
        self.rtv_list=rtv_list

    def fetchRtvProduct(self,quant):
        temp=[]
        diction={}
        for product in self.rtv_list:
            product.assign_status()
        for product in self.rtv_list:
            if product.rtv_stat_code==500 and product.quantity>quant:
                temp.append(product)
        temp.sort(key=lambda x:x.quantity,reverse=True)
        if len(temp)!=0:
            diction[temp[0].sku_nbr]=temp[0]
        return diction

if __name__=='__main__':
    rtv_list=[]
    count=int(input())
    for c in range(count):
        sku_nbr=int(input())
        quantity=int(input())
        return_Reason=input()
        ship_To_Rlc_Flg=input()
        RTVProduct_obj=RTVProduct(sku_nbr,quantity,return_Reason,ship_To_Rlc_Flg,None)
        rtv_list.append(RTVProduct_obj)
    quant=int(input())
    Store_obj=Store(rtv_list)
    result=Store_obj.fetchRtvProduct(quant)
    if len(result)==0:
        print("No RTVProduct Found")
    else:
        for k,v in result.items():
            print(v.sku_nbr,v.quantity,v.ship_To_Rlc_Flg)
