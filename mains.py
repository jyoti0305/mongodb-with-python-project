from models import add_book, view_books, update_book, delete_book, search_book

while True:
    print("\n Bookstore Menu")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Update Book")
    print("5. Delete Book")
    print("6. Exit")

    choice = input("Choose an option: ")

    if choice == '1':
        add_book()
    elif choice == '2':
        view_books()
    elif choice == '3':
        search_book()
    elif choice == '4':
        update_book()
    elif choice == '5':
        delete_book()
    elif choice == '6':
        print("Goodbye!")
        break
    else:
        print("Invalid choice, try again.")
