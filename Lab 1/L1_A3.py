n=input("Enter string: ")
for i in n:
    if i not in '0123456789ABCDEF':
        print("Not Hexadecimal")
        exit(0)
print("Hexadecimal")
