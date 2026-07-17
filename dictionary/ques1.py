marks = {
    "Math":90,
    "Physics":85,
    "Chemistry":95
}
f=0
for i in marks:
    f=f+marks[i]
print(f)

s="are","huhu","nyomi"
m={}
for i in range(0,len(s)):
    if s[i] in m:
        m[s[i]]=m[s[i]]+1
    else:
        m[s[i]]=1
print(m)