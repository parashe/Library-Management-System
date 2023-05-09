from tkinter import *
from tkinter import messagebox
import sqlite3
import tkinter as tk
from tkinter import ttk

# this function includes the every logic and Gui to getAll account details of the user
# This function is used by the librarian to get all the account details of the user


def get_all_account_details():

    # connecting to database.
    conn = sqlite3.connect('library.db')
    cursorObject = conn.cursor()

    try:
        with conn:
            cursorObject.execute("SELECT * FROM Account")
            all_accountdetails = cursorObject.fetchall()

            # account details is passed to get_all_account_ui function
            get_all_account_ui(all_accountdetails,
                               )
    except Exception as e:
        print("Failed to get account", e)

        messagebox.showinfo("Error", "Failed to get account")


def get_all_account_ui(all_accountdetails):

    # creating  new instance of a Tkinter
    get_allAcountDetails = tk.Tk()

    get_allAcountDetails.title("Library Management System ")
    get_allAcountDetails.geometry("600x400")
    get_allAcountDetails.config(bg="gray")

    # Create a frame to hold the widgets
    # fetching the data from the Account table and displaying it in the Table
    tk.Label(get_allAcountDetails, text="All Borrowed Books", font=("Times", "14", "bold "),
             pady=10, bg="gray").pack()

    frame = tk.Frame(get_allAcountDetails, bg="gray")
    frame.pack(pady=5)
    table = ttk.Treeview(frame)
    table['columns'] = ('no_borrowed_books', 'no_reserved_books', 'no_returned_books',
                        'fine_amount', 'UserID')

    table.column('#0', minwidth=0, width=0, stretch=NO)
    table.heading('no_borrowed_books', text='no_borrowed_books')
    table.column('no_borrowed_books', width=50)
    table.heading('no_reserved_books', text='no_reserved_books')
    table.column('no_reserved_books', width=75)
    table.heading('no_returned_books', text='no_returned_books')
    table.column('no_returned_books', width=75)
    table.heading('fine_amount', text='fine_Paid')
    table.column('fine_amount', width=100)
    table.heading('UserID', text='UserID')
    table.column('UserID', width=100)

    # looping through the account details  and inserting it into the table
    for accountDetails in all_accountdetails:
        table.insert('', 'end', text='', value=(
            accountDetails[1],  accountDetails[2], accountDetails[3], accountDetails[5], accountDetails[6]))
        style = ttk.Style()
        style.configure('Treeview.Heading', font=("Times", "12", "bold "))
        style.configure('Treeview', font=("Times", "10"), rowheight=25)

    table.pack(pady=20)
    get_allAcountDetails.mainloop()
