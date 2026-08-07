word = input("Enter a word :")

print("Length of the string is =", len(word))
print("Uppercase =", word.upper())
print("Lowercase =", word.lower())
print("Title Case =", word.title())
print("First character =", word[0])
print("Last character =", word[-1])
print("First 3 characters =", word[0:3:1])

choice = input("Enter a character :")
print(f"The count of {choice} in {word} is =", word.count(choice))