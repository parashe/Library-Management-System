from tkinter import *
from tkinter import messagebox
import sqlite3
from datetime import date, timedelta, datetime
import tkinter as tk


# this function is called when renew button is clicked
# this function is used by student staff
# this function is used to renew the book
# this function is called in studentstaffAction.py


def renew_book_function(isbn, title, UserID):

    # Assuming book ID is 1234
    if isbn == "" or title == "":
        messagebox.showinfo("Error", "Please enter all fields")
    else:

        conn = sqlite3.connect('library.db')
        cursorObject = conn.cursor()

        try:
            with conn:

                cursor = cursorObject.execute(
                    "SELECT due_date FROM borrowed_books WHERE isbn = ? AND UserID= ?", (isbn, UserID))
                result = cursor.fetchone()
                due_date = result[0]
                print('due_date', due_date)

                # convert the due date to date format
                due_dates = datetime.strptime(
                    due_date, "%Y-%m-%d").date()
                print('due_dates', due_dates)

                # # Calculate the number of days between the current date and the due date
                now = date.today()
                print('now', now)
                days_overdue = (now - due_dates).days
                print('days_overdue', days_overdue)

                # Check if the book can be renewed
                if days_overdue > 7:
                    print(
                        "Sorry, this book cannot be renewed as it is already overdue by more than 7 days.")
                else:
                    # Calculate the new due date (14 days from today)
                    new_due_date = now + timedelta(days=14)

                    # Update the due date and the number of renewals in the database
                    cursorObject.execute("UPDATE borrowed_books SET due_date = ? WHERE isbn = ? AND UserID= ?",
                                         (new_due_date, isbn, UserID))
                    messagebox.showinfo(
                        "Success", "Book renewed successfully. New due date:" + new_due_date.strftime('%Y-%m-%d'))

        except Exception as e:

            print("Failed to renew book", e)
            messagebox.showinfo("Error", "Failed to Renew book")

    # Close the database connection
    conn.commit()
    cursorObject.close()

# creating Gui for renew book


def renew_book_window(UserID):
 # creating  new instance of a Tkinter
    renew_book = tk.Tk()

    # set the title, size, background color and disable the resizing property of the window
    renew_book.title("Library Management System ")
    renew_book.geometry("400x250")
    renew_book.config(bg="gray")

    # Create a frame to hold the widgets
    tk.Label(renew_book, text="Renew Book", font=("Times", "14", "bold "),
             pady=10, bg="gray").pack()

    frame = tk.Frame(renew_book, bg="gray")
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

    # button to renew book
    renew_btn = tk.Button(frame, text="Renew Book", bg="#18C809", font=("Times", "10", "bold "),
                          fg="black", padx=15, command=lambda: renew_btn())
    renew_btn.grid(row=5, column=0, columnspan=2, padx=5,
                   pady=5, )
# this function is called when borrow button is clicked

    def renew_btn():
        renew_book_function(bookid_entry.get(), title_entry.get(), UserID)
        bookid_entry.delete(0, tk.END)
        title_entry.delete(0, tk.END)

 # this allow receive and handle events it must be called last in order for the window to work properly
    renew_book.mainloop()
