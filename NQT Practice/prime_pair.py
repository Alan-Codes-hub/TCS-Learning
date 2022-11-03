def PrimeList(m,n):
    lst=[]
    for i in range(m,n+1):
        lst.append(i)
    for i in range(m,n+1):
        for j in range(2,i):
            if i%j==0 and i in lst:
                lst.remove(i)
    return lst

def Prime_Pair(primelist):
    dictionary={}
    for k in primelist:
        if k+6 in primelist:
            dictionary[k]=k+6
    return dictionary
    
if __name__=='__main__':
    m=int(input())
    n=int(input())
    primelist=PrimeList(m,n)
    dictionary=Prime_Pair(primelist)
    print(primelist)
    if len(dictionary.keys())==0:
        print("No prime pair")
    else:
        print(len(dictionary.keys()))
    