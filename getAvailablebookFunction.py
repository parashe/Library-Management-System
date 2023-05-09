from tkinter import *
from tkinter import messagebox
import sqlite3
import tkinter as tk
from tkinter import ttk


# This function is used by student / staff to view available books
# This function check the available column  if its greater than 0 then it will show the book is available
# using get_available_book_ui function in the table
# This function is called in studentstaffAction.py

def get_available_book():
    # connecting to database.
    conn = sqlite3.connect('library.db')
    cursorObject = conn.cursor()
    try:
        with conn:
            cursorObject.execute("SELECT * FROM books WHERE available > 0")
            available_books = cursorObject.fetchall()

            # passing the books to get_available_book_ui function
            get_available_book_ui(available_books)

    except Exception as e:
        print("Failed to get available books", e)

        messagebox.showinfo("Error", "Failed to get available books")


def get_available_book_ui(available_books):

 # creating  new instance of a Tkinter
    get_availableBook = tk.Tk()

    get_availableBook.title("Library Management System ")
    get_availableBook.geometry("600x400")
    get_availableBook.config(bg="gray")

    # Create a frame to hold the widgets
    # fetching the available books data from the Books table and displaying it in the Table
    tk.Label(get_availableBook, text="Available Books", font=("Times", "14", "bold "),
             pady=10, bg="gray").pack()

    frame = tk.Frame(get_availableBook, bg="gray")
    frame.pack(pady=5)
    table = ttk.Treeview(frame)
    table['columns'] = ('ISBN', 'Title', 'Author',
                        'Available',  'Category')
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

    # looping through the available books and inserting it into the table
    for book in available_books:
        table.insert('', 'end', text='', values=book)
        style = ttk.Style()
        style.configure('Treeview.Heading', font=("Times", "12", "bold "))
        style.configure('Treeview', font=("Times", "10"), rowheight=25)

    table.pack(pady=20)
    get_availableBook.mainloop()
