choice = ""

while choice != "exit":

    choice = str(input("Enter what action you want to perform: "))

    if choice != "exit":
        a = int(input("Enter 1st number: "))
        b = int(input("Enter 2nd number: "))

    match choice:
        case "total":
            print(a + b)

        case "subtract":
            print(a - b)

        case "product":
            print(a * b)

        case "division":
            if b == 0:
                print("Cannot divide by zero")
            else:
                print(a / b)

        case "exit":
            print("Calculator closed")

        case _:
            print("Invalid operation")