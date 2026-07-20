words = ["apple", "banana", "mango"]
gurts = list(map(lambda word: word.upper(),words))
print(gurts)

hurt=list(filter(lambda n:len(n)>5,words))
print(hurt)
from functools import reduce
lst=[1,2,3,4,5,6,7,8]
murt=reduce(lambda a,b:(a+b)/len(lst),lst)
print(murt)