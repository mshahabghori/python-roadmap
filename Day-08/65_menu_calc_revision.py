print("Welcome to My Calculator!!!\nWhat do you want to perform : ")
print("\t\t\tTotal\n\t\t\tSubtract\n\t\t\tDivide\n\t\t\tMultiply\n\t\t\tExit")
choice=""

while choice!="exit":
    choice=str(input("Enter what u want to perform "))
    choice=str.lower(choice)
    if choice!="exit":
        a,b=map(float,input("Enter two numbers").split())

        match choice:
            case "total":
                print(a+b)
            case "subtract":
                print(a-b)
            case "divide":
                if b==0:
                    print("Cannot Divide")
                else:
                    print(a/b)
            case "multiply":
                print(a*b)
            case "exit":
                print("Closing Calculator")
            case _:
                print("Invalid Input")