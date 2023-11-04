sentence = input("Enter the sentence : ").split()

words = {}
i = 0
for word in sentence:
    words[i] = word
    i+= 1

print(words)
print("Total words: ", len(words))
