def even_odd(number):
    odd=[]
    even=[]
    for i in number:
        if i%2!=0:
            if i not in odd:
                odd.append(i)
        else:
            if i not in even:
                even.append(i)
    return odd, even

n = list(map(int,input("Enter your numbers :").split()))
odd, even = even_odd(n)
print("Odd =", odd)
print("Even =", even)