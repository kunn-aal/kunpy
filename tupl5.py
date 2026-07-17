t = (12,15,18,21,24,27,30)
m=list(t)
s=[]
for i in range(0,len(m)):
    if m[i]%3==0:
        s=s+[m[i]]
    else:
        s=s
f=tuple(m)

#merging uples
t1=(1,21,3)
k=1
for i in range(0,len(t1)):
    k=k*t1[i]
print(k)