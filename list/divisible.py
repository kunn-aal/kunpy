kist=input("enter your numbers")
lst=kist.split(" ")
s=[]
mist=list(map(int,lst))
for i in range(0,len(mist)):
    if mist[i]%3==0 and mist[i]%5==0:
        s=s+[mist[i]]
print(s)


# 9 marks