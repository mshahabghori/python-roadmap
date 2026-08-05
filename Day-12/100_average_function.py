def avg(a):
    total=0
    for number in a:
        total=total+number
    avg=total/(len(a))
    return avg
average=list(map(int,input("Enter your numbers ").split()))
print("The average is = ",avg(average))
