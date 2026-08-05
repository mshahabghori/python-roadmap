def area(shape):
    if shape=="square":
        s=float(input("Enter the length of side :"))
        return s**2

    elif shape=="rectangle":
        l,b=map(float,input("Enter the length and breadth :").split())
        return l*b

    elif shape=="circle":
        r=float(input("Enter the radius :"))
        return 3.14*r*r

    else:
        return "Invalid input"

choice=input("Enter the shape you want to find the area of :").lower()
result=area(choice)

if result=="Invalid input":
    print(result)
else:
    print("Area =",result)