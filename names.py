user=input("enter your names ")
lst=user.split(" ")
fist=list(map(str,lst))
for i in range(0,len(fist)):
    fist[i]=fist[i].capitalize()
print(fist)
