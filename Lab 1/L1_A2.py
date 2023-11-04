n = int(input("Enter the number: "))
sum = 0
order = len(str(n))
temp = n
while temp>0:
    digit = temp % 10
    sum += digit ** order
    temp //= 10
if n == sum:
    print("It is an armstrong number")
else:
    print("It is not an armstrong number")
