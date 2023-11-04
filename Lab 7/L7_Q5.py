def checkChar(inputstr):
    pattern = r'^(.).*\1$'
    matchObj = re.match(pattern,inputstr)
    if matchObj:
        print("The first and last character of the string matches.")
    else:
        print("The first and last character of the string do not match.")

inputStr = input("Enter a string: ")
checkChar(inputStr)
