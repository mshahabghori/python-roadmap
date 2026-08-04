words=input("Enter your sentence :").replace(" ", "").upper()
character_counter={}
for character in words:
    if character in character_counter:
        character_counter[character]=character_counter[character]+1
    else:
        character_counter[character]=1
print("The Total characters recieved are")
for key,value in character_counter.items():
    print(key,":",value)