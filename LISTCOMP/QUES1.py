nums = [2, 5, 8, 11, 14]
even=[num for num in nums if num%2==0]
print(even)

text = "Python list comprehension makes coding concise"
text=text.split(" ")
lentext=[great for great in text if len(great)>5]
print(lentext)


word = input("enter your word: ")
dup=[ot for ot in word if word.count(ot)>1]
print(dup)

students = [
    ("Aman", 82),
    ("Riya", 65),
    ("Kabir", 91),
    ("Neha", 74)
]
top=[marks for marks in students if marks[1]>80]
print(top)

words = ["apple", "bat", "orange", "dog", "elephant", "cat"]
flter= [fruit.upper() for fruit in words if len(fruit)>3 and fruit.count("a")>0]
print(flter)


a = [1, 2, 3]
b = [4, 5, 6]
cartesian= [(numa,numb) for numa in a for numb in b if (numa+numb)%3==0]
print(cartesian)


text = "PyThOn Programming!!"
miras= [guti for guti in text if guti==guti.lower()]
print(miras)