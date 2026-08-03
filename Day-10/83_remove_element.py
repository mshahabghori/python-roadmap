a=list(map(int,input("Enter your numbers").split()))
print("This is your current list :",a)
choice=int(input("Enter the number you want to remove :"))
if choice not in a:
    print("Number cannot be found")
else:
    a.remove(choice)
    print("Your updated list is :",a)