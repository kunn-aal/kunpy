#ab tereko 1 list leni hai wow nice question user se booht saare number lene hai aur sirf even no ki list bnani hai
user=input("enter your numbers ")
lst=user.split(" ")
fist=list(map(int,lst))
s=[]
for i in range(0,len(fist)):
    if fist[i]%2==0:
        s=s+[fist[i]]
print(s)