"""
Write a python script to create a list of tuples, where each tuple is a pair of elements,
first element is uppercase character and second element is its unicode
"""

# taking input from the user
n = int(input("Enter how many elements you want to store : "))

# creating a list of elements taking from the user
l1 = list()

i = 0
while i < n :
    l1.append(input("Enter %d character : " %(i+1)))
    i += 1
    
# creating a list of tuples
tuple_list = list()

for string in l1 :
    tuple_list.append((string.upper(), ord(string)))
    
# printing a list of tuple
print(tuple_list)