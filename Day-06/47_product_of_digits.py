num=int(input("Enter a number "))
prod=1

while num>0:
    digit=num%10
    prod=prod*digit
    num=num//10

print("The prod is = ",prod)