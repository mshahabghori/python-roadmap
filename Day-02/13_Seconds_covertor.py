sec=float(input("Enter time in seconds"))
hours=sec//(60*60) #calc the hours
remaining=sec%(60*60) #calc the remaining seconds 
minutes=remaining//(60) #gvs the minutes
seconds=remaining%60 #gvs the seconds
print(f"Hours={hours},Minutes={minutes},Seconds={seconds}")