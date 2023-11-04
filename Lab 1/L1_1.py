x=[]
y=[]
z=[]
n = int(input("Enter the number of elements in the first list: "))
print("Enter the elements: ")
for i in range(0,n):
    ele = int(input())
    x.append(ele)
m = int(input("Enter the number of elements in the second list: "))
print("Enter the elements: ")
for j in range(0,m):
    elem = int(input())
    y.append(elem)

print("First List:")
print(x)
print("Second List:")
print(y)

for i in x:
    if(i%2!=0):
        z.append(i)
for j in y:
    if(j%2==0):
        z.append(j)
print("Output:")
print(z)
