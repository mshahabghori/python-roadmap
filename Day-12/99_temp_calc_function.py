def temp(t):
    t=t.lower()
    if t=="celsius":
        f=int(input("Enter temp in fahrenheit "))
        c = (f - 32) * 5/9
        return c
    elif t=="fahrenheit":
            c=int(input("Enter temp in celsius "))
            f = (c * 9/5) + 32 
            return f
    else:
        return 'Invalid'
t=input("Do u want to convert into Fahrenheit or Celsius ")
print(temp(t))