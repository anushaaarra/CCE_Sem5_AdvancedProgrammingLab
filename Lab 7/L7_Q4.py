import re
import os

def email_validity(email):
    email_regex = r'^[A-Za-z0-9._%+-]+@[A-Za-z]+\.[A-za-z]+$'
    if re.match(email_regex, email):
        return True
    else:
        return False

def checkValid(filename):
    try:
        with open(filename,'r',encoding='utf-8') as f:
            email_list = f.read().splitlines()
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return f"An error occured: {str(e)}"  
      
    valid_emails = []
    invalid_emails = []
    
    for email in email_list:
        if email_validity(email):
            valid_emails.append(email)
        else:
            invalid_emails.append(email)
    
    with open('valid.txt', 'w', encoding='utf-8') as valid_file:
        for email in valid_emails:
            valid_file.write(email + '\n')
    
    with open('invalid.txt', 'w', encoding='utf-8') as invalid_file:
        for email in invalid_emails:
            invalid_file.write(email + '\n')
    
    print(f"Valid email IDs are saved in 'valid.txt'.")
    print(f"Invalid email IDs are saved in 'invalid.txt'.")

filename = input("Enter your filename with stored email ids: ")
checkValid(filename)
