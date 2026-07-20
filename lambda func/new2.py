# Question 7

employees = {
    "Ravi": ("HR", 45000),
    "Simran": ("IT", 80000),
    "Amit": ("Sales", 35000),
    "Sara": ("IT", 90000),
    "Neha": ("HR", 70000)
}

# Keep only employees earning more than 50000.
# Increase their salary by 10%.
# Convert employee names to uppercase.
# Print:
# SIMRAN works in IT and earns 88000.0
# using f-strings.
# Finally, use reduce() to find the total salary after the increment.

rich_emp=list(filter(lambda x:employees[x][1]>50000,employees))
print(rich_emp)

profit=list(map(lambda y:employees[y][1]+employees[y][1]/10,employees))
print(profit)

uname=list(map(lambda u:u.upper(),rich_emp))
print(uname)
name=uname[0]
print(f"{name} works in IT and earns 88000.0")

from functools import reduce

total=reduce(lambda a,b:a+b,profit)
print(total)