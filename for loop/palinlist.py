r=input("enter your nuber: ")
r=r.split(" ")
s=list(map(int,r))
def palin(lst):
    m=[]
    for i in range(len(lst)-1,-1,-1):
        m=m+[lst[i]]
    if lst==m:
        print("palindrome")
    else:
        print("nope")
palin(s)