def calc(a,b,op):
    if op=="+":
        print(a+b)
    elif op=="-":
        print(a-b)
    elif op=="*":
        print(a*b)
    elif op=="/":
        if b==0:
            print("Cannot Divide by 0")
        else:
            print(a/b)
    else:
        print("Unidentified Operator")
x,y=map(int,input("Enter two numbers").split())
sign=input("Enter the sign of operation you want to perform")
calc(x,y,sign)