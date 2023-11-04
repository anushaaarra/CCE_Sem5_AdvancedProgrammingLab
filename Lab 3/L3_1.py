
def multiply(n,x):
    mul = 1
    for i in x:
        mul = mul * i
    return mul


n = int(input("Enter the number of elements in the list: "))
x = []
print("Enter the elements: ")
for i in range(0,n):
    ele = int(input())
    x.append(ele)
y = multiply(n, x)
print("Sum of all the elements in the list: ", y)
