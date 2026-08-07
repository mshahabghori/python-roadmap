sentence=input("Enter a sentence : ")
word=input("Enter word to search : ")

print("Position of word =", sentence.find(word))
print("Number of times it appears =", sentence.count(word))
print("Does sentence start with the word? =", sentence.startswith(word))
print("Does sentence end with the word? =", sentence.endswith(word))