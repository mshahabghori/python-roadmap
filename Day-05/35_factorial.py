num=int(input("Enter a number "))
if num==0:
    print("1")
elif num<0:
    print("Not possible for negative numbers")
else:
    fact=1
    for i in range(1,num+1):
        fact=i*fact
print(f"Factorial of {num} = ",fact)