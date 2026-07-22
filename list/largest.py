#find the largest coeing
kist=input("enter your numbers")
lst=kist.split(" ")
mist=list(map(int,lst))

s = mist[0]

for i in range(1,len(mist)):
    if s>mist[i]:
        s=s
    elif s<mist[i]:
        s=mist[i]

print(s)