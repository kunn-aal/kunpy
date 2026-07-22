r=input("enter your nuber: ")
r=r.split(" ")
s=list(map(int,r))

def doubleList(lst):
    new_lst = lst.copy()
    for i in range(0, len(lst)):
        new_lst[i]=lst[i]
    
    return new_lst


update_lst = doubleList(s)
print(update_lst)
print(s)



