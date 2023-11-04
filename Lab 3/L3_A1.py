def casecalc(strn):
    lower = 0
    upper = 0
    for i in strn:
        if (i.islower()):
            lower += 1
        if (i.isupper()):
            upper += 1
    print("The number of lowercase characters is:",lower)
    print("The number of uppercase characters is:",upper)

strn = input("Enter the string: ")
casecalc(strn)
