employees = {}

n = int(input("How many employees do you want to enter? "))

for i in range(n):
    print(f"Employee {i+1}")

    name = input("Enter name: ").title()
    age = int(input("Enter age: "))
    department = input("Enter department: ")
    salary = int(input("Enter salary: "))

    employees[name] = {
        "Age": age,
        "Department": department,
        "Salary": salary
    }

print("Employee Database")

for name, details in employees.items():
    print("Name:", name)
    for key, value in details.items():
        print(key, ":", value)