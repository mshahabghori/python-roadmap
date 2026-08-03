numbers = list(map(int, input("Enter numbers: ").split()))
size = len(numbers)

for i in range(size - 1):
    smallest = i

    for j in range(i + 1, size):

        if numbers[j] < numbers[smallest]:
            smallest = j

    numbers[i], numbers[smallest] = numbers[smallest], numbers[i]

print("Sorted List:", numbers)