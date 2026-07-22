inte=int(input("enter your number"))
b=0
while inte>0:
    c=inte%10
    b=b*10+c
    inte=inte//10
print(b)

"""
1st iteration let input be 2345
c=5
b=0*10+5
inte=234

2nd 
c=4
b=50+4
inte=23

3rd
c=3
b=540+3
inte=2

4th
c=2
b=5430+2
inte=0

end loop

"""