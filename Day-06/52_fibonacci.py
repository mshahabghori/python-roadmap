num=int(input("Enter a num"))
i=2
if num<0:
    print("Invalid input")
elif num==0:
    print("No Terms")
elif num==1:
    print(0)
else:
    prev=0
    current=1

    print(prev, end=" ")
    print(current, end=" ")

    while i<=num:
        next=prev+current
        prev=current
        current=next
        print(next,end=" ")
        i=i+1