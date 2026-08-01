num=int(input("Enter a number "))
guess=10
count=0
if num==guess:
    print("Correct")
else:
    while num!=guess:
        print("Try Again")
        num=int(input("Enter a number again "))
        count=count+1
        if count==3:
            exit()
    print("Correct")
