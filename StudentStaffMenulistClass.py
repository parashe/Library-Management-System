import tkinter as tk
from AccountClass import Account
from StudentStaffActionClass import StudentStaffAction

# This class create everything you see when you are logged in as a student or staff
# This class creates the menu for the student/staff
# where it call the every function from the StudentStaff class
# all button are created and functions are called from StudentStaffAction class


class Student_Staff_MenuList:
    def __init__(self, uid, name, UserType):
        self.uid = uid
        self.name = name
        self.UserType = UserType

    # gives the Main window for student and staff

    def menu_Window(self):

        # creating the instance of StudentStaffAction to call function
        StudentStaffAction_instance = StudentStaffAction(self.uid)

        # creating the instance of Account to call function
        Account_instance = Account(self.uid)

        # creating  new instance of a Tkinter
        Studentmenu = tk.Tk()
        Studentmenu.title("Library Management System ")
        Studentmenu.geometry("600x400")
        Studentmenu.configure(bg="gray")

        # Create a frame to hold the widgets
        tk.Label(Studentmenu, text=f"Welcome to {self.UserType} Page", font=("Times", "15", "bold "),
                 pady=10, bg="gray").pack()
        frame = tk.Frame(Studentmenu, bg="gray")

        # Create a frame to hold the widgets
        # provides the user details of student or staff  in menu

        tk.Label(Studentmenu, text=f"UserID: {self.uid}", bg='gray').pack(
            pady=0)
        tk.Label(Studentmenu, text=f"Name: {self.name}",  bg='gray').pack(
            pady=0)
        tk.Label(Studentmenu, text=f" User Type: {self.UserType}", bg='gray').pack(
            pady=0)
        frame = tk.Frame(Studentmenu, bg="gray")
        frame.pack(pady=10)

 # this  buttons calls the borrowBook() function from studentStaffAction to  borrow books
        borrow_btn = tk.Button(frame, text="Borrow Books", bg="#18C809",
                               fg="white", padx=15, command=lambda: StudentStaffAction_instance.borrowBook())

        borrow_btn.grid(row=2, column=0, columnspan=2, padx=5,
                        pady=5)

        # this  buttons calls the reserveBook() function from studentStaffAction to  reserve books
        reserve_btn = tk.Button(frame, text="Reserve Books", bg="#4503fc",
                                fg="white", padx=15, command=lambda: StudentStaffAction_instance.reserveBook()
                                )
        reserve_btn.grid(row=2, column=2, columnspan=2, padx=5,
                         pady=5, )

        # this  buttons calls the renewBook() function from studentStaffAction to  renew books
        renew_btn = tk.Button(frame, text="Renew Books", bg="#6C06DA",
                              fg="white", padx=5, command=lambda: StudentStaffAction_instance.renewBook()
                              )
        renew_btn.grid(row=2, column=4, columnspan=2, padx=15,
                       pady=5, )

        # this  buttons calls the returnBook() function from studentStaffAction to  return books
        return_btn = tk.Button(frame, text="Return Books", bg="#fc030b",
                               fg="white", padx=5, command=lambda: StudentStaffAction_instance.returnBook()

                               )
        return_btn.grid(row=2, column=6, columnspan=2, padx=15,
                        pady=5, )

        # this  buttons calls the getAccount() function from Account to  get account details
        account_btn = tk.Button(frame, text="Account Report", bg="#eb059e",
                                fg="white", padx=5, command=lambda: Account_instance.get_account()
                                )
        account_btn.grid(row=3, column=0, columnspan=2, padx=0,
                         pady=5, )

        # this  buttons calls the getReservedBook() function from Account to  get reserved books

        view_reserved_Books = tk.Button(frame, text="View Reserved Books", bg="#c74d0c",
                                        fg="white", padx=10, command=lambda: StudentStaffAction_instance.getReservedBooks()
                                        )

        view_reserved_Books.grid(row=3, column=2, columnspan=2,
                                 pady=5, padx=20)

        # this  buttons calls the getBorrowedBooks() function from Account to  get borrowed books

        view_borrowed_Books = tk.Button(frame, text="View Borrowed Books", bg="#8f0cc7",
                                        fg="white", padx=5, command=lambda: StudentStaffAction_instance.getBorrowedBooks()
                                        )
        view_borrowed_Books.grid(row=3, column=4, columnspan=2, padx=0,
                                 pady=5, )

        # this  buttons calls the getAvailablebook() function from studentStaffAction to  get available books
        view_available_Books = tk.Button(frame, text="View Available Books", bg="green",
                                         fg="white", padx=5, command=lambda: StudentStaffAction_instance.getAvailablebook()
                                         )
        view_available_Books.grid(row=3, column=6, columnspan=2, padx=5,
                                  pady=5, )

        # this  buttons calls the getAllBooks() function from studentStaffAction to  get all books

        view_all_Books = tk.Button(frame, text="View All Books", bg="#DAC406",
                                   fg="white", padx=5, command=lambda: StudentStaffAction_instance.getAllBooks()
                                   )
        view_all_Books.grid(row=4, column=2, columnspan=2, padx=0,
                            pady=5, )

        # this  buttons calls the searchBook() function from studentStaffAction to  search books
        search_btn = tk.Button(frame, text="Search for Books", bg="#e67e22",
                               fg="white", padx=5, command=lambda: StudentStaffAction_instance.searchBook()
                               )
        search_btn.grid(row=4, column=4, columnspan=2, padx=15,
                        pady=5, )

        Studentmenu.mainloop()
