def max_num(a):
    largest=a[0]

    for number in a:
        if number>largest:
            largest=number
    return(largest)

number=list(map(int,input("Enter your numbers").split()))
print("The largest number is =",max_num(number))


