t = (1,2,2,3,4,4,5,5,6)
m=list(t)
m.sort(reverse=True)
s=set(m)
print(s)


#tuple unpacking

tup = ["kunal", "aditi" , "bob", "koru"]

first, *middle , second_last, last= tup
print(first)
print(middle)
print(second_last)
print(last)





