word=input("enter your wordd")
word=word.lower()
word=word.strip()
vowel=0
consonant=0
for i in range(0,len(word)):
    if word[i].isalpha()==True:
        if word[i]=="a" or word[i]=="e" or word[i]=="i" or word[i]=="o" or word[i]=="u":
            vowel=vowel+1
        else:
            consonant=consonant+1
    elif word[i].isalpha()==False:
            consonant=consonant
print("total no. of vowels are ",vowel)
print("total no. of consonants are ",consonant)