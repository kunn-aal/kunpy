lst=input("enter your numeros: ")
lst=lst.split(" ")
lst2=list(map(int,lst))
m=lst2[0]
for i in range(0,len(lst2)):
    if m>lst2[i]:
        m=m
    else:
        m=lst2[i]
lst2.remove(m)
n=lst2[0]
for t in range(0,len(lst2)):
    if n>lst2[t]:
        n=n
    else:
        n=lst2[t]
print(n)