input_lst = input("enter numbers you want: ")
#these values are known as space-seperated values

lst = list(map(float, input_lst.split(" ")))

print(lst)
#use int() to convert char and strings to integer 
#map() is used to convert items in a list to passed parameter like int, str, bool etc

