a=list(map(int,input("Enter your numbers ").split()))
target=int(input("Enter the number to be searched "))

left=0
right=len(a)-1

while left<=right:
    middle=(left+right)//2

    if a[middle]==target:
        print("Number found at ",middle)
        break
    elif target>a[middle]:
        left=middle+1
    else:
        right=middle-1
else:
    print("Number not found")