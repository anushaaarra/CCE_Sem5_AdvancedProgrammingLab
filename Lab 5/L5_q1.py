class Employee:
    def __init__(self, id, name, salary, department):
        self.emp_details = (int(id), name, int(salary), department)

def SearchList(emp, id):
    found = False
    for tup in emp:
        if tup[0] == id:
            print("Employee found.\n")
            print(f"Name: {tup[1]}, Salary: {tup[2]}, Department: {tup[3]}")
            found = True
            break

    if not found:
        print("Employee not found")

emp = []
n = int(input("Enter the number of employees: "))
for i in range(n):
    print("Enter id, name, salary, department:")
    id, name, salary, department = input().split()
    details_tup = Employee(id, name, salary, department).emp_details
    emp.append(details_tup)

print("Employee List: ", emp)
id = int(input("Enter employee id: "))
SearchList(emp, id)
