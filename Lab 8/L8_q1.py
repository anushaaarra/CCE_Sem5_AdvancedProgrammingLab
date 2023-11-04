import re

function_names = dir(re)

pattern = re.compile('.*find.*')
find_functions = [name for name in function_names if pattern.match(name)]

sorted_functions = sorted(find_functions)

for function in sorted_functions:
    print(function)
