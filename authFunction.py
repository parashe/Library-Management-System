import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3
from UserClass import Student
from UserClass import Staff
from UserClass import Librarian


# The module login.py is used to create login  and register window a and when user is logged in
# it provides menu according to the user type
# when user is  logged in the program moves to  UserClass.py


# this method authenticates the user
# Login Gui window
def login_window():

    # creating  new instance of a Tkinter
    login_root = tk.Tk()
    login_root.title("Library Management System ")
    login_root.geometry("400x300")
    login_root.resizable(False, False)
    login_root.config(bg="gray")

    # Create a frame to hold the widgets
    tk.Label(text="Login Panel", font=("Times", "14", "bold "),
             pady=10, bg="gray").pack()
    frame = tk.Frame(login_root)

    frame = tk.Frame(login_root, bg="gray")
    frame.pack(pady=5)

    # Create the widgets
    # creating a label and input box for user id and password
    uid_label = tk.Label(frame, text="User ID",
                         font=("Times", "12", "bold "), bg="gray")
    uid_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

    pswd_label = tk.Label(frame, text="Password",
                          font=("Times", "12", "bold "), bg="gray")
    pswd_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")

    uid_entry = tk.Entry(frame, font=("Times", "12", "bold "),
                         width=25, highlightthickness=2, highlightcolor="red")
    uid_entry.grid(row=0, column=1, padx=10, pady=10)

    pswd_entry = tk.Entry(
        frame, show="*", font=("Times", "12", "bold "), width=25, highlightthickness=2, highlightcolor="red")
    pswd_entry.grid(row=1, column=1, padx=10, pady=10)


# when this button is clicked  it will call the login function
    login_btn = tk.Button(frame, text="Login", bg="#18C809",
                          fg="white", padx=15, command=lambda: login(uid_entry, pswd_entry))
    login_btn.grid(row=2, column=0, columnspan=2, padx=5,
                   pady=5, )

# when this button is clicked  it will call the register_window function
# and register gui is opened to register for new user.

    reg_btn = tk.Button(frame, text="Register", bg="#0624DA",
                        fg="white", padx=12, command=lambda: register_window())
    reg_btn.grid(row=3, column=0, columnspan=2, padx=5,
                 pady=5, )
    login_root.mainloop()


# this function is called when login button is clicked
def login(uid_entry, pswd_entry):

    uid = uid_entry.get()
    pswd = pswd_entry.get()
    print(uid, pswd)

    # provide user id and password to authenticate function
    v, u = authenticate(uid, pswd)

    if v:
        messagebox.showinfo("Login Successful",
                            "Welcome to the BCU Library System!")

        # Name = u[1]
        # userid = uid
        # password = u[2]
        # usertype = u[3]
        # deptorclass = u[4]

# when user is verified it provide the menu according to userType
# and  provide data to  class
# visit UserClass.py for more details
        if u[3] == "Staff":
            usr = Staff(u[1], uid, u[3], u[4])
            messagebox.showinfo("Credential Verification ",
                                "Now verifying your credentials please wait......Press OK to continue")

            usr.menu()
        elif u[3] == "Student":
            usr = Student(u[1], uid, u[3], u[4])
            messagebox.showinfo("Credential Verification ",
                                "Now verifying your credentials please wait......Press OK to continue")

            usr.menu()
        elif u[3] == "Librarian":
            messagebox.showinfo("Credential Verification ",
                                "Now verifying your credentials please wait......Press OK to continue")

            print('1', u[1], '2', uid, '3', u[2])
            usr = Librarian(u[1], uid, u[3], u[2])
            usr.menu()

        else:
            messagebox.showerror(
                "Data Error", "Invalid User ID or Password")

    else:
        messagebox.showerror(
            "Login Failure", "Invalid User ID or Password")


# this method authenticates the user
def authenticate(uid, pswd):

    # Create connection to database
    conn = sqlite3.connect("library.db")
    cursorObject = conn.cursor()
    try:

        with conn:

            # selects the UserID and Password from the Users table
            # compare it with the provided UserID and Password
            cursorObject.execute("SELECT * FROM Users WHERE UserID = ? AND Password = ?",
                                 (uid, pswd))
            user_data = cursorObject.fetchone()

            # Name = u[1]
            # userid = uid
            # password = u[2]
            # usertype = u[3]
            # deptorclass = u[4]

            if user_data is not None:
                if user_data[2] == pswd:
                    return True, user_data
            return False, None
    except Exception as e:
        print(e)
        messagebox.showerror("Login Failure", 'Invalid User ID or Password')

# this methods uses  authenticate method to verify the user
# when user is verified it provide the menu according to userType
# and  provide data to  class


