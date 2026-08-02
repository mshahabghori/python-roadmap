num=int(input("Enter a number "))
if num<0:
    print("Not Valid")
elif num==0:
    print("No Value")
elif num==1:
    print("0")
else:
    prev=0
    current=1
    print(prev,end=" ")
    print(current,end=" ")
    for i in range(num-2):
        next=prev+current
        prev=current
        current=next
        print(next,end=" ")
