def find_Max_Number_From_Line(string):
    lst=string.split(" ")
    res=[]
    for i in lst:
        try:
            int(i)*1!=None
        except ValueError:
            pass
        else:
            res.append(i)
    for k in res:
        p=[]
        p[:0]=k
        if str(9) in p:
            res.remove(k)
    fin=[]
    for j in res:
        fin.append(int(j))
    return(max(fin))
    
if __name__=='__main__':
    tot=[]
    count=int(input())
    for k in range(count):
        tot.append(find_Max_Number_From_Line(input()))
    print(max(tot))
    
    
    
    