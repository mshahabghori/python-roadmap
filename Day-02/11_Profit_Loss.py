cost=float(input("Enter cost price"))
sell=float(input("Enter selling price"))

if cost>sell:
    print("Loss")
elif cost<sell:
    print("Profit")
else:
    print("No profit no loss")