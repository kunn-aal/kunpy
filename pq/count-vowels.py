#Write a function count_vowels(text) that returns the number of vowels in a string.
sentence=input("enter your sentence: ")
mentence=list(map(str,sentence))
def count_vowels(text):
    diction={}
    for i in range(0,len(text)):
        if text[i] in diction:
            diction[text[i]]=diction[text[i]]+1
        elif text[i]=="a" or text[i]=="e" or text[i]=="i" or text[i]=="o" or text[i]=="u":
            diction[text[i]]=1
    print(diction)

count_vowels(mentence)
