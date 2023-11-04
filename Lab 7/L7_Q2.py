import os
import re 

def countWords(filename):
    word_count = {}
    try:
        with open(filename,'r',encoding='utf-8') as f:
            ftxt = f.read()
            fwords = ftxt.split()
            for word in fwords:
                if word not in word_count:
                    word_count[word] = 1
                else:
                    word_count[word] = word_count[word] + 1 
            print(word_count)
            
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return f"An error occured: {str(e)}"  
    
filename = input("Enter the name of the file: ")
countWords(filename)
