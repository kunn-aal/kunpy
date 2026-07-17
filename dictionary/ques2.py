s="aabbcdde"
m={}
for i in range(0,len(s)):
    if s[i] in m:
        m[s[i]]=m[s[i]]+1
    else:
        m[s[i]]=1

for t in m: # m= {"a" : 2, "b" : 2, "c" : 1, "d": 2, "e": 1} 
    if m[t] == 1 :
        print(t)
        break #stop the loop 
    if m[t] != 1:
        continue # move to next iteration
    print(t, " hii")
    




#break and continue
