def check_palindrome(inp_str):
    lst=[]
    for i in inp_str:
        j=i.lower()
        if j==j[::-1]:
            lst.append(i)
    return lst
if __name__=='__main__':
    count=int(input())
    inp_str=[]
    for i in range(count):
        inp_str.append(input())
    output=check_palindrome(inp_str)
    if len(output)!=0:
        for i in output:
            print(i)
    else:
        print('No palindrome found')
