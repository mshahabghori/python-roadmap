import random
num=int(input("Enter a number between 1 to 100"))
guess=random.randint(1,100)
count=0
if num==guess:
    print("Correct")
else:
    while num!=guess:
        if count==2:
            print("The number was ",guess)
            exit()
        else:
            if num<guess:
                print("Too Low")
            else:
                print("Too High")
        num=int(input("Enter a number again "))
        count=count+1
    print("Correct")
