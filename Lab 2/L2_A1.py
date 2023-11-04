def factorial(n, ca={}):
    if n in ca:
        return ca[n]
    if n<=1:
        result=1
    else:
        result=n*factorial(n-1)
    ca[n]=result
    return result

n = int(input("Enter the number: "))
print(factorial(n))
