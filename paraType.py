def printPositions(first, second, third="unknown", *consolations): # *variable-length argument
    print(first, " stood first in the race")
    print(second, " stood second")
    print(third, "stood third")
    
    for i in range(0, len(consolations)):
        print(consolations[i], " is consolation")


printPositions(third = "kunal", second = "mayank", first = "aditi") #keyword argument
printPositions("kunal","mayank","aditi") #positional argument
printPositions("kunal", "aditi", "mayank") #default parameters
printPositions("kunal", "aditi", "mayank", "nikita", "komal", "ishita") #default parameters

tup  = (1,3, 4,5, 10,0)
print(set(tup))

lst = (100, 23, 454, 123, 454, 14, 34, 123)
print(set(lst))














