from models import (
    add_book,
    view_books,
    search_book,
    update_book,
    delete_book,
    export_books_to_csv
)
from utils import display_menu

while True:
    display_menu()
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
        export_books_to_csv()
    elif choice == '7':
        print("Goodbye!")
        break
    else:
        print("Invalid choice, try again.")


