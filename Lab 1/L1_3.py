x = []
n = int(input("Enter the number of strings: "))
for i in range(0,n):
    ele = str(input())
    x.append(ele)
print()
print("List of strings: ")
print(x)
print()
print("Strings with odd length: ")
for i in x:
    if len(i)%2!=0:
        print(i)
print()     
print("Number of strings with same first and last character and length greater than 2: ")
count = 0
for i in x:
    if len(i)>=2:
            if i[0] == i[-1]:
                count+=1
        
print(count)

