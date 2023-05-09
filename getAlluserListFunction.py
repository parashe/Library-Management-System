from tkinter import *
from tkinter import messagebox
import sqlite3
import tkinter as tk
from tkinter import ttk


# This function is used by the librarian to get all thuserlist
# This function simply select all user from Users table and display in the GUI using table
# using get_all_users_ui function

def get_all_user():

    # connecting to database.
    conn = sqlite3.connect('library.db')
    cursorObject = conn.cursor()
    try:
        with conn:
            # get all the users from the database
            cursorObject.execute("SELECT * FROM Users")
            users = cursorObject.fetchall()

            # passing the users to get_all_users_ui function
            get_all_users_ui(users)

    except Exception as e:
        print("Failed to get  Users", e)

        messagebox.showinfo("Error", "Failed to get  Users")


def get_all_users_ui(users):

    # creating  new instance of a Tkinter
    get_allUsers = tk.Tk()

    get_allUsers.title("Library Management System ")
    get_allUsers.geometry("600x400")
    get_allUsers.config(bg="gray")

    # Create a frame to hold the widgets
    # fetching the data from the Users table and displaying it in the Table
    tk.Label(get_allUsers, text="All User List", font=("Times", "14", "bold "),
             pady=10, bg="gray").pack()

    frame = tk.Frame(get_allUsers, bg="gray")
    frame.pack(pady=5)
    table = ttk.Treeview(frame)
    table['columns'] = ('UserID', 'Name', 'UsetType', 'DeptOrClass',
                        )
    table.column('#0', minwidth=0, width=0, stretch=NO)
    table.heading('UserID', text='UserID')
    table.column('UserID', width=50, anchor='w')
    table.heading('Name', text='Name')
    table.column('Name', width=100)
    table.heading('UsetType', text='UsetType')
    table.column('UsetType', width=100)
    table.heading('DeptOrClass', text='DeptOrClass')
    table.column('DeptOrClass', width=100)

    # looping through the users and inserting it into the table
    for users in users:
        table.insert('', 'end', text='', values=(
            users[0], users[1], users[3], users[4]))
        style = ttk.Style()
        style.configure('Treeview.Heading', font=("Times", "12", "bold "))
        style.configure('Treeview', font=("Times", "10"), rowheight=25)

    table.pack(pady=20)
    get_allUsers.mainloop()
