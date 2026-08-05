def fact(num):
    if num==0:
        factorial=1
        return (factorial)
    elif num<0:
        return("Not possible for negative numbers")
    else:
        factorial=1
        for i in range(1,num+1):
            factorial=i*factorial    
        return (factorial)
number=int(input("Enter a number "))
print(fact(number))
