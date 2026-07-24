a,b,c=map(float,input("Enter three no.s").split())
if (a>b and a>c):
    print("The largest is ",a)
elif (b>a and b>c):
    print("The largest is ",b)
elif (c>a and c>b):
    print("The largest is ",c)
elif (a>=b and b<c):
    print("The largest is ",a)
elif (a>=c and c<b):
    print("The largest is ",a)
elif (b>=c and b<a):
    print("The largest is ",b)
else:
    print("All are equal")