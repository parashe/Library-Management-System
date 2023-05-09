from tkinter import *
from tkinter import messagebox
import sqlite3
from datetime import date, timedelta
import random
import tkinter as tk


# this function includes the every logic and Gui to borrow book when book book is clicked in
# the main window

def borrow_book_function(isbn, title, UserID):
    # connecting to database.
    conn = sqlite3.connect('library.db')
    cursorObject = conn.cursor()
    try:
        with conn:
            # checks for the empty fields.
            if isbn == "" or title == "":
                messagebox.showinfo("Error", "Please enter all fields")

            else:
                # checks if the book with isbn  is available in the database.
                cur = cursorObject.execute(
                    "select * from books where isbn = ?", (isbn,))

                # if the book is not available then it will show error.
                if cur.fetchone() == None:

                    messagebox.showinfo(
                        "Error", "Books not found please check the book id or title")
                else:
                    # check if the user has already borrowed the maximum number of books (5)
                    cur = cursorObject.execute(
                        'SELECT COUNT(*) FROM borrowed_books WHERE UserID = ?', (UserID,))
                    number_of_borrowed_books = cur.fetchone()[0]

                    print('number_of_borrowed_books1',
                          number_of_borrowed_books)

                    # check the number of book borrowed by the user if it is greater than 5 then it will show error
                    if number_of_borrowed_books > 5:
                        messagebox.showinfo(
                            "Error", "You have already borrowed the maximum number of books (5).")

                    else:

                        # check if the book is available for borrowing
                        # (i.e., not already borrowed by someone else)

                        available_book = cursorObject.execute(
                            'select available from books where isbn = ?', (isbn,))

                        # get the number of available books
                        available = available_book.fetchone()[0]

                        print('available', available)
                        # checks for availbility of the book
                        if available <= 0:

                            messagebox.showinfo(
                                "Error", "Sorry, the book is already borrowed by someone else.")

                        else:
                            # calculate the due date (7 days from today)
                            due_date = date.today() + timedelta(days=7)
                            number_of_count = cursorObject.execute(
                                'SELECT Count(borrow_id) FROM borrowed_books')

                            max_id = number_of_count.fetchone()[0]
                            # generates the random borrow id
                            borrow_id = max_id + random.randint(1, 1000)
                            print('borrow_id:', borrow_id)

                            # checking if same book is borrowed  by the same user or not
                            cur = cursorObject.execute(
                                'SELECT * FROM borrowed_books WHERE UserID = ? AND isbn = ?', (UserID, isbn))
                            result = cur.fetchone()
                            if result:
                                messagebox.showerror(
                                    "Error", "You have already borrowed this book")

                            else:
                                # insert a new record into the borrowed_books table
                                cursorObject.execute(
                                    'INSERT INTO borrowed_books VALUES(:borrow_id,:UserID,:isbn,:borrow_date,:returned,:status,:due_date)', {
                                        'borrow_id': borrow_id, 'UserID': UserID, 'isbn': isbn, 'borrow_date': date.today(),  'returned': 0, 'status': 'borrowed', 'due_date': due_date, })

                            # check if the user has an account

                                cursorObject.execute(
                                    'select no_borrowed_books from Account where UserID = ?', (UserID,))

                            # if user donot borrowed books then insert the record into the account table
                                if cursorObject.fetchone() is None:

                                    cursorObject.execute(
                                        'INSERT INTO Account VALUES(:account_id,:no_borrowed_books,:no_reserved_books,:no_returned_books,:no_lost_books,:fine_amount,:UserID)',
                                        {'account_id': borrow_id, 'no_borrowed_books': 1, 'no_reserved_books': 0, 'no_returned_books': 0, 'no_lost_books': 0, 'fine_amount': 0, 'UserID': UserID, })

                                # if user already borrowed books then update the record into the account table
                                else:
                                    cursorObject.execute("""UPDATE Account SET no_borrowed_books=no_borrowed_books+1
                                                        WHERE UserID=:UserID""",
                                                         {'UserID': UserID})

                                # update the available books in the books table
                                cursorObject.execute("""UPDATE books SET available=available-1
                                            WHERE isbn=:isbn""",
                                                     {'isbn': isbn})

                                messagebox.showinfo(
                                    "Success", "Book borrowed successfully. Please return the book by " + due_date.strftime('%Y-%m-%d'))
    except Exception as e:
        print("Failed to insert data into sqlite table", e)
        messagebox.showinfo("Error", "Failed to borrow the book")

        # commit the changes and close the cection
    conn.commit()
    cursorObject.close()


def borrow_book_window(UserID):
    # creating  new instance of a Tkinter
    borrow_book = tk.Tk()

    # set the title, size, background color and disable the resizing property of the window
    borrow_book.title("Library Management System ")
    borrow_book.geometry("400x250")
    borrow_book.config(bg="gray")

    # Create a frame to hold the widgets
    tk.Label(borrow_book, text="Borrow Book", font=("Times", "14", "bold "),
             pady=10, bg="gray").pack()

    frame = tk.Frame(borrow_book, bg="gray")

    # This adds the frame to the application window with a padding of 5 pixels vertically.
    frame.pack(pady=5)

    bookid_label = tk.Label(frame, text="Book ID",
                            font=("Times", "12", "bold "), bg="gray")

    bookid_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

    title_label = tk.Label(frame, text="Book Title",
                           font=("Times", "12", "bold "), bg="gray")
    title_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")

    bookid_entry = tk.Entry(frame, font=("Times", "12", "bold "),
                            width=25, highlightthickness=2, highlightcolor="red")

    bookid_entry.grid(row=0, column=1, padx=10, pady=10)

    title_entry = tk.Entry(
        frame, font=("Times", "12", "bold "), width=25, highlightthickness=2, highlightcolor="red")

    title_entry.grid(row=1, column=1, padx=10, pady=10)

# when this button is clicked  it will call the borrow_btn function
    borrow_btn = tk.Button(frame, text="Borrow Book", bg="#18C809", font=("Times", "10", "bold "),
                           fg="black", padx=15, command=lambda: borrow_btn())
    borrow_btn.grid(row=5, column=0, columnspan=2, padx=5,
                    pady=5, )

# this function is called when borrow button is clicked
    def borrow_btn():
        borrow_book_function(bookid_entry.get(),
                             title_entry.get(), UserID)
        bookid_entry.delete(0, tk.END)
        title_entry.delete(0, tk.END)

    # this allow receive and handle events it must be called last in order for the window to work properly
    borrow_book.mainloop()
