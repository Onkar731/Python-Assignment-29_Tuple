"""
Write a python script to find the sum  of all odd numbers stored in a tuple
"""

# creating a tuple
t1 = (23, 45, 12, 56, 98, 45, 98, 92, 12, 55, 19, 47, 78, 675,)

# finding sum of all odd numbers stored in a tuple
sum = 0
for e in t1 :
    if e%2 != 0 :
        sum += e
        
# printing sum of all odd numbers
print("Sum of all odd numbers stored in tuple is", sum)