votes=input("Who do you want to vote for ").upper().split()
vote_counter={}
for vote in votes:
    if vote in vote_counter:
        vote_counter[vote]=vote_counter[vote]+1
    else:
        vote_counter[vote]=1
print("The Total votes recieved are")
for key,value in vote_counter.items():
    print(key,":",value)