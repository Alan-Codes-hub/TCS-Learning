def countOfUniquenumbers(start,stop):
    count=0
    for i in range(start,stop+1):
        if str(i)[0]!=str(i)[1]:
            count+=1
    return count
        
if __name__=='__main__':
    start=int(input())
    stop=int(input())
    count=countOfUniquenumbers(start,stop)
    if count==0:
        print("No unique number")
    else:
        print(count)