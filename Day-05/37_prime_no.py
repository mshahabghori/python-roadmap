num=int(input("Enter a number "))
if num<0:
    print("Invalid Input")
elif num==0 or num==1:
    print("Its not a prime number")
else:
    for i in range(2,num):
            if (num%i)==0:
                print("Its not a prime number")
                break
    else:
                print("Its a prime number")
 