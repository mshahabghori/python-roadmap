#for rectangle
l,b=map(int,input("Enter length and breadth for rectangle").split())
#for circle
r=float(input("Enter radius"))
#calc of area
area_rec=l*b
area_cir=3.14*r*r
print(f"Area of rectangle={area_rec}\nArea of circle={area_cir}")