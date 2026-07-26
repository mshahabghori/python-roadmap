unit=float(input("Enter units"))
if unit<=0:
    print("0 Bill")
elif unit>=1 and unit<=100:
    print(unit*5)
elif unit>=101 and unit<=200:
    print((unit-100)*7+500)
else :
    print((unit-200)*10+500+700)