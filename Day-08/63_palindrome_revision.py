num=int(input("Enter a number "))
original=num
total=0
while num>0:
    digit=num%10
    total=total*10+digit
    num=num//10
if total==original:
    print("Palindrome")
else:
    print("Not Palindrome")