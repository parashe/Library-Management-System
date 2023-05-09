import tkinter as tk
import sqlite3
from tkinter import messagebox

# this function is used to update and delete table in the database
# this function is used by librarian
# This retrieve the data according to isbn from books and edit it and again save into books
# this system doesnt allow librarian to edit category and isbn of the book
# restriction is also implementted
# this function is called in LibDatabaseClass.py

# This function gets the data of books according to isbn from database
# and data is passed to update_book_ui function and updated


def get_isbn_to_update_book_ui():

    # create instance of a Tkinter
    return_book = tk.Tk()

    # set the title, size, background color and disable the resizing property of the window
    return_book.title("Library Management System ")
    return_book.geometry("500x250")
    return_book.config(bg="gray")

    # Create a frame to hold the widgets
    tk.Label(return_book, text="Get Book to Update", font=("Times", "14", "bold "),
             pady=10, bg="gray").pack()

    frame = tk.Frame(return_book, bg="gray")
    frame.pack(pady=5)

    # Create the widgets
    isbn_label = tk.Label(frame, text="Enter ISBN of the book to update",
                          font=("Times", "12", "bold "), bg="gray")

    isbn_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

    title_label = tk.Label(frame, text="Book Title",
                           font=("Times", "12", "bold "), bg="gray")
    title_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")

    isbn_entry = tk.Entry(frame, font=("Times", "12", "bold "),
                          width=25, highlightthickness=2, highlightcolor="red")

    isbn_entry.grid(row=0, column=1, padx=10, pady=10)

    title_entry = tk.Entry(
        frame, font=("Times", "12", "bold "), width=25, highlightthickness=2, highlightcolor="red")

    title_entry.grid(row=1, column=1, padx=10, pady=10)

    search_btn = tk.Button(frame, text="Search Book", bg="#18C809", font=("Times", "10", "bold "),
                           fg="black", padx=15, command=lambda: search_book_btn())
    search_btn.grid(row=5, column=0, columnspan=2, padx=5,
                    pady=5, )

    # this function is called when borrow button is clicked

    def search_book_btn():
        update_book_ui(isbn_entry.get(), title_entry.get())
        isbn_entry.delete(0, tk.END)
        title_entry.delete(0, tk.END)

    return_book.mainloop()

# this funcitons holds the logic to update data


def update_book(book):
    # Retrieve the updated book details from the input fields

    # Update the book details in the database
    conn = sqlite3.connect('library.db')
    cursorObject = conn.cursor()
    try:
        with conn:
            # update the book details by searching the book with isbn published_date
            cursorObject.execute("""UPDATE books 
                                    SET  title=:title, author=:author,published_date=:published_date, available=:available 
                                      WHERE isbn=:isbn""",
                                 {'title': book['title'], 'author': book['author'], 'published_date': book['published_date'], 'available': book['available'],
                                  'isbn': book['isbn']})

        messagebox.showinfo("Success", "Book updated successfully!")

    except Exception as e:
        print("Failed to update book", e)
        messagebox.showinfo("Error", "Failed to Update book")

    conn.commit()
    conn.close()


