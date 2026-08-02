a=list(map(int,input("Enter your numbers ").split()))
unique=[]
for number in a:
    if number not in unique:
        unique.append(number)
print(unique)