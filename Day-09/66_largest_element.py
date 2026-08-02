a=list(map(int,input("Enter your numbers").split()))
largest=a[0]

for number in a:
    if number>largest:
        largest=number
print("The largest number is =",largest)