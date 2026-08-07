names = input("Enter student names : ").split()
marks = list(map(int, input("Enter marks : ").split()))

for number, name in enumerate(names, start=1):
    print("Student", number, ":", name)

print("Sorted marks =", sorted(marks))