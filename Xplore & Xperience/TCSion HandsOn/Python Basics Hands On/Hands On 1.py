s=input()
c=0
for i in s:
    i=i.lower()
    if i in ("a","e","i","o","u"):
        c+=1
print(c)
