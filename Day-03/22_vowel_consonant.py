alpha=str(input("Enter a letter "))
alpha_new=alpha.lower()
check=['a','e','i','o','u']
if alpha_new in check:
    print("Its a vowel")
else:
    print("Its a consonant")