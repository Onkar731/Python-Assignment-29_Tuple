"""
Write a python script to create a tuple from a given list
"""


# taking input from the user
n = int(input("Enter how many elements you want to store : "))

# creating a list of elements taking from the user
l1 = list()

i = 0
while i < n :
    l1.append(eval(input("Enter %d element : " %(i+1))))
    i += 1

# creating a tuple from the given list using tuple method
t1 = tuple(l1)

# printing tuple 
print(t1)