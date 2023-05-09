
import sqlite3
import tkinter.messagebox as messagebox

# this function creates the table for the database
# this function is created when  login window is opened


def create_tables():

    conn = sqlite3.connect("library.db")
    # Create c object
    cursorObject = conn.cursor()

    try:
        with conn:

            # Create Users table
            cursorObject.execute("""CREATE TABLE IF NOT EXISTS Users (
                                        UserID TEXT PRIMARY KEY,
                                        Name TEXT,
                                        Password TEXT,
                                        UserType TEXT,
                                        DeptOrClass TEXT)""")

            cursorObject.execute("""CREATE TABLE IF NOT EXISTS borrowed_books (
            borrow_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE ,
            UserID TEXT,
            isbn TEXT,
            borrow_date TEXT,
            returned Boolean,
            status TEXT,
            due_date TEXT,
            FOREIGN KEY (UserID) REFERENCES Users (UserID),
            FOREIGN KEY (isbn) REFERENCES Books (isbn)
            
            )""")
            cursorObject.execute("""CREATE TABLE IF NOT EXISTS ReservedBook (
            reserved_book_id  INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE ,
            isbn TEXT,
            reserved_date TEXT,
            reserved_status TEXT,
            UserID TEXT,
            FOREIGN KEY (isbn) REFERENCES Users (isbn),
            FOREIGN KEY (UserID) REFERENCES Users (UserID)

        )""")

            cursorObject.execute("""CREATE TABLE IF NOT EXISTS Account (
            account_id  INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE ,
            no_borrowed_books integer,
            no_reserved_books integer,
            no_returned_books integer,
            no_lost_books integer ,
            fine_amount REAL,
            UserID TEXT,
            FOREIGN KEY (UserID) REFERENCES Users (UserID)

        )""")
            cursorObject.execute("""CREATE TABLE IF NOT EXISTS  category(
                    category_id integer PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE ,
                    category text
                    )""")

            cursorObject.execute("""CREATE TABLE IF NOT EXISTS  books(
                    isbn text  PRIMARY KEY,
                    title text,
                    author text,
                    available integer,
                    published_date text,
                    category text
                    
                    )""")

    except Exception as e:
        print("Failed to create tables", e)

        messagebox.showinfo("Error", "Failed to create tables")

    conn.commit()
    cursorObject.close()
