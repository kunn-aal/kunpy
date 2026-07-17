user=input("enter your numbers ")
lst=user.split(" ")
fist=list(map(int,lst))
for i in range(0,len(fist)):
    fist[i]=fist[i]+fist[i]

print(fist)