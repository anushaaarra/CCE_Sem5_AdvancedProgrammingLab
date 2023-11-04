def add():
    x = 2
    y = 4
    z = x+y
    print(z)

print(add.__code__.co_nlocals)
