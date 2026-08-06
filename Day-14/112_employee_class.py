class Employee:
    pass

employee_01 = Employee()

employee_01.name = input("Enter name: ")
employee_01.age = int(input("Enter age: "))
employee_01.department = input("Enter department: ")
employee_01.salary = int(input("Enter salary: "))

print("\nEmployee Details :")

print("Name =", employee_01.name)
print("Age =", employee_01.age)
print("Department =", employee_01.department)
print("Salary =", employee_01.salary)