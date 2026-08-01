num=int(input("Enter a number "))
count=0

if num==0:
    print("The no of digits are = 1")
else:
    if num<0:
        num=abs(num)

    while num>0:
        num=num//10
        count=count+1

    print("The no of digits are = ",count)