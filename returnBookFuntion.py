from tkinter import *
from tkinter import messagebox
import sqlite3
import tkinter as tk
from datetime import date, datetime

# this function returns the book
# this function return book by student staff
# this function is called in studentstaffAction.py
# This function checks if the book is borrowed or not by the user Id in the borrowed books table
# if its borrowed then it will calculate the fine and update the fine in the account table
# and update the book's availability and the user's number of borrowed books


def return_book_function(isbn, UserID, title):

    # Connect to the database
    conn = sqlite3.connect('library.db')
    cursorObject = conn.cursor()

    try:
        with conn:
            if isbn == "" or title == "":
                messagebox.showinfo("Error", "Please enter all fields")
            else:
                # check if the book is borrowed or not
                cur = cursorObject.execute(
                    "select * from borrowed_books where isbn = ?", (isbn,))
                if cur.fetchone() == None:
                    print('no books')
                    messagebox.showinfo(
                        "Error", "Books not found please check the book id or title")
                else:

                    # Check if the book is already returned
                    # check the book status in the borrowed_books table and checking returned column
                    cursor1 = cursorObject.execute(
                        "SELECT status FROM borrowed_books WHERE UserID=? AND isbn=?", (UserID, isbn))
                    status = cursor1.fetchone()

                    # Check if the book is  reserved status in the ReservedBook table
                    # If the book is not return then return the book
                    # calculate fine and update fine in Account table
                    # and update the book's availability and the user's number of borrowed books
                    # and delete the record from the borrowed_books table
                    #
                    print('status', status[0])
                    # check for the status of the book

                    if status[0] == 'borrowed':

                        # Calculate the fine for the returned book
                        # select due_date from borrowed_books table
                        cursor = cursorObject.execute(
                            "SELECT due_date FROM borrowed_books WHERE UserID=? AND isbn=?", (UserID, isbn))
                        due_date = cursor.fetchone()[0]

                        print('due_date', due_date)
                        due_dates = datetime.strptime(
                            due_date, "%Y-%m-%d").date()
                        print('due_date', due_date)

                        # Calculate the number of days between the current date and the due date
                        now = date.today()
                        print('now', now)
                        days_late = (now - due_dates).days
                        print('days_late', days_late)
                        if days_late <= 0:
                            messagebox.showinfo(
                                "Fine", "You have no fine, Click OK to return book")
                            messagebox.showinfo(
                                "Success", "Book returned successfully.")

                        else:

                            fine_per_day = 1.0  # Assuming £1 per day

                            fine_amount = fine_per_day * days_late  # calculate the fine

                            if fine_amount > 0:
                                # update the fine in the Account table
                                # call the pay_fine_window function to display the fine to the user
                                # for the payment
                                pay_fine_window(fine_amount)
                                cursorObject.execute(
                                    """update Account set fine_amount = ? where UserID = ?""", (fine_amount, UserID))

                                # Display the fine to the user
                                messagebox.showinfo(
                                    "Fine", f"Your book is {days_late} days late. Your fine is £{fine_amount:.2f}.")

                                messagebox.showinfo(
                                    "Success", "Book returned successfully.")
                        # delete the records from borrowed books
                        cursorObject.execute(
                            'DELETE FROM borrowed_books WHERE isbn = ? ', (isbn,))

                        # Update the book's availability
                        cursorObject.execute("UPDATE Account SET no_borrowed_books=no_borrowed_books-1,no_returned_books=no_returned_books+1 WHERE UserID=?",
                                             (UserID,))
                        cursorObject.execute(
                            "UPDATE books SET available=available+1 WHERE isbn=?", (isbn,))

                        # Commit the changes and close the database connection

                    else:
                        # Display an error message if the book is already returned or not reserved
                        messagebox.showinfo(
                            "Error", "This book has not been borrowed by the user.")

    except Exception as e:

        print("Failed to return book", e)
        messagebox.showinfo("Error", "Failed to return book")

    # Commit the changes and close the database connection
    conn.commit

# Return book window for GUI


def return_book_window(UserID):

    # creating  new instance of a Tkinter
    return_book = tk.Tk()

    # set the title, size, background color and disable the resizing property of the window
    return_book.title("Library Management System ")
    return_book.geometry("400x250")
    return_book.config(bg="gray")

    # Create a frame to hold the widgets
    tk.Label(return_book, text="Return Book", font=("Times", "14", "bold "),
             pady=10, bg="gray").pack()

    frame = tk.Frame(return_book, bg="gray")
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

    return_btn = tk.Button(frame, text="Return Book", bg="#18C809", font=("Times", "10", "bold "),
                           fg="black", padx=15, command=lambda: return_btns())
    return_btn.grid(row=5, column=0, columnspan=2, padx=5,
                    pady=5, )
# this function is called when borrow button is clicked

    def return_btns():
        return_book_function(bookid_entry.get(), UserID, title_entry.get())
        bookid_entry.delete(0, tk.END)
        title_entry.delete(0, tk.END)

    return_book.mainloop()


# payment window when fine is due
def pay_fine_window(fine):

    # creating  new instance of a Tkinter
    payment = tk.Tk()

    # set the title, size, background color and disable the resizing property of the window
    payment.title("Library Management System ")
    payment.geometry("400x250")
    payment.config(bg="gray")

    # Create a frame to hold the widgets
    tk.Label(payment, text="Pay Fine", font=("Times", "14", "bold "),
             pady=10, bg="gray").pack()

    frame = tk.Frame(payment, bg="gray")
    frame.pack(pady=5)

    # Create the widgets

    amount_label = tk.Label(frame, text="Payment Amount",
                            font=("Times", "12", "bold "), bg="gray")
    amount_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")

    amount_entry = tk.Entry(
        frame, font=("Times", "12", "bold "), width=25, highlightthickness=2, highlightcolor="red")

    amount_entry.grid(row=1, column=1, padx=10, pady=10)
    amount_entry.insert(tk.END, fine)
    amount_entry.config(state="readonly")

    pay_btn = tk.Button(frame, text="Pay ", bg="#18C809", font=("Times", "10", "bold "),
                        fg="black", padx=15, command=lambda: pay_btns())
    pay_btn.grid(row=5, column=0, columnspan=2, padx=5,
                 pady=5, )
# this function is called when borrow button is clicked

    def pay_btns():
        messagebox.showinfo('Success', 'Fine paid successfully.')

    payment.mainloop()
