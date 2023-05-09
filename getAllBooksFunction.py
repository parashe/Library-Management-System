from tkinter import *
from tkinter import messagebox
import sqlite3
import tkinter as tk
from tkinter import ttk


# this function gets the borrowed books
# this function is used by  student staff and librarian to view list of books
# this function is called in studentstaffAction.py and LibDatabaseClass.py
# this function simply gets all data from books table and displays in the  GUI using table


def get_all_book():
    # connecting to database.
    conn = sqlite3.connect('library.db')
    cursorObject = conn.cursor()
    try:
        with conn:
            cursorObject.execute("SELECT * FROM books")
            books = cursorObject.fetchall()

            # passing the books to get_all_book_ui function
            get_all_book_ui(books)

    except Exception as e:
        print("Failed to get  books", e)

        messagebox.showinfo("Error", "Failed to get  books")


def get_all_book_ui(books):

 # creating  new instance of a Tkinter
    get_availableBook = tk.Tk()

    get_availableBook.title("Library Management System ")
    get_availableBook.geometry("800x400")
    get_availableBook.config(bg="gray")

    # Create a frame to hold the widgets
    # fetching the data from the Books table and displaying it in the Table
    tk.Label(get_availableBook, text="All Books List", font=("Times", "14", "bold "),
             pady=10, bg="gray").pack()

    frame = tk.Frame(get_availableBook, bg="gray")
    frame.pack(pady=5)
    table = ttk.Treeview(frame)
    table['columns'] = ('ISBN', 'Title', 'Category', 'Author',
                        'Available', 'published_date')
    table.column('#0', minwidth=0, width=0, stretch=NO)
    table.heading('ISBN', text='ISBN')
    table.column('ISBN', width=50, anchor='w')
    table.heading('Title', text='Title')
    table.column('Title', width=100)
    table.heading('Author', text='Author')
    table.column('Author', width=100)
    table.heading('Available', text='Available')
    table.column('Available', width=100)
    table.heading('Category', text='Category')
    table.column('Category', width=100)
    table.heading('published_date', text='published_date')
    table.column('published_date', width=100)

    # looping through the books and inserting it into the table
    for book in books:
        table.insert('', 'end', text='', values=(
            book[0], book[1], book[5], book[2], book[3], book[4]))
        style = ttk.Style()
        style.configure('Treeview.Heading', font=("Times", "12", "bold "))
        style.configure('Treeview', font=("Times", "10"), rowheight=25)

    table.pack(pady=20)
    get_availableBook.mainloop()
