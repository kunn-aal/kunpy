words = ["python", "AI", "developer", "code", "machine", "hi", "learning"]

# Keep only words having length > 4.
# Convert them to uppercase.
# Join them into one string separated by " | " using reduce().
# Print using an f-string.

from functools import reduce

len=list(filter(lambda x:len(x)>4,words))
print(len)
ulen=list(map(lambda y:y.upper(),len))
print(ulen)
len2=reduce(lambda a,b:a+" | "+b,ulen)
min=len2
print(f"{min} is the list")