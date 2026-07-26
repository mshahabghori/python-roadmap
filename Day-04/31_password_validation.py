password=str(input("Enter a password"))
l=len(password)
has_digit = any(ch.isdigit() for ch in password)

if l>=8:
    if has_digit:
        print("Valid password")
    else:
        print("Weak password number is required")
else:
    print("Weak password increasethe length")