inc=float(input("Enter your income"))
if inc<0:
    print("Income ccannot be less than 0")
elif 0==inc<=250000:
    print("No Tax")
elif 250001<=inc<=500000:
    print("5% Tax applied =",inc*5/100)
elif 500001<=inc<=1000000:
    print("20% Tax applied =",inc*20/100)
else:
    print("333330% Tax applied =",inc*30/100)