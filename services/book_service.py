import uuid
from datetime import datetime
from utilities.json_handler import load_json, save_json, append_json
from os import remove

BOOKS_FOLDER = "data_storage/uploaded_books"


def upload_book(title, author, category, file_content, filename_extension=".txt"):
    book_id = str(uuid.uuid4())
    filename = f"{book_id}{filename_extension}"

    filepath = f"{BOOKS_FOLDER}/{filename}"
    with open(filepath, "w", encoding="utf-8") as file:
        file.write(file_content)

    book_record = {
        "id": book_id,
        "title": title,
        "author": author,
        "category": category,
        "filename": filename,
        "date_uploaded": datetime.now().isoformat(),
    }

    append_json("data_storage/books.json", book_record)

    return {"message": "Book uploaded successfully"}


def get_all_books():
    books = load_json("data_storage/books.json")

    safe_books = []
    for book in books:
        safe_book = {
            "id": book["id"],
            "title": book["title"],
            "author": book["author"],
            "category": book["category"],
            "date_uploaded": book["date_uploaded"],
        }
        safe_books.append(safe_book)

    return safe_books


def search_books(query, role):
    books = load_json("data_storage/books.json")

    search_term = query.lower()

    matching_books = []
    for book in books:
        title_match = search_term in book["title"].lower()
        author_match = search_term in book["author"].lower()

        if title_match or author_match:
            if role == "admin":
                safe_book = {
                    "id": book["id"],
                    "title": book["title"],
                    "author": book["author"],
                    "category": book["category"],
                    "date_uploaded": book["date_uploaded"],
                }
            else:
                safe_book = {
                    "title": book["title"],
                    "author": book["author"],
                    "category": book["category"],
                }
            matching_books.append(safe_book)

    return matching_books


def get_book_content(book_id):
    books = load_json("data_storage/books.json")

    matched_book = None
    for book in books:
        if book["id"] == book_id:
            matched_book = book
            break

    if matched_book is None:
        return {"message": "Book not found"}

    filepath = f"{BOOKS_FOLDER}/{matched_book['filename']}"
    with open(filepath, "r", encoding="utf-8") as file:
        content = file.read()

    return {
        "id": matched_book["id"],
        "title": matched_book["title"],
        "author": matched_book["author"],
        "category": matched_book["category"],
        "content": content,
    }


def get_book_content_by_title(title):
    books = load_json("data_storage/books.json")

    matched_book = None
    for book in books:
        if book["title"].lower() == title.lower():
            matched_book = book
            break

    if matched_book is None:
        return {"message": "Book not found"}

    filepath = f"{BOOKS_FOLDER}/{matched_book['filename']}"
    with open(filepath, "r", encoding="utf-8") as file:
        content = file.read()

    return {
        "title": matched_book["title"],
        "author": matched_book["author"],
        "category": matched_book["category"],
        "content": content,
    }

def update_book(book_id, title, author, category):
    books = load_json("data_storage/books.json")

    updated_books = []
    found = False
    for book in books:
        if book["id"] == book_id:
            updated_book = {
                "id": book["id"],
                "title": title,
                "author": author,
                "category": category,
                "filename": book["filename"],
                "date_uploaded": book["date_uploaded"],
            }
            updated_books.append(updated_book)
            found = True
        else:
            updated_books.append(book)

    if not found:
        return {"message": "Book not found"}

    save_json("data_storage/books.json", updated_books)

    return {"message": "Book updated successfully"}


def delete_book(book_id):
    books = load_json("data_storage/books.json")

    matched_book = None
    updated_books = []
    for book in books:
        if book["id"] == book_id:
            matched_book = book
        else:
            updated_books.append(book)

    if matched_book is None:
        return {"message": "Book not found"}

    filepath = f"{BOOKS_FOLDER}/{matched_book['filename']}"
    try:
        remove(filepath)
    except FileNotFoundError:
        pass

    save_json("data_storage/books.json", updated_books)

    return {"message": "Book deleted successfully"}