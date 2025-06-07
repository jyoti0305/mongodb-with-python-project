from db import books
import csv

def add_book():
    try:
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
        print("✅ Book added!")
    except ValueError:
        print("❌ Invalid input for price or stock.")

def view_books():
    all_books = books.find()
    for book in all_books:
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
    try:
        price = float(input("New price: "))
        stock = int(input("New stock: "))
        result = books.update_one(
            {"title": title},
            {"$set": {"price": price, "stock": stock}}
        )
        if result.modified_count:
            print("✅ Book updated!")
        else:
            print("❌ No matching book found.")
    except ValueError:
        print("❌ Invalid input for price or stock.")

def delete_book():
    title = input("Enter title of the book to delete: ")
    result = books.delete_one({"title": title})
    if result.deleted_count:
        print("✅ Book deleted!")
    else:
        print("❌ No matching book found.")

def export_books_to_csv():
    try:
        cursor = books.find()
        with open("books_export.csv", mode="w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=["title", "author", "genre", "price", "stock"])
            writer.writeheader()
            for book in cursor:
                book.pop("_id", None)
                writer.writerow(book)
        print("✅ Exported to 'books_export.csv'")
    except Exception as e:
        print("❌ Failed to export:", e)
