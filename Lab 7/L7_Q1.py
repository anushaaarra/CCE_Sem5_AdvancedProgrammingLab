import os
import re

def countFile(filename): 
    try:
        with open(filename,'r',encoding='utf-8') as f:
            ftxt = f.read()
            char_count = len(ftxt)
            word_count = len(ftxt.split())
            line_count = ftxt.count('\n')+1
        print(f"No of Characters: {char_count}")
        print(f"No of Words: {word_count}")
        print(f"No of Lines: {line_count}")
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return f"An error occured: {str(e)}"

filename = input("Enter the name of the file: ")
countFile(filename)
