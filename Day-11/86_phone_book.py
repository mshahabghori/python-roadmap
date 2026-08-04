inventory = {
    "pen": 25,
    "book": 10,
    "laptop": 1
}

choice = input("Enter the item you want to search ").lower()
print("Your current inventory :")
for key, value in inventory.items():
    print(key, ":", value)

if choice in inventory:
    add_new = int(input(f"Enter the quantity you want to add to the {choice}: "))
    inventory[choice] = inventory[choice] + add_new
else:
    print("Item not found")

print("Your updated inventory :")
for key, value in inventory.items():
    print(key, ":", value)
