ans=input("enter your numbers: ")
s=ans.split(" ")
m=tuple(map(int,s))
t=m[len(m):len(m)-5:-1]
print(t)
