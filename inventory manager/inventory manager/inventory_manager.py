inventory = {}

print("-----Personal Inventory Manager-----")

while True:
    print("\nOptions: [1] Add [2] Remove [3] List [4] Exit")
    choice = input("Select an option (1-4): ")
    if choice == "1":
        name = input("Enter item name: ").strip().capitalize()
        qty = int(input(f"How many {name}s?: "))
        inventory[name] = inventory.get(name, 0) + qty
    elif choice == "2":
        name = input("What item would you like to remove?: ").strip().capitalize()
        if name in inventory:
            del inventory[name]
            print(f"Removed {name} from inventory.")
    elif choice == "3":
        print("______Current Inventory______")
        for item, qty in inventory.items():
            print(f"- {item}: {inventory[item]}")
        print("_____________________________")
    elif choice == "4":
        print("Exiting... Goodbye!")
        break
    else:
        break