names = list(map(str, input("Enter name : ").split()))
marks = list(map(int, input("Enter marks : ").split()))
for name,mark in zip(names,marks):
    print(name , ":" ,mark)