students = [
    ("Aman", 85),
    ("Kunal", 42),
    ("Riya", 91),
    ("Neha", 65),
    ("Rahul", 39),
    ("Simran", 78)
]
marks=list(filter(lambda x:x[1]>50,students))
print(marks)
transform=list(map(lambda a: f"{a[0]} : {a[1]}",marks))
print(transform)
from functools import reduce
