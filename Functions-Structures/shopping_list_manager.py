def display_menu():
    print("Shopping List Manager")
    print("1. Add item")
    print("2. Remove item")
    print("3. View shopping list")
    print("4. Exit")
display_menu()

def main():
    shopping_list = []
    while True:
        try:
            choice = int(input("Enter choice: "))
        except ValueError:
            print("Invalid input. Try again!")
            continue

        if choice == 1:
            item = input("Enter item to add: ").strip().lower()
            if item in shopping_list:
                print(f"{item} is already on the list. Add another item.")
            else:
                shopping_list.append(item)
        elif choice == 2:
            item = input("Enter item to remove from the list: ").strip().lower()
            if item in shopping_list:
                shopping_list.remove(item)
            else:
                print(f"{item} is not on the list.")
        elif choice == 3:
            if shopping_list:
                print("Here is your list!")
                for i, item in enumerate(shopping_list, start=1):
                    print(f"{i}.{item}")
            else:
                print("Your shopping list is empty.")
        elif choice == 4:
            print("Exiting the Shopping list manager. Goodbye!")
            break
        else:
            print("Invalid choice. Try again!")
            
if __name__ == "__main__":
    main()
