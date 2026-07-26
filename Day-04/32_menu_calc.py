a=float(input("Enter 1st number"))
b=float(input("Enter 2nd number"))
choice=int(input("Enter the index number of the operation you want to perform\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Exit"))
match choice:
    case 1:
        print(a+b)
    case 2:
        print(a-b)
    case 3:
        print(a*b)
    case 4:
        if b==0:
            print("Cannot divide by zero")
        else:
            print(a/b)
    case 5:
        exit()
    case _:
        print("Invalid operation")