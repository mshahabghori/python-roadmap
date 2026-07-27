num=int(input("Enter a num"))
if num<0:
    print("Invalid input")
elif num==0:
    print()
elif num==1:
    print(0)
else:
    prev=0
    current=1

    print(prev, end=" ")
    print(current, end=" ")

    for i in range(num-2):
        next=prev+current
        prev=current
        current=next
        print(next,end=" ")