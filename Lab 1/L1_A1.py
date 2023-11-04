n = int(input("Enter Starting Range: "))
m = int(input("Enter Ending Range: "))
for i in range(n,m+1):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i)

