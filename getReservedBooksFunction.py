from tkinter import *
from tkinter import messagebox
import sqlite3
import tkinter as tk
from tkinter import ttk

# this modules gets the reserved books according to userid for user to view their reserved books
# this module also gets all reserved list with user id for librarian to view all reserved books and user id

# This function is called in studentstaffAction.py
# this gives the reserved books by user id


def get_reserved_book_by_UserID(UserID):
    # connecting to database
    conn = sqlite3.connect('library.db')
    cursorObject = conn.cursor()
    try:
        with conn:
            print('UserID', UserID)
            cursorObject.execute(
                "SELECT * FROM ReservedBook WHERE UserID = ?", (UserID,))
            reserved_books = cursorObject.fetchall()
            print('reserved_books', reserved_books)

            # passing the reserved_books to get_reserved_book_by_UserID_ui function
            get_reserved_book_by_UserID_ui(reserved_books)

    except Exception as e:
        print("Failed to get reserved books", e)

        messagebox.showinfo("Error", "Failed to get reserved books")


# this function gets all reserved books
# it select all the reserved books from the database
# and display it in Gui table

def get_all_reserved_books():
    # connecting to database
    conn = sqlite3.connect('library.db')
    cursorObject = conn.cursor()
    try:
        with conn:
            cursorObject.execute(
                'select * from ReservedBook')
            all_reserved_books = cursorObject.fetchall()

            # passing the all_reserved_books to get_all_reserved_book_ui function
            get_all_reserved_book_ui(all_reserved_books)
    except Exception as e:
        print("Failed to get reserved books", e)

        messagebox.showinfo("Error", "Failed to get reserved books")


# this function gives the gui for all reserved books
# and gets the data from get_all_reservedbook_by_UserID function
def get_reserved_book_by_UserID_ui(reserved_books):

 # creating  new instance of a Tkinter
    get_reservedBook = tk.Tk()

    # set the title, size, background color and disable the resizing property of the window
    get_reservedBook.title("Library Management System ")
    get_reservedBook.geometry("600x400")
    get_reservedBook.config(bg="gray")

    # Create a frame to hold the widgets
    # fetching the reserved books data from the ReservedBook table and displaying it in the Table
    tk.Label(get_reservedBook, text="My Reserved Books", font=("Times", "14", "bold "),
             pady=10, bg="gray").pack()

    frame = tk.Frame(get_reservedBook, bg="gray")
    frame.pack(pady=5)
    table = ttk.Treeview(frame)
    table['columns'] = ('ISBN', 'UserID', 'reserved_status',
                        'reserved_date')
    table.column('#0', minwidth=0, width=0, stretch=NO)
    table.heading('ISBN', text='ISBN')
    table.column('ISBN', width=50)
    table.heading('UserID', text='UserID')
    table.column('UserID', width=75)
    table.heading('reserved_status', text='reserved_status')
    table.column('reserved_status', width=75)
    table.heading('reserved_date', text='Reserved_date')
    table.column('reserved_date', width=100)

    # looping through the reserved_books and inserting it into the table
    for books in reserved_books:
        table.insert('', 'end', text='', value=(
            books[1],  books[4], books[3], books[2]))
        style = ttk.Style()
        style.configure('Treeview.Heading', font=("Times", "12", "bold "))
        style.configure('Treeview', font=("Times", "10"), rowheight=25)

    table.pack(pady=20)
    get_reservedBook.mainloop()


def get_all_reserved_book_ui(all_reserved_books):

 # creating  new instance of a Tkinter
    get_reservedBook = tk.Tk()

    # set the title, size, background color and disable the resizing property of the window

    get_reservedBook.title("Library Management System ")
    get_reservedBook.geometry("600x400")
    get_reservedBook.config(bg="gray")

    # Create a frame to hold the widgets
    # fetching the all reserved books  according to UserID from the ReservedBook table and displaying it in the Table
    tk.Label(get_reservedBook, text="All Reserved Books", font=("Times", "14", "bold "),
             pady=10, bg="gray").pack()

    frame = tk.Frame(get_reservedBook, bg="gray")
    frame.pack(pady=5)
    table = ttk.Treeview(frame)
    table['columns'] = ('ISBN', 'UserID', 'reserved_status',
                        'reserved_date')
    table.column('#0', minwidth=0, width=0, stretch=NO)
    table.heading('ISBN', text='ISBN')
    table.column('ISBN', width=50)
    table.heading('UserID', text='UserID')
    table.column('UserID', width=75)
    table.heading('reserved_status', text='Status')
    table.column('reserved_status', width=75)
    table.heading('reserved_date', text='Reserved_date')
    table.column('reserved_date', width=100)

    # looping through the all_reserved_books and inserting it into the table
    for books in all_reserved_books:
        table.insert('', 'end', text='', value=(
            books[1], books[3], books[2], books[4], ))
        style = ttk.Style()
        style.configure('Treeview.Heading', font=("Times", "12", "bold "))
        style.configure('Treeview', font=("Times", "10"), rowheight=25)

    table.pack(pady=20)
    get_reservedBook.mainloop()
