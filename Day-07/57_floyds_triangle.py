n = int(input("Enter the number of rows: "))
total=1
for i in range(1,n+1):
    for j in range(1,i+1):
        print(total,end=" ")
        total=total+1
    print()