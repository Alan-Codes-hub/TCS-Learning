hand=open('regex_sum_167824.txt')
sum=0
import re
for line in hand:
    y=re.findall('[0-9]+',line)
    if len(y)<1 : continue
    print(y)
    for x in y:
        a=int(x)
        print(a)
        sum=sum+a
print('the sum is',sum)
