lst=input("enter your numeros: ")
lst=lst.split(" ")
lst2=list(map(int,lst))
mt_dict={}
for i in range(0,len(lst2)):
    if lst2[i] in mt_dict:
        mt_dict[lst2[i]]=mt_dict[lst2[i]]+1
        if mt_dict[lst2[i]]==3:
           print("index: ", i)
           break
    else:
        mt_dict[lst2[i]]=1

print(mt_dict)