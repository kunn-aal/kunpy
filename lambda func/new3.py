# Question 4

sentence = "python makes coding fun and python is powerful"

# Convert the sentence into words.
# Keep only words starting with "p".
# Convert them to uppercase.
# Join them using " -> " with reduce().
# Print the final result using an f-string.
ment=sentence.split(" ")
sent=list(map(str,ment))
print(sent)

pword=list(filter(lambda x:x[0]=="p",sent))
print(pword)

uword=list(map(lambda y:y.upper(),pword))
print(uword)

from functools import reduce
adding=reduce(lambda a,b:a+"->"+b,uword)
print(adding)