#boy
word=input("enter your word")
a=0
for i in range(0,len(word)):
    if word[i]=="a" or word[i]=="e" or word[i]=="i" or word[i]=="o" or word[i]=="u":
        a=a+1
        print(word[i],"is a vowel") 
    else:
        print(word[i],"not a vowel")
print(a,"is the number of ovwel")