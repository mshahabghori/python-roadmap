P,R,T=map(float,input("Enter Principal ,ROI and Time in years").split())
SI=(P*R*T)/100
Total=P+SI
print("Simple Interest=",SI)
print("Total Amount=",Total)