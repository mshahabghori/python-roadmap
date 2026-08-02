a=list(map(int,input("Enter your numbers ").split()))
total=0
for number in a:
    total=total+number
avg=total/(len(a))
print("The average is =",avg)