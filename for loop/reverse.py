word=input("enter your wor")
reverse="" 
for i in range(len(word)-1,-1,-1):
    reverse=reverse+word[i]
word=word.strip()
reverse=reverse.strip()
if word.lower()==reverse.lower():
    word.strip()
    print("yes palindrome")
else:
    print("not a palindrome")
