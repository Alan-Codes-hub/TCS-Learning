def get_Index_of_number(integer_list,n):
    m=integer_list.index(n)
    c=-1
    for i in integer_list:
        c+=1
        if i==n and c!=m:
            return c
        else:
            return 0

if __name__=='__main__':
    integer_list=[]
    count=int(input())
    for j in range(count):
        integer_list.append(int(input()))
    n=int(input())


    result=get_Index_of_number(integer_list,n)
    if result==None:
        print("0")
    else:
        print(result)
