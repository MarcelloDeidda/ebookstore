# This program manages the database of a bookshop. It imports "ebookstore_functions.py"
# from the same folder and uses its functions to interact to the database, which is
# "ebookstore.db".

import ebookstore_functions as book

# Define main menu
menu = """1. Show all books
2. Search book by title
3. Add book
4. Edit book
5. Delete book
6. Delete all books
7. Exit"""

# Define edit book menu
edit_menu = """
Select value to update:
1. Title
2. Author
3. Quantity
4. Price
5. Back to Main Menu"""

# Create table if not exists and populate if empty
book.create_table()
if book.count_books() == 0:
    book.seed_book()

# === START OF PROGRAM ===
print("\n=== Welcome to the EBookStore database ===\n")

while True:
    # Show main menu and get user choice
    print(menu)
    action = input(": ")

    # Show all books
    if action == "1":
        book.show_all_books()
    
    # Search books by title
    elif action == "2":
        title = input("\nEnter title: ")
        book.show_book_by_title(title)
    
    # Create new book
    elif action == "3":
        # Get info from user input. Quantity must be int, price must be float.
        while True:
            title = input("\nTitle:\t")
            author = input("Author:\t")

            try:
                quantity = int(input("Qty:\t"))
                price = float(input("Price:\t"))
            except ValueError:
                print("Please enter valid quantity and price!")
                continue
            
            # Check that strings aren't empty and numeric values are greater than zero
            if title.strip() == "" or author.strip() == "":
                print("Title and author cannot be blank!")
            elif quantity < 0 or price < 0:
                print("Quantity and price cannot be smaller than zero!")
            else:
                break

        # Confirm action
        confirm = input("\nDo you want to save this book? ").lower()

        if confirm in ["yes", "y"]:
            # Add book to database
            book.add_book(title, author, quantity, price)
        else:
            print()

    # Edit book
    elif action == "4":
        back = False
        while True:
            # Get book info from input
            title = input("\nTitle (or \"-1\" for main menu):  ")
            if title == "-1":
                back = True
                break

            author = input("Author (or \"-1\" for main menu): ")
            if author == "-1":
                back = True
                break

            # Search for book in database
            book_exists = book.book_exists(title, author)

            if book_exists:
                break
            else:
                print("Couldn't find this book in the database!")
        
        # Back to main menu
        if back:
            print()
            continue

        # Show book info
        print(f"\nTitle:\t{book_exists[1]}")
        print(f"Author:\t{book_exists[2]}")
        print(f"Qty:\t{book_exists[3]}")
        print(f"Price:\t{book_exists[4]}")

        while True:
            # Show Edit Options: Title, Author, Quantity, Price
            print(edit_menu)
            edit_action = input(": ")

            # Edit Title
            if edit_action == "1":
                while True:
                    new_title = input("\nEnter new title: ")
                    # Title can't be blank
                    if new_title.strip() == "":
                        print("Title cannot be blank!")
                        continue
                    book.edit_title(title, author, new_title)
                    break
                break
            
            # Edit Author
            elif edit_action == "2":
                while True:
                    new_author = input("\nEnter new author: ")
                    # Author can't be blank
                    if new_author.strip() == "":
                        print("Author cannot be blank!")
                        continue
                    book.edit_author(title, author, new_author)
                    break
                break

            # Edit Quantity
            elif edit_action == "3":
                while True:
                    try:
                        new_quantity = int(input("\nEnter quantity: "))
                        # Quantity can't be negative
                        if new_quantity < 0:
                            print("Quantity can't be negative!")
                            continue
                        book.edit_quantity(title, author, new_quantity)
                        break
                    # Handle non numeric value
                    except ValueError:
                        print("Enter correct value!")
                break

            # Edit Price
            elif edit_action == "4":
                while True:
                    try:
                        new_price = float(input("\nEnter price: "))
                        # Price can't be negative
                        if new_price < 0:
                            print("Price can't be negative!")
                            continue
                        book.edit_price(title, author, new_price)
                        break
                    # Handle non numeric value
                    except ValueError:
                        print("Enter correct value!")
                break

            # Back to main menu
            elif edit_action == "5":
                print()
                break
            
            # Handle incorrect input
            else:
                print("\nInvalid input!")

    # Delete book
    elif action == "5":
        back = False
        while True:
            # Get book info from input
            title = input("\nTitle (or \"-1\" for main menu):  ")
            if title == "-1":
                back = True
                break

            author = input("Author (or \"-1\" for main menu): ")
            if author == "-1":
                back = True
                break

            # Search for book in database
            book_exists = book.book_exists(title, author)

            if book_exists:
                break
            else:
                print("Couldn't find this book in the database!")
        
        # Back to main menu
        if back:
            print()
            continue
        
        # Show book info
        print(f"\nTitle:\t{book_exists[1]}")
        print(f"Author:\t{book_exists[2]}")
        print(f"Qty:\t{book_exists[3]}")
        print(f"Price:\t{book_exists[4]}")

        # Confirm action
        confirm = input("\nDo you want to delete this book? This action cannot be reversed: ").lower()

        if confirm in ["yes", "y"]:
            book.delete_book(title, author)
        else:
            print()

    # Delete all books
    elif action == "6":
        confirm = input("\nDo you want to delete all records? This action cannot be reversed: ").lower()

        if confirm in ["yes", "y"]:
            book.delete_all_books()
        else:
            print()
    
    # Exit program
    elif action == "7":
        print("\nGoodbye!\n")
        exit()

    # Handle incorrect input
    else:
        print("\nIncorrect input!\n")
        