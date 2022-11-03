def check_prime(n):
    if n>1:
        for i in range(2,n,1):
            if (n%i)==0:
                return 0
                break
        else:
            return 1
    elif n==1:
        return 0
    elif n<1:
        return 0

def prime_composite_list(inp):
    prime_list=[]
    comp_list=[]
    for j in inp:
        if check_prime(j)==1:
            prime_list.append(j)
        elif check_prime(j)==0:
            comp_list.append(j)
    output=[]
    output.append(prime_list)
    output.append(comp_list)
    return output

if __name__=='__main__':
    inp=[]
    count=int(input())
    for i in range(count):
        inp.append(int(input()))
    print(check_prime(inp[1]))

    result=prime_composite_list(inp)
    print(result)
    
