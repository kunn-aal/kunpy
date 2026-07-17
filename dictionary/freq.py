s="missisipi"
m={}
for i in range(0,len(s)):
    if s[i] in m:
        m[s[i]]=m[s[i]]+1
    else:
        m[s[i]]=1


num = list(m.keys())[0]
c=m[num]


for t in m:
    if m[t]>c:
        c=m[t]
        num = t
    else:
        c=c
print(num,":",c)
