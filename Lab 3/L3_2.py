
def uniqueElem(x):
    return list(set(x))

x = []
y = []

n = int(input("Enter the number of elements in the list: "))
print("Enter the elements: ")
for i in range(0,n):
    ele = int(input())
    x.append(ele)

y = uniqueElem(x)
print("List of unique elements: ",y)
