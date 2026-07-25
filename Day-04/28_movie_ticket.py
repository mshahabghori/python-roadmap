age=int(input("Enter age"))
if age<0:
    print("Invalid age")
elif age<5:
    print("Free")
elif 5<=age<=17:
    print("100")
elif 18<=age<=59:
    print("200")
else:
    print("150")