from tkinter import *
from tkinter import messagebox
import sqlite3
from datetime import date, timedelta
import random
import tkinter as tk


# This function is used to reserved book by student staff
# this function is called in studentstaffAction.py
# this function verify if the book is available or not if the book is not availale then only it can be reserved
# if available then directly borrow the book

def reserve_book_function(isbn, title, UserID):
    conn = sqlite3.connect('library.db')
    cursorObject = conn.cursor()
    try:
        with conn:
            if isbn == "" or title == "":
                messagebox.showinfo("Error", "Please enter all fields")

            else:
                # checks if the book with isbn  is available in the database.
                cur = cursorObject.execute(
                    "select * from books where isbn = ?", (isbn,))

                if cur.fetchone() == None:
                    print('no books')
                    messagebox.showinfo(
                        "Error", "Books not found please chek the book id or title")
                else:

                    available_book = cursorObject.execute(
                        'select available from books where isbn = ?', (isbn,))

                    # get the number of available books
                    available = available_book.fetchone()[0]

                    print('available', available)
                    # checks for availbility of the book
                    if available > 0:

                        messagebox.showinfo(
                            "Message", "Yeah ! you can directly borrow books.")

                    else:

                        # system doestnot allow more than two books to reserve
                        # check if the user has already borrowed or reserved the maximum number of books (2)
                        cur = cursorObject.execute(
                            'SELECT COUNT(no_reserved_books) FROM Account WHERE UserID = ?', (UserID,))

                        num_of_reserved_book = cur.fetchone()[0]
                        print('num_borrowed1', num_of_reserved_book)

                        # individual can only reserve two books
                        # check if the user has already borrowed or reserved the maximum number of books (2)
                        if num_of_reserved_book > 2:
                            messagebox.showinfo(
                                "Error", "You have already reserved the maximum number of books (2).")

                        else:

                            # this is to give a unique borrow_id to each borrow transaction

                            cur3 = cursorObject.execute(
                                'SELECT Count(reserved_book_id) FROM ReservedBook')
                            max_id = cur3.fetchone()[0]
                            print('max_id', max_id)
                            reserve_id = max_id + random.randint(1, 1000)
                            print('reserve_id:', reserve_id)

                            # insert a new record into the reserved_books table

                            cursorObject.execute("""insert into ReservedBook Values(:reserved_book_id ,:isbn,:reserved_date,:reserved_status,:UserID,)""",
                                                 {'reserved_book_id': reserve_id, 'isbn': isbn, 'reserved_date': date.today(), 'reserved_status': 'reserved', 'UserID': UserID, })

                            # check if the user has already reserved books or not

                            cursorObject.execute(
                                'select * from Account where UserID = ?', (UserID,))
                            num_reserved_acc = cursorObject.fetchone()

                            if num_reserved_acc == None:

                                # IF USERid doestnot have reserved book then it insert data
                                cursorObject.execute(
                                    'INSERT INTO Account VALUES(:account_id,:no_borrowed_books,:no_reserved_books,:no_returned_books,:no_lost_books,:fine_amount,:UserID)',
                                    {'account_id': reserve_id, 'no_borrowed_books': 0, 'no_reserved_books': 1, 'no_returned_books': 0, 'no_lost_books': 0, 'fine_amount': 0, 'UserID': UserID, })
                                messagebox.showinfo(
                                    "Success", f"Book {title} reserved successfully.  ")
                            else:

                                # else it update data if it already exist
                                cursorObject.execute("""UPDATE Account SET no_reserved_books=no_reserved_books+1
                                    WHERE UserID=:UserID""",
                                                     {'UserID': UserID})

                                messagebox.showinfo(
                                    "Success", f"Book {title} reserved successfully.  ")
    except Exception as e:

        print("Failed to reserve book", e)
        messagebox.showinfo("Error", "Failed to reserve book")

        # commit the changes and close the cection
        conn.commit()
        cursorObject.close()


def reserve_book_window(UserID):
   # creating  new instance of a Tkinter
    reserve_book = tk.Tk()

    # set the title, size, background color and disable the resizing property of the window
    reserve_book.title("Library Management System ")
    reserve_book.geometry("400x250")
    reserve_book.config(bg="gray")

    # Create a frame to hold the widgets
    tk.Label(reserve_book, text="Reserve Book", font=("Times", "14", "bold "),
             pady=10, bg="gray").pack()

    frame = tk.Frame(reserve_book, bg="gray")
    # This adds the frame to the application window with a padding of 5 pixels vertically.
    frame.pack(pady=5)
    # Create the widgets

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
    reserve_btn = tk.Button(frame, text="Reserve Book", bg="#18C809", font=("Times", "10", "bold "),
                            fg="black", padx=15, command=lambda: reserve_btn())
    reserve_btn.grid(row=5, column=0, columnspan=2, padx=5,
                     pady=5, )

# this function is called when borrow button is clicked
    def reserve_btn():
        reserve_book_function(bookid_entry.get(),
                              title_entry.get(), UserID)
        bookid_entry.delete(0, tk.END)
        title_entry.delete(0, tk.END)

    # this allow receive and handle events it must be called last in order for the window to work properly
    reserve_book.mainloop()
