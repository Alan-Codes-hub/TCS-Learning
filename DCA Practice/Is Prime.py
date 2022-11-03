# 0 implies positive and 1 implies negative
def Is_Neg(num):
    if num<0:
        return 1
    elif num>0:
        return 0

# 0 implies not prime and 1 implies prime
def Is_Prime(num):
    val=0
    if num==1:
        val=0
    elif num>1:
        for i in range(2,num):
            if num%i==0:
                val=1
            else:
                val=0
    return val
    
if __name__=='__main__':
    num=int(input())
    if Is_Neg(num)==0:
        if Is_Prime(num)==1:
            print(num,"is a prime number")
        elif Is_Prime(num)==0:
            print(num,"is not a prime number")
    elif Is_Neg(num)==1:
        print("Enter a positive number")
            
            
    
        
    
    