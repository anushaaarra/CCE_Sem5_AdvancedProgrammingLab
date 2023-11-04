#Inputting matrices
print("INPUT FIRST MATRIX")
n = int(input("Enter the number of rows: "))
m = int(input("Enter the number of columns: "))

matrix = {}
print("Enter the elements: ")

for i in range(n):
    lst = []
    for j in range(m):
        ele = int(input(""))
        if ele != 0:
            lst.append(ele)
        else:
            continue
    matrix[i] = lst

print("INPUT SECOND MATRIX")
x = int(input("Enter the number of rows: "))
y = int(input("Enter the number of columns: "))

matrix1 = {}
print("Enter the elements: ")

for i in range(x):
    lst = []
    for j in range(y):
        ele = int(input(""))
        if ele != 0:
             lst.append(ele)
        else:
            continue
    matrix1[i] = lst

#Printing matrices
print("First Matrix: ")
for k in matrix:
    print(matrix[k])
    
print("Second Matrix: ")
for k in matrix1:
    print(matrix1[k])

#Adding the matrices
sum_matrix = {}

for i in range(n):
    lst1 = matrix[i]
    lst2 = matrix1[i]
    lst3 = []
    for j in range(x):
        ele = lst1[j] + lst2[j]
        lst3.append(ele)
    sum_matrix[i] = lst3

print("Sum Matrix: ")
for k in sum_matrix:
    print(sum_matrix[k])



