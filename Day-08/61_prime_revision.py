num=int(input("Enter a number "))
if num<0:
    print("Not Valid")
elif num==0 or num==1:
    print("Not Prime")
else:
    for i in range(2,num):
        if num%i==0:
            print("Not Prime")
            break
    else:
        print("Prime")