# this function is gui for updating data
def update_book_ui(isbn, title):
    # Retrieve the book details from the database
    conn = sqlite3.connect('library.db')
    cursorObject = conn.cursor()

    try:
        with conn:

            cursorObject.execute(
                "SELECT * FROM books WHERE isbn=? ", (isbn,))
            book = cursorObject.fetchone()

            # Create a new window with input fields to accept the updated book details
            # creating  new instance of a Tkinter
            update_window = tk.Tk()

            # set the title, size, background color and disable the resizing property of the window
            update_window.title("Library Management System ")
            update_window.geometry("600x400")
            update_window.config(bg="gray")

            # Create a frame to hold the widgets
            tk.Label(update_window, text="Update Book", font=("Times", "14", "bold "),
                     pady=10, bg="gray").pack()

            frame = tk.Frame(update_window, bg="gray")
            # Create a frame to hold the widgets
            frame = tk.Frame(update_window)
            frame.pack(pady=5)
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

            # category field is not editable
            category_entry = tk.Entry(frame, font=("Times", "12", "bold "),
                                      width=25, highlightthickness=2, highlightcolor="red")
            category_entry.grid(row=0, column=1, padx=10, pady=10)
            category_entry.insert(tk.END, book[5])
            category_entry.config(state="readonly")

            isbn_entry = tk.Entry(frame, font=("Times", "12", "bold "),
                                  width=25, highlightthickness=2, highlightcolor="red")
            isbn_entry.grid(row=1, column=1, padx=10, pady=10)
            isbn_entry.insert(tk.END, book[0])
            isbn_entry.config(state="readonly")

            title_entry = tk.Entry(frame, font=("Times", "12", "bold "),
                                   width=25, highlightthickness=2, highlightcolor="red")
            title_entry.grid(row=2, column=1, padx=10, pady=10)
            title_entry.insert(tk.END, book[1])

            author_entry = tk.Entry(frame, font=("Times", "12", "bold "),
                                    width=25, highlightthickness=2, highlightcolor="red")
            author_entry.grid(row=3, column=1, padx=10, pady=10)
            author_entry.insert(tk.END, book[2])

            available_entry = tk.Entry(frame, font=("Times", "12", "bold "),
                                       width=25, highlightthickness=2, highlightcolor="red")
            available_entry.grid(row=4, column=1, padx=10, pady=10)
            available_entry.insert(tk.END, book[3])

            published_date_entry = tk.Entry(frame, font=("Times", "12", "bold "),
                                            width=25, highlightthickness=2, highlightcolor="red")
            published_date_entry.grid(row=5, column=1, padx=10, pady=10)
            published_date_entry.insert(tk.END, book[4])

            # when this button is clicked  it will call the borrow_btn function
            save_btn = tk.Button(frame, text="Update Books", bg="#18C809",
                                 fg="white", padx=15, command=lambda: updatebtn()
                                 )
            save_btn.grid(row=6, column=0, columnspan=2, padx=5,
                          pady=5, )

        # this function is called when borrow button is clicked and passed the book details to
        #  the update_book function

            def updatebtn():
                updatedbook = {
                    'isbn': isbn_entry.get(),
                    'title': title_entry.get(),
                    'author': author_entry.get(),
                    'available': available_entry.get(),
                    'published_date': published_date_entry.get(),
                    'category': book[5]
                }
                update_book(updatedbook)

                isbn_entry.delete(0, tk.END)
                title_entry.delete(0, tk.END)
                author_entry.delete(0, tk.END)
                available_entry.delete(0, tk.END)
                published_date_entry.delete(0, tk.END)

    except Exception as e:
        print("Failed to get  book", e)
        messagebox.showinfo("Error", "Failed to get  book")

    conn.commit()
    cursorObject.close()

# This function for delete GUI used for deleting book


def get_isbn_to_delete_book_ui():

    return_book = tk.Tk()

    # set the title, size, background color and disable the resizing property of the window
    return_book.title("Library Management System ")
    return_book.geometry("500x250")
    return_book.config(bg="gray")

    # Create a frame to hold the widgets
    tk.Label(return_book, text="Enter Book to Delete", font=("Times", "14", "bold "),
             pady=10, bg="gray").pack()

    frame = tk.Frame(return_book, bg="gray")
    frame.pack(pady=5)

    # Create the widgets
    isbn_label = tk.Label(frame, text="Enter isbn of the book Delete",
                          font=("Times", "12", "bold "), bg="gray")

    isbn_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

    title_label = tk.Label(frame, text="Book Title",
                           font=("Times", "12", "bold "), bg="gray")
    title_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")

    isbn_entry = tk.Entry(frame, font=("Times", "12", "bold "),
                          width=25, highlightthickness=2, highlightcolor="red")

    isbn_entry.grid(row=0, column=1, padx=10, pady=10)

    title_entry = tk.Entry(
        frame, font=("Times", "12", "bold "), width=25, highlightthickness=2, highlightcolor="red")

    title_entry.grid(row=1, column=1, padx=10, pady=10)

    search_delete_btn = tk.Button(frame, text="Delete", bg="#18C809", font=("Times", "10", "bold "),
                                  fg="black", padx=15, command=lambda: search_deletebook_btn())
    search_delete_btn.grid(row=5, column=0, columnspan=2, padx=5,
                           pady=5, )

    # this function is called when borrow button is clicked

    def search_deletebook_btn():

        delete_book(isbn_entry.get(), title_entry.get())
        isbn_entry.delete(0, tk.END)
        title_entry.delete(0, tk.END)
    return_book.mainloop()


# When function gets the isbn number and gets book for isbn number and delete it
def delete_book(isbn, title):
    # Delete the book from the database
    conn = sqlite3.connect('library.db')
    cursorObject = conn.cursor()
    try:
        with conn:
            if isbn == "" or title == "":
                messagebox.showinfo("Error", "Please enter isbn")
            else:
                # delete the book details by searching the book with isbn published_date
                cursorObject.execute(
                    """DELETE FROM books WHERE isbn=:isbn""", {'isbn': isbn})

                messagebox.showinfo("Success", "Book deleted successfully!")

    except Exception as e:
        print("Failed to delete book", e)
        messagebox.showinfo("Error", "Book not Found")

    conn.commit()
    conn.close()
