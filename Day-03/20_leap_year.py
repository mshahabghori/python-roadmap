year=int(input("Enter year"))

if year%400==0:
    print("Its a leap year")
elif year%100==0:
    print("Not a leap year")
elif year%4==0:
    print("Its a leap year")
else:
    print("Not a leap year")