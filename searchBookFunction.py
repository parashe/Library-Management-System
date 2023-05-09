from tkinter import *
from tkinter import messagebox
import sqlite3
import tkinter as tk
from tkinter import ttk


# This function is used by the librarian  and student and staff to search book by title, publication, category
# and author
# This function is called in studentstaffAction.py and LibrarianAction.py
# this function search book by title, publication, category and author
# this logic is same as  given by stish sarna in the class.

def search_book(opt, s):
    print("searching", opt, s)
    conn = sqlite3.connect('library.db')
    cursorObject = conn.cursor()

    try:
        with conn:
            s = '%'+s+'%'

            cmd = f'SELECT * FROM books WHERE {opt} LIKE :s'
            if opt in ['title', 'author', 'category', 'published_date']:
                # cursorObject.execute('SELECT * FROM books WHERE title LIKE :s', {'s':s})
                cursorObject.execute(cmd, {'s': s})
                # cursorObject.execute('SELECT * FROM books WHERE title =:s', {'s':s})
            else:
                cursorObject.execute(
                    'SELECT * FROM books WHERE author LIKE :s', {'s': s})
                # cursorObject.execute('SELECT * FROM books WHERE author =:s', {'s':s})
            return cursorObject.fetchall()
    except Exception as e:
        print("Failed to search book", e)
        messagebox.showerror("Error", "Failed to search book")


def search_book_ui():

    # create the main window and widgets
    searchroot = tk.Tk()

    # set the title, size, background color and disable the resizing property of the window
    searchroot.title("Library Management System ")
    searchroot.geometry("800x750")
    searchroot.config(bg="gray")

    # Create a frame to hold the widgets
    tk.Label(searchroot, text="Search Book", font=("Times", "14", "bold "),
             pady=10, bg="gray").pack()

    frame = tk.Frame(searchroot, bg="gray")
    frame.pack(pady=5)

    # create entery the search item
    s = tk.StringVar()
    opt = tk.StringVar(frame)
    opt.set('title')
    search_entry = tk.Entry(frame, textvariable=s, font=("Times", "12", "bold "),
                            width=25, highlightthickness=2, highlightcolor="red", )

    search_entry.pack(side=tk.LEFT, padx=5)

    # option menu for types of search
    search_option = tk.OptionMenu(
        frame, opt, 'title', 'author', 'category', 'published_date')
    search_option.config(
        font=('Times', 10),
        bg='gray',
        fg='black',
        highlightthickness=1,
    )
    search_option.pack()

    search_option.pack(side=tk.LEFT)
    search_button = tk.Button(
        frame, text='Search', command=lambda: search(opt, search_entry), bg="#33FF36", font=('Times', 10),)
    search_button.pack(side=tk.LEFT, padx=5)

    # create table
    table = ttk.Treeview(searchroot)
    table['columns'] = ('ISBN', 'Title', 'Author',
                        'Available', 'published_date', 'Category')
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
    table.pack(side=tk.BOTTOM, pady=200)

    def search(opt, s):

        # get searched data from search_books function
        results = search_book(opt.get(), s.get())
        print("results", results)

        # clear the treeview
        for i in table.get_children():
            table.delete(i)

        # display the results in the table
        for result in results:
            table.insert('', 'end', values=result)

    searchroot.mainloop()
