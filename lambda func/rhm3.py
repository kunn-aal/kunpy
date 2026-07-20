from functools import reduce
words = ["apple", "banana", "cat", "elephant", "dog", "grapes"]
fil_word=list(filter(lambda x:len(x)>5,words))
print(fil_word)
mword=list(map(lambda n:n.upper(),fil_word))
print(mword)
red_word=reduce(lambda a,b:a+" | "+b,mword)
print(red_word)