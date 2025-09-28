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
        item = input("Enter the item to add: ")
        shopping_list.append(item)
        pass
    elif choice == 2:
        item = input("Name the item to be removed: ")
        shopping_list.append(item)
        pass
    elif choice == 3:
        shopping_list = []
        pass
    elif choice == 4:
        print("Goodbye")
        break
    else:
        print("Invalid choice. Try again")
