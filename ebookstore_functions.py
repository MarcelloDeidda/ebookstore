# This file contains functions to be exported to the main program, which
# is "ebookstore.py". All the functions connect to "ebookstore_db" and
# perform CRUD operation on book database.

import sqlite3

# This list contains values to populate database
seeds = [
    ["A Tale of Two Cities", "Charles Dickens", 30, 10.99],
    ["Harry Potter and the Philosopher's Stone", "J.K. Rowling", 40, 8.99],
    ["The Lion, the Witch and the Wardrobe", "C.S. Lewis", 25, 9.99],
    ["The Lord of the Rings", "J.R.R. Tolkien", 37, 9.99],
    ["Alice in Wonderland", "Lewis Carroll", 12, 8.99]
]


# This function creates a table to store data about books
def create_table():
    try:
        # Connect database and create table
        db = sqlite3.connect("ebookstore_db")
        cursor = db.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS books(
        id INTEGER PRIMARY KEY,
        title TEXT,
        author TEXT,
        quantity INTEGER,
        price FLOAT
        );""")
        db.commit()

    except Exception as e:
        db.rollback()
        print(e, "\n")

    finally:
        db.close()


# This function populates the database with values from the list seeds
def seed_book():
    try:
        # Connect database and insert many books
        db = sqlite3.connect("ebookstore_db")
        cursor = db.cursor()
        cursor.executemany("""
        INSERT INTO books(title, author, quantity, price)
        VALUES (?, ?, ?, ?);
        """, seeds)
        db.commit()

    except Exception as e:
        db.rollback()
        print(e, "\n")

    finally:
        db.close()


# This function adds a book to the database
def add_book(title, author, quantity, price):
    try:
        # Connect database and insert book
        db = sqlite3.connect("ebookstore_db")
        cursor = db.cursor()
        cursor.execute("""
        INSERT INTO books(title, author, quantity, price)
        VALUES (?, ?, ?, ?);
        """, [title, author, quantity, price])
        db.commit()
        print("Book successfully added to the database!\n")

    except Exception as e:
        db.rollback()
        print(e, "\n")

    finally:
        db.close()


# This function updates the title of a book
def edit_title(title, author, value):
    try:
        # Connect database and execute query
        db = sqlite3.connect("ebookstore_db")
        cursor = db.cursor()
        cursor.execute("""
        UPDATE books
        SET title = ?
        WHERE title LIKE ? AND author LIKE ?;
        """, [value, title, author])
        db.commit()
        print("The database has been updated!\n")

    except Exception as e:
        db.rollback()
        print(e, "\n")

    finally:
        db.close()


# This function updates the author of a record
def edit_author(title, author, value):
    try:
        # Connect database and execute query
        db = sqlite3.connect("ebookstore_db")
        cursor = db.cursor()
        cursor.execute("""
        UPDATE books
        SET author = ?
        WHERE title LIKE ? AND author LIKE ?;
        """, [value, title, author])
        db.commit()
        print("The database has been updated!\n")

    except Exception as e:
        db.rollback()
        print(e, "\n")

    finally:
        db.close()


# This function updates the quantity of a record
def edit_quantity(title, author, value):
    try:
        # Connect database and execute query
        db = sqlite3.connect("ebookstore_db")
        cursor = db.cursor()
        cursor.execute("""
        UPDATE books
        SET quantity = ?
        WHERE title LIKE ? AND author LIKE ?;
        """, [value, title, author])
        db.commit()
        print("The database has been updated!\n")

    except Exception as e:
        db.rollback()
        print(e, "\n")

    finally:
        db.close()


# This function updates the price of a record
def edit_price(title, author, value):
    try:
        # Connect database and execute query
        db = sqlite3.connect("ebookstore_db")
        cursor = db.cursor()
        cursor.execute("""
        UPDATE books
        SET price = ?
        WHERE title LIKE ? AND author LIKE ?;
        """, [value, title, author])
        db.commit()
        print("The database has been updated!\n")

    except Exception as e:
        db.rollback()
        print(e, "\n")

    finally:
        db.close()


# This function deletes a book
def delete_book(title, author):
    try:
        # Connect database and delete book
        db = sqlite3.connect("ebookstore_db")
        cursor = db.cursor()
        deleted_book = cursor.execute("""
        DELETE FROM books
        WHERE title LIKE ? and author LIKE ?;
        """, (title, author))
        db.commit()
        print("Book successfully deleted!\n")

    except Exception as e:
        db.rollback()
        print(e, "\n")

    finally:
        db.close()


# This function deletes all records
def delete_all_books():
    try:
        # Connect database and delete all books
        db = sqlite3.connect("ebookstore_db")
        cursor = db.cursor()
        cursor.execute("""
        DELETE FROM books;
        """)
        db.commit()
        print("The database is empty!\n")

    except Exception as e:
        db.rollback()
        print(e, "\n")

    finally:
        db.close()


# This function searches for a book by title
def show_book_by_title(title):
    try:
        # Connect database and execute query
        db = sqlite3.connect("ebookstore_db")
        cursor = db.cursor()
        cursor.execute("""
        SELECT * FROM books
        WHERE title LIKE ?;
        """, ([f"%{title}%"]))

        # Handle no book found
        book = cursor.fetchall()
        if not book:
            print("Couldn't find this book!\n")

        # Print books found
        else:
            for row in book:
                print(f"\nTitle:\t{row[1]}")
                print(f"Author:\t{row[2]}")
                print(f"Qty:\t{row[3]}")
                print(f"Price:\t{row[4]}")
            print()

    except Exception as e:
        print(e, "\n")

    finally:
        db.close()


# This function shows all books in database
def show_all_books():
    try:
        # Connect database and execute query
        print("\nFetching all the books from the database...")
        db = sqlite3.connect("ebookstore_db")
        cursor = db.cursor()
        cursor.execute("""
        SELECT * FROM books ORDER BY title;
        """)

        # Handle no book found
        books = cursor.fetchall()
        if not books:
            print("Couldn't find any book!\n")

        # Print books found
        else:
            for row in books:
                print(f"\nTitle:\t{row[1]}")
                print(f"Author:\t{row[2]}")
                print(f"Qty:\t{row[3]}")
                print(f"Price:\t{row[4]}")
            print()

    except Exception as e:
        print(e, "\n")
    finally:
        db.close()


# This function checks for book record in database
def book_exists(title, author):
    try:
        # Connect database and execute query
        db = sqlite3.connect("ebookstore_db")
        cursor = db.cursor()
        cursor.execute("""
        SELECT * FROM books
        WHERE title LIKE ? and author LIKE ?;
        """, (title, author))

        # Handle no book found
        book = cursor.fetchone()
        if not book:
            return False

        # Return book found
        else:
            return book

    except Exception as e:
        print(e, "\n")

    finally:
        db.close()


# This function counts all the books in database
def count_books():
    try:
        # Connect database and count books
        db = sqlite3.connect("ebookstore_db")
        cursor = db.cursor()
        cursor.execute("""
        SELECT * FROM books;
        """)

        # Return result
        book_count = len(cursor.fetchall())
        return book_count

    except Exception as e:
        print(e, "\n")

    finally:
        db.close()


# This function deletes table from database
def delete_table():
    try:
        # Connect database and drop table
        db = sqlite3.connect("ebookstore_db")
        cursor = db.cursor()
        cursor.execute("""
        DROP TABLE books;
        """)
        db.commit()

    except Exception as e:
        db.rollback()
        print(e, "\n")

    finally:
        db.close()
