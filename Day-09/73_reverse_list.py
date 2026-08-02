a=list(map(int,input("Enter your numbers ").split()))
rev=[]
for number in range(len(a)-1,-1,-1):
    rev.append(a[number])
print(rev)