n = int(input("Enter the number of lines: "))

#Reading and Writing the data
if n>7:
    with open ('D:/210953092/Lab 2/readme.txt','a+') as f:
        print("Enter the lines to input: ")
        for i in range(0,n):
            ele = input()
            f.write(ele)
            f.write('\n')
    with open ('D:/210953092/Lab 2/readme.txt','r+') as f1:
        lines = f1.readlines()
        print(lines)
else:
    print("Require a minumum of 8 lines to create the file")


#Storing in the form of a dictionary
line_dict = {}
for i, line in enumerate(lines, start=1):
    line = line.strip()
    line_length = len(line)
    line_dict[i] = [line, line_length]

print("Dictionary with line numbers as keys and [line, length] as values:")
for key, value in line_dict.items():
    print(key, ":", value)

letter_freq = {}
for line in lines:
    for char in line:
        if char.isalpha():
            char = char.lower()
            if char in letter_freq:
                letter_freq[char] += 1
            else:
                letter_freq[char] = 1

print("\nDictionary with letters as keys and frequencies as values:")
for key, value in letter_freq.items():
    print(key, ":", value)
