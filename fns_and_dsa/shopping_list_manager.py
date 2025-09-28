def display_menu():
    print("Shopping list manager")
    print("1. Add item")
    print("2. Remove item")
    print("3. View list")
    print("4. Exit")

shopping_list = []
while true:
    display_menu()
    choice = input("Enter your choice: ")
    if choice == 1:
        item_name = input("Enter the itemt to add: ")
        shopping_list.append(item_name)
        pass
    elif choice == 2:
        item_removed = input("Enter item to remove: ")
        shopping_list.append(item_removed)
        pass
    elif choice == 3:
        shopping_list = []
        pass
    elif choice == 4:
        print("Goodbye")
        break
    else:
        print("Invalid choice. Try again")