# this method is used to register the user


def register(name_entry, uid_entry, pswd_entry, user_type_entry, dept_or_class_entry):

    # Create connection to database
    conn = sqlite3.connect("library.db")
    cursorObject = conn.cursor()
    # In
    uid = uid_entry.get()
    print(uid)
    pswd = pswd_entry.get()
    name = name_entry.get()
    dept = dept_or_class_entry.get()
    usertype = user_type_entry.get()
    print(uid, pswd, name, dept, usertype)

    try:
        with conn:
            # checks for empty fields
            if uid == " " or pswd == " " or name == " " or dept == " " or usertype == " ":
                messagebox.showerror("Registration Failure",
                                     "Please fill in all the fields")
            else:

                # checks if the user id already exists
                cursorObject.execute(
                    "SELECT * FROM Users WHERE UserID = ?", (uid,))
                result = cursorObject.fetchone()

                if result:
                    messagebox.showerror(
                        "Registration Failure", "User ID already exists")

                else:
                    # inserts the user data into the Users table
                    cursorObject.execute("INSERT INTO Users VALUES (?,?,?,?,?)",
                                         (uid, name, pswd, usertype, dept))
                    messagebox.showinfo("Registration Successful",
                                        "You have successfully registered!")
    except Exception as e:
        messagebox.showerror("Registration Failure", e)
    conn.commit()
    cursorObject.close()


def register_window():
    reg_root = tk.Tk()

    # set the title, size, background color and disable the resizing property of the window
    reg_root.title("Library Management System ")
    reg_root.geometry("400x400")
    reg_root.config(bg="gray")

    # Create a frame to hold the widgets
    tk.Label(reg_root, text="User Registration", font=("Times", "14", "bold "),
             pady=10, bg="gray").pack()

    frame = tk.Frame(reg_root, bg="gray")
    frame.pack(pady=5)

    # Create the widgets
    # creating a label and input box for user id and password

    name_label = tk.Label(frame, text="Name",
                          font=("Times", "12", "bold "), bg="gray")
    name_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

    uid_label = tk.Label(frame, text="User ID",
                         font=("Times", "12", "bold "), bg="gray")
    uid_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")

    pswd_label = tk.Label(frame, text="Password",
                          font=("Times", "12", "bold "), bg="gray")
    pswd_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")

    user_type_label = tk.Label(frame, text="User Type",
                               font=("Times", "12", "bold "), bg="gray")
    user_type_label.grid(row=3, column=0, padx=10, pady=10, sticky="w")

    dept_or_class_label = tk.Label(frame, text="Department/Class",
                                   font=("Times", "12", "bold "), bg="gray")
    dept_or_class_label.grid(row=4, column=0, padx=10, pady=10, sticky="w")

    name_entry = tk.Entry(frame, font=("Times", "12", "bold "),
                          width=25, highlightthickness=2, highlightcolor="red")
    name_entry.grid(row=0, column=1, padx=10, pady=10)

    uid_entry = tk.Entry(frame, font=("Times", "12", "bold "),
                         width=25, highlightthickness=2, highlightcolor="red")
    uid_entry.grid(row=1, column=1, padx=10, pady=10)

    pswd_entry = tk.Entry(frame, show="*", font=("Times", "12", "bold "),
                          width=25, highlightthickness=2, highlightcolor="red")
    pswd_entry.grid(row=2, column=1, padx=10, pady=10)

    # creating a select box for user type
    user_type = tk.StringVar()
    user_type = ttk.Combobox(frame, textvariable=user_type,
                             font=("Times", "12", "bold "), width=23, state="readonly")
    user_type["values"] = ("Student", "Staff", "Librarian")
    user_type.current(0)
    user_type.grid(row=3, column=1, padx=10, pady=10)

    # creating input box for department or class

    dept_or_class_entry = tk.Entry(frame, font=("Times", "12", "bold "),
                                   width=25, highlightthickness=2, highlightcolor="red")
    dept_or_class_entry.grid(row=4, column=1, padx=10, pady=10)

    register_btn = tk.Button(frame, text="Register", bg="#18C809",
                             fg="white", padx=15, command=lambda: getRegister()



                             )
    register_btn.grid(row=5, column=0, columnspan=2, padx=5,
                      pady=5, )


# this function is called when register button is clicked

    def getRegister():

        # passing  entered data to register function
        register(name_entry, uid_entry,
                 pswd_entry, user_type, dept_or_class_entry)

        # clearing the entry boxes
        name_entry.delete(0, tk.END),
        uid_entry.delete(0, tk.END),
        pswd_entry.delete(0, tk.END),
        dept_or_class_entry.delete(0, tk.END)

    reg_root.mainloop()
