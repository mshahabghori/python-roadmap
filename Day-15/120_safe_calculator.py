def calc(a, b, op):
    if op == "+":
        print(a + b)

    elif op == "-":
        print(a - b)

    elif op == "*":
        print(a * b)

    elif op == "/":
        if b == 0:
            print("Cannot Divide by 0")
        else:
            print(a / b)

    elif op == "exit":
        exit()

    else:
        print("Unidentified Operator")


while True:

    try:
        x, y = map(int, input("Enter two numbers : ").split())

    except ValueError:
        print("Invalid number")
        continue

    sign = input("Enter the sign of operation you want to perform : ").lower()

    calc(x, y, sign)