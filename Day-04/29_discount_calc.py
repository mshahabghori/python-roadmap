bill=float(input("Enter bill amount"))
if bill<0:
    print("Invalid")
elif bill<1000:
    print("No discount")
elif 1000<=bill<=4999:
    print("After 10% discount=",bill-(bill*10/100))
elif 5000<=bill<=9999:
    print("After 20% discount=",bill-(bill*20/100))
else:
    print("After 30% discount=",bill-(bill*30/100))