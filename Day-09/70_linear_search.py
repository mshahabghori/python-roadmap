a=list(map(int,input("Enter your numbers ").split()))
target=int(input("Enter the number to be searched "))
found=False
position=-1
for i in range(len(a)):
    if a[i]==target:
        found=True
        position=i
        break
if found==True:
    print("Number Found at ",position)
else:
    print("Number not Found")