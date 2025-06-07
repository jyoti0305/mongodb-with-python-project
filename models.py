from db import books

def add_book():
    title = input("Title: ")
    author = input("Author: ")
    genre = input("Genre: ")
    price = float(input("Price: "))
    stock = int(input("Stock: "))

    book = {
        "title": title,
        "author": author,
        "genre": genre,
        "price": price,
        "stock": stock
    }

    books.insert_one(book)
    print("Book added!")

def view_books():
    for book in books.find():
        print(book)

def search_book():
    query = input("Enter title or author to search: ")
    results = books.find({
        "$or": [
            {"title": {"$regex": query, "$options": "i"}},
            {"author": {"$regex": query, "$options": "i"}}
        ]
    })
    found = False
    for book in results:
        print(book)
        found = True
    if not found:
        print("No books found.")

def update_book():
    title = input("Enter title of the book to update: ")
    price = float(input("New price: "))
    stock = int(input("New stock: "))
    result = books.update_one(
        {"title": title},
        {"$set": {"price": price, "stock": stock}}
    )
    if result.modified_count:
        print("Book updated!")
    else:
        print("No matching book found.")

def delete_book():
    title = input("Enter title of the book to delete: ")
    result = books.delete_one({"title": title})
    if result.deleted_count:
        print("Book deleted!")
    else:
        print("No matching book found.")

