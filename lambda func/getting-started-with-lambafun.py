"""
def add(num1, num2):
    print(num1+num2)"""

"""lamba function!!!
-shorthand function: shorter way to write a function
-Anonymous function: function without a name
-single expression only"""

lst = [1, 2, 3, 4, 5]
nested_list = [[1,2,3,4], [4,5,6,7], [6,7,8]]

def double_item(num):
    return num*2

#map
double = list(map(double_item, lst))
double_lambda = list(map(lambda num: num*2,lst))


#function call --- func()
#function pass --- func(a,b) func(func) use lambda  : HIGHER ORDER FUNCTIONS
print(double)
print(double_lambda)
#filter

#reduce
