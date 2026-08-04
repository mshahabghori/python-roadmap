inventory = {
    "pen": 25,
    "book": 10,
    "laptop": 1
}
choice=input("Enter the item you want to search ").lower()
print
for key,value in inventory:
    print(key,":",value)


if choice in inventory:
    add_new=int(input(f"Enter the quantity u want to add to the {choice}"))
    inventory[choice]=inventory[choice]+add_new
else:
        print("Item not found")
for key,value in inventory:
    print("Your updated inventory :\n",key,":",value)
