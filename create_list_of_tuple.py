"""
Write a python script to create a list of tuples from a given list of strings,
where each tuple is a collection of strings begin with the same character
"""

# taking input from the user
n = int(input("Enter how many elements you want to store : "))

# creating a list of elements taking from the user
l1 = list()

i = 0
while i < n :
    l1.append(input("Enter %d string : " %(i+1)))
    i += 1
    
# creating a list of tuples
tuple_list = list()
temp_list = list()

l1.sort()
str = str()
for e in l1 :
    if str == e[0] :
        temp_list.append(e)
    str = e
print(l1)