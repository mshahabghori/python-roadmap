a=input("Enter your sentence ").lower().split()
frequency={}
for word in a:
    if word in frequency:
        frequency[word]=frequency[word]+1
    else:
        frequency[word]=1
for key,value in frequency.items():
    print(key,":",value)