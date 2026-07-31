num=int(input("Enter a number "))
if num<0:
    print("Not a natural number")
else:
    sum=0
    for i in range(1,num+1):
        sum=i+sum
print("SUM=",sum)