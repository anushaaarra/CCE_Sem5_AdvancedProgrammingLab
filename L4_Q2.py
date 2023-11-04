import math
import cmath

def calc(x):
    print("Sin value of the number:", cmath.sin(x))
    print("Square root of the number:", cmath.sqrt(x))
    print("Log value of the number:", cmath.log(x))
    
x,y = map(int,input("Enter the complex number: ").split())
n = complex(x,y)
print("The complex number entered is: ",x,"+",y,"j")
calc(n)
