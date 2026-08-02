a=list(map(int,input("Enter your numbers").split()))
smallest=a[0]

for number in a:
    if number<smallest:
        smallest=number
print("The smallest number is =",smallest)