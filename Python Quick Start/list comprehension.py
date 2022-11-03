seq=range(11)
seq1=[x*2 for x in seq]
seq2=[x for x in seq if x%3 !=0]
seq3=[(x,x**2) for x in seq]
from math import pi
seq4=[round(pi,i) for i in seq]
seq5={x:x**2 for x in seq}
seq6={x for x in 'superduper' if x not in 'pd'}
for i in range(11):
    print(i,end=' ',flush=True)
print()
print('seq1:',seq1)
print('seq2:',seq2)
print('seq3:',seq3)
print('seq4:',seq4)
print('seq5:',seq5)
print('seq6:',seq6)
