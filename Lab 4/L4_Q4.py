import time
from datetime import date

name = input("Enter your name: ")
curr = int(time.time())
current_time = time.localtime(curr)
today = date.today()

print("Hello ",name)
print(today)
print(f'{current_time.tm_hour}h: {current_time.tm_min}m: {current_time.tm_sec}s')

if current_time.tm_hour > 20:
    print("Good Night", name)
elif current_time.tm_hour >16:
    print("Good Evening", name)
elif current_time.tm_hour > 12:
    print("Good Afternoon", name)
else:
    print("Good Morning", name)
