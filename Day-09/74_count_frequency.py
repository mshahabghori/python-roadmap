a=list(map(int,input("Enter your numbers ").split()))
frequency={}
for number in a:
    if number in frequency:
        frequency[number] = frequency[number] + 1
    else:
        frequency[number] = 1

print(frequency)