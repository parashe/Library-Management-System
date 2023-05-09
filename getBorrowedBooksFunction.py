from tkinter import *
from tkinter import messagebox
import sqlite3
from datetime import date, timedelta
import tkinter as tk
from tkinter import ttk

# this  modeule gets the borrowed according to userid for  user to view their borrowed books
# this module also gets all borrowed list  with user id for librarian to view all borrowed books and user id


# this function get borrowed books by user id
# this function is used by  student staff

def get_borrowed_book_by_UserID(UserID):

    # connecting to database
    conn = sqlite3.connect('library.db')
    cursorObject = conn.cursor()
    try:
        with conn:
            cursorObject.execute(
                'SELECT * FROM borrowed_books WHERE UserID = ?', (UserID,))
            borrowed_books = cursorObject.fetchall()

            # passing the borrowed_books to get_all_book_ui function
            get_borrowed_book_by_UserID_ui(borrowed_books)

    except Exception as e:
        print("Failed to get borrowed books", e)

        messagebox.showinfo("Error", "Failed to get borrowed books")

# this functions get the all borrowed books by user
# this function is viwed by librarian


# this function get all borrowed books
def get_all_borrowed_books():

    # connecting to database
    conn = sqlite3.connect('library.db')
    cursorObject = conn.cursor()
    try:
        with conn:
            cursorObject.execute(
                'select * from borrowed_books')
            all_borrowed_books = cursorObject.fetchall()

            # passing the all_borrowed_books to get_all_borrowed_book_ui function
            get_all_borrowed_book_ui(all_borrowed_books)
    except Exception as e:
        print("Failed to get Borrowed books", e)

        messagebox.showinfo("Error", "Failed to get Borrowed books")


# this gives the gui for all borrowed books
def get_all_borrowed_book_ui(all_borrowed_books):

 # creating  new instance of a Tkinter
    get_availableBook = tk.Tk()

    # set the title, size, background color and disable the resizing property of the window
    get_availableBook.title("Library Management System ")
    get_availableBook.geometry("600x400")
    get_availableBook.config(bg="gray")

    # Create a frame to hold the widgets
    # fetching the all borrowed books from the borrowed_books table and displaying it in the Table
    tk.Label(get_availableBook, text="All Borrowed Books", font=("Times", "14", "bold "),
             pady=10, bg="gray").pack()

    frame = tk.Frame(get_availableBook, bg="gray")
    frame.pack(pady=5)
    table = ttk.Treeview(frame)
    table['columns'] = ('ISBN', 'UserID', 'status',
                        'borrow_date', 'due_date')
    table.column('#0', minwidth=0, width=0, stretch=NO)
    table.heading('ISBN', text='ISBN')
    table.column('ISBN', width=50)
    table.heading('UserID', text='UserID')
    table.column('UserID', width=75)
    table.heading('status', text='Status')
    table.column('status', width=75)
    table.heading('borrow_date', text='borrow_date')
    table.column('borrow_date', width=100)
    table.heading('due_date', text='due_date')
    table.column('due_date', width=100)

    # looping through the all borrowed books and inserting it into the table
    for borrowed_books in all_borrowed_books:
        table.insert('', 'end', text='', value=(
            borrowed_books[2], borrowed_books[1], borrowed_books[5], borrowed_books[3], borrowed_books[6]))
        style = ttk.Style()
        style.configure('Treeview.Heading', font=("Times", "12", "bold "))
        style.configure('Treeview', font=("Times", "10"), rowheight=25)

    table.pack(pady=20)
    get_availableBook.mainloop()


# this gives the gui for borrowed books by user id
def get_borrowed_book_by_UserID_ui(borrowed_books):

 # creating  new instance of a Tkinter
    get_availableBook = tk.Tk()

    # set the title, size, background color and disable the resizing property of the window
    get_availableBook.title("Library Management System ")
    get_availableBook.geometry("600x400")
    get_availableBook.config(bg="gray")

    # Create a frame to hold the widgets
    # fetching the borrowed books data from the borrowed_books table and displaying it in the Table
    tk.Label(get_availableBook, text="My Borrowed Books", font=("Times", "14", "bold "),
             pady=10, bg="gray").pack()

    frame = tk.Frame(get_availableBook, bg="gray")
    frame.pack(pady=5)
    table = ttk.Treeview(frame)
    table['columns'] = ('ISBN', 'UserID', 'status',
                        'borrow_date', 'due_date')
    table.column('#0', minwidth=0, width=0, stretch=NO)
    table.heading('ISBN', text='ISBN')
    table.column('ISBN', width=50)
    table.heading('UserID', text='UserID')
    table.column('UserID', width=75)
    table.heading('status', text='Status')
    table.column('status', width=75)
    table.heading('borrow_date', text='borrow_date')
    table.column('borrow_date', width=100)
    table.heading('due_date', text='due_date')
    table.column('due_date', width=100)

    # looping through the borrowed books and inserting it into the table
    for books in borrowed_books:
        table.insert('', 'end', text='', value=(
            books[2], books[1], books[5], books[3], books[6]))
        style = ttk.Style()
        style.configure('Treeview.Heading', font=("Times", "12", "bold "))
        style.configure('Treeview', font=("Times", "10"), rowheight=25)

    table.pack(pady=20)
    get_availableBook.mainloop()
