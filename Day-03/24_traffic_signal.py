light=str(input("Enter the colour of the light"))
light=light.lower()
if light=="red":
    print("STOP")
elif light=="green":
    print("GO")
elif light=="yellow":
    print("WATCHOUT")
else:
    print("Invalid Colour")
