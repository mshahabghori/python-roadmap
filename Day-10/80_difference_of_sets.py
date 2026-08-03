a=list(map(int,input("Enter your numbers").split()))
b=list(map(int,input("Enter your numbers").split()))
new_a=set(a)
new_b=set(b)
diff_set_a=new_a.difference(new_b)
diff_set_b=new_b.difference(new_a)

print("Difference of 1st set =",diff_set_a)
print("Difference of 2nd set =",diff_set_b)