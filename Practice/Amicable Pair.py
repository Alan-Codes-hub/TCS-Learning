def amicable(x,y):
    lstx=[]
    lsty=[]
    for c in range(1,x):
        if x%c==0:
            lstx.append(c)
    for v in range(1,y):
        if y%v==0:
            lsty.append(v)
    if sum(lstx)==y and sum(lsty)==x:
        return True
    else:
        return False
if __name__=='__main__':
    x=int(input())
    y=int(input())
    result=amicable(x,y)
    if result:
        print(x,"and",y,"constitute an amicable pair")
    else:
        print("Not an amicable pair")
