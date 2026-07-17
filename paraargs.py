def greet(name,age,city):
    print("hello",name,age,"living in",city)

greet("rahul",34,"mumbai")

def student(name,course,year):
    print("hey",name, "are you in",course,"in",year)

student("btech","kunal",4)

def welcome(greet="figler"):
    print(greet,"welcome to the house")

welcome()

a=input("enter your number")
b=a.split(" ")
c=list(map(int,b))
def func(number):
    for i in range(0,len(number)):
        print(number[i])
func(c)

