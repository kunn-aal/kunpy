from functools import reduce
nums = [1,2,3,4,5,6,7,8,9,10]
even=list(filter(lambda n:n%2==0,nums))
print(even)
square=list(map(lambda x:x*x,even))
print(square)
sum=reduce(lambda a,b:a+b,square)
print(sum)