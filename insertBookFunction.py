import sqlite3
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import json

# This module insert book by selecting category into the database table
# This module is used by librarian to insert book into the database
# this module is called in LibDatabaseClass.py

# This function verify many stage in the book insertion process
# check if the fields are empty
# check if the book already exists


def insert_book(books):
    # connecting to database
    conn = sqlite3.connect('library.db')
    cursorObject = conn.cursor()

    try:

        with conn:

            # check if the fields are empty
            if books['isbn'] == '' or books['title'] == "" or books['author'] == " " or books['available'] == "" or books['published_date'] == "" or books['category'] == " ":

                messagebox.showerror("Error", "Please fill all the fields")

            # check if the book already exists
            elif cursorObject.execute("SELECT * FROM books WHERE isbn = :isbn", {'isbn': books['isbn']}):
                result = cursorObject.fetchone()
                if result:
                    messagebox.showerror(
                        "Error", "Book with the given ISBN already exists")
                else:
                    # with open('books.json') as f:
                    #     book_data = json.load(f)

                    # for books in book_data:
                    # inserting into books database
                    cursorObject.execute("INSERT INTO books VALUES(:isbn,:title,:author,:available,:published_date,:category)",
                                         {
                                             'isbn': books['isbn'], 'title': books['title'], 'author': books['author'],
                                             'available': books['available'], 'published_date': books['published_date'],
                                             'category': books['category']})

                    messagebox.showinfo("Book has been created Successfully",
                                        "You have successfully Added Books!")

    except Exception as e:

        messagebox.showerror(
            "Error", e)


def insert_book_ui():

    # extracting the categories to get the category name
    # connecting to database
    conn = sqlite3.connect('library.db')
    cursorObject = conn.cursor()

    try:
        with conn:
            cursorObject.execute("SELECT * FROM category")
            categories = cursorObject.fetchall()
            print('category', categories)
    except Exception as e:
        print("Failed to get  category", e)

        messagebox.showinfo("Error", "Failed to get  category")

    # creating  new instance of a Tkinter
    add_books = tk.Tk()

    # set the title, size, background color and disable the resizing property of the window
    add_books.title("Library Management System ")
    add_books.geometry("400x400")
    add_books.config(bg="gray")

    # Create a frame to hold the widgets
    tk.Label(add_books, text="Add Book", font=("Times", "14", "bold "),
             pady=10, bg="gray").pack()

    frame = tk.Frame(add_books, bg="gray")

    # Create a frame to hold the widgets
    frame = tk.Frame(add_books)
    frame.pack(pady=5)

    # Create the widgets
    category = tk.Label(frame, text="Category",
                        font=("Times", "12", "bold "))
    category.grid(row=0, column=0, padx=10, pady=10, sticky="w")

    isbn = tk.Label(frame, text="ISBN",
                    font=("Times", "12", "bold "))
    isbn.grid(row=1, column=0, padx=10, pady=10, sticky="w")

    title = tk.Label(frame, text="Title",
                     font=("Times", "12", "bold "))
    title.grid(row=2, column=0, padx=10, pady=10, sticky="w")

    author = tk.Label(frame, text="Author", font=("Times", "12", "bold "),
                      )
    author.grid(row=3, column=0, padx=10, pady=10, sticky="w")

    available = tk.Label(frame, text="Available",
                         font=("Times", "12", "bold "))
    available.grid(row=4, column=0, padx=10, pady=10, sticky="w")

    published_date = tk.Label(frame, text="Published Date",
                              font=("Times", "12", "bold "))
    published_date.grid(row=5, column=0, padx=10, pady=10, sticky="w")

    # creating entry fields
    category_values = [category[1] for category in categories]
    category = tk.StringVar()
    category = ttk.Combobox(frame, textvariable=category,
                            font=("Times", "12", "bold "), width=23, state="readonly")
    category["values"] = (category_values)
    category.current(0)
    category.grid(row=0, column=1, padx=10, pady=10)

    # input box
    isbn_entry = tk.Entry(frame, font=("Times", "12", "bold "),
                          width=25, highlightthickness=2, highlightcolor="red")
    isbn_entry.grid(row=1, column=1, padx=10, pady=10)

    title_entry = tk.Entry(frame, font=("Times", "12", "bold "),
                           width=25, highlightthickness=2, highlightcolor="red")
    title_entry.grid(row=2, column=1, padx=10, pady=10)

    author_entry = tk.Entry(frame, font=("Times", "12", "bold "),
                            width=25, highlightthickness=2, highlightcolor="red")
    author_entry.grid(row=3, column=1, padx=10, pady=10)

    available_entry = tk.Entry(frame, font=("Times", "12", "bold "),
                               width=25, highlightthickness=2, highlightcolor="red")
    available_entry.grid(row=4, column=1, padx=10, pady=10)

    published_date_entry = tk.Entry(frame, font=("Times", "12", "bold "),
                                    width=25, highlightthickness=2, highlightcolor="red")
    published_date_entry.grid(row=5, column=1, padx=10, pady=10)

    save_btn = tk.Button(frame, text="Add Books", bg="#18C809",
                         fg="white", padx=15, command=lambda: save_book()
                         )
    save_btn.grid(row=6, column=0, columnspan=2, padx=5,
                  pady=5, )
# this functions provide data to the insert_book function

    def save_book():

        data = {
            'isbn': isbn_entry.get(),
            'title': title_entry.get(),
            'author': author_entry.get(),
            'available': available_entry.get(),
            'published_date': published_date_entry.get(),
            'category': category.get()

        }
        insert_book(data)
        isbn_entry.delete(0, tk.END)
        title_entry.delete(0, tk.END)
        author_entry.delete(0, tk.END)
        available_entry.delete(0, tk.END)
        published_date_entry.delete(0, tk.END)
        category.delete(0, tk.END)

    add_books.mainloop()
