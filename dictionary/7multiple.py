#print first multiple of seven
lst=input("enter your numeros: ")
lst=lst.split(" ")
lst2=list(map(int,lst))
mt_dict={}
for i in range(0,len(lst2)):
    if lst2[i]%7==0:
        mt_dict[i]=lst2[i]
        print(mt_dict,"is divisible")
        break
else:
    print("no no. is divisible")