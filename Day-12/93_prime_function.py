def prime(num):
    if num<0:
        return ("Not Valid")
    elif num==0 or num==1:
        return ("Not Prime")
    else:
        for i in range(2,num):
            if num%i==0:
                return("Not Prime")
        else:
            return("Prime")
number=int(input("Enter a number :"))
print(prime(number))