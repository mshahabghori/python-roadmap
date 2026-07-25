password=str(input("Enter a password"))
l=len(password)
c=password.isdigit()
if l>8:
    if c==True:
        print("Valid password")
    else:
        print("Weak password number is required")
else:
    print("Weak password increasethe length")