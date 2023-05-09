import sqlite3
import tkinter as tk
import tkinter.messagebox as messagebox

# This class is used to get the account details of the user
# the details is retrieved from the database and displayed in the account report


class Account:
    def __init__(self, UserID):
        self.UserID = UserID

    def get_account(self):

        conn = sqlite3.connect('library.db')
        c = conn.cursor()

        try:
            with conn:

                c.execute("SELECT * FROM Account WHERE UserID = ?",
                          (self.UserID,))
                accountdetails = c.fetchall()

                # account details is passed to getu_account_ui function
                Account.get_account_ui(accountdetails
                                       )
        except Exception as e:
            print("Failed to get account", e)

            messagebox.showinfo("Error", "Failed to get account")

    # Account report  user interface

    def get_account_ui(accountdetails):

        print('accountdetails', accountdetails)

        account_window = tk.Tk()
        account_window.title("Library Management System ")
        account_window.config(bg="gray")
        account_window.geometry('400x300')
        tk.Label(account_window, text="Account Report", font=("Times", "15", "bold "),
                 pady=10, bg="gray").pack()

        # fetching the data from the Account table and displaying it in the account report
        # accountdetails[i][j] where i is the row and j is the column

        tk.Label(account_window, text=f"UserID: {accountdetails[0][6]}", bg="gray").pack(
            pady=0)
        tk.Label(account_window, text=f"No. of books borrowed: {accountdetails[0][1]}", bg="gray"
                 ).pack(
            pady=5)
        tk.Label(account_window, text=f"No. of  books reserved: {accountdetails[0][2]}", bg="gray").pack(
            pady=5)
        tk.Label(account_window, text=f"No. of  books returned: {accountdetails[0][3]}", bg="gray").pack(
            pady=5)
        tk.Label(account_window,
                 text=f"Fine Paid: £{accountdetails[0][5]}").pack(pady=5)

        account_window.mainloop()
