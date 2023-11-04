import random

dict1 = {}
n = int(input("Enter the number of inputs: "))

# Reading dictionary from user
dtype = "Number"
print("Enter dictionary inputs: ")
for i in range(n):
    y = input("")
    if y.isnumeric() and dtype == "Number":
        y = int(y)
    dict1[random.randint(0,100)] = y;
    if isinstance(y,str):
        dtype = "String"
print("Data Type of dictionary is: ")
print (dtype)

# Printing average of numbers/ concatenating strings
avg = 0
res = ""
if(dtype == "Number"):
    for i in dict1:
        avg += dict1[i]
    avg = avg/len(dict1)
    print("As integers are present, Average: ")
    print(avg)
else:
    for i in dict1:
        res = res + dict1[i] + " "
    print("As strings are present, Concatenate: ")
    print(res)

print(dict1)

# Searching for an input string
if dtype == "String":
    inp = input("Enter the string to be searched: ")
    for i in dict1:
        if dict1[i] == inp:
            print("String present")

# Printing special value characters 
if dtype == "String":
    print("\nSpecial Characters: ")
    special_characters='[](){}<>\/!@#$%^&_*-+=|:`~'
    print(special_characters)
    for i in dict1:
        for char in dict1[i]:
            if char in special_characters:
                print(dict1[i])
