import tkinter as tk
import LibDatabaseClass

# This class create everything you see when you are logged in as a librarian
# This class creates the menu for the librarian
# where it call the every function from the LibDatabase class
# all button are created and functions are called from LibDatabase class


class Librarian_MenuList:
    def __init__(self, uid, name, UserType):
        self.uid = uid
        self.name = name
        self.UserType = UserType

    def librairan_menu_window(self):

        # creating the instance of LibDatabase to call function
        # LibDatabaseClass is in LibDatabaseClass.py
        libDatabase_instance = LibDatabaseClass.LibDatabase()

# creatign instance of Tkinter
        librarian_menu = tk.Tk()
        librarian_menu.title("Library Management System ")
        librarian_menu.geometry("600x400")
        librarian_menu.configure(bg="gray")

        # Create a frame to hold the widgets
        # provides the user details of librarian in menu

        tk.Label(librarian_menu, text=f"Welcome to {self.UserType} Page", font=("Times", "15", "bold "),
                 pady=10, bg="gray").pack()
        frame = tk.Frame(librarian_menu, bg="gray")

        tk.Label(librarian_menu, text=f"UserID: {self.uid}", bg='gray').pack(
            pady=0)
        tk.Label(librarian_menu, text=f"Name: {self.name}",  bg='gray').pack(
            pady=0)
        tk.Label(librarian_menu, text=f" User Type: {self.UserType}", bg='gray').pack(
            pady=0)
        frame = tk.Frame(librarian_menu, bg="gray")
        frame.pack(pady=10)

        # button is created to go to the window for the function

        # this  buttons calls the insertCategory() function from libdatabase to insert/create category.
        add_category_btn = tk.Button(frame, text="Add Category", bg="#873e23",
                                     fg="white", padx=5, command=lambda: libDatabase_instance.insertCategory())
        add_category_btn.grid(row=2, column=0, columnspan=2, padx=5,
                              pady=5, )

        # this  buttons calls the insertBook() function from libdatabaseto insert/create book.
        insert_book_btn = tk.Button(frame, text="Add Books", bg="#3498db",
                                    fg="white", padx=15, command=lambda: libDatabase_instance.insertBook())

        insert_book_btn.grid(row=2, column=2, columnspan=2, padx=5,
                             pady=5)

        # this  buttons calls the updateBook() function from libdatabase to update book.
        UpdateBook_btn = tk.Button(frame, text="Update Book", bg="#8000ff",
                                   fg="white", padx=5, command=lambda: libDatabase_instance.updateBook())
        UpdateBook_btn.grid(row=2, column=4, columnspan=2, padx=5,
                            pady=5, )

        # this  buttons calls the deleteBook() function from libdatabase to delete book.
        UpdateBook_btn = tk.Button(frame, text="Delete Book", bg="#ff0000",
                                   fg="white", padx=5, command=lambda: libDatabase_instance.deleteBook())
        UpdateBook_btn.grid(row=2, column=6, columnspan=2, padx=5,
                            pady=5, )

        # this  buttons calls the getAllBooks() function from libdatabase to get all books.
        get_all_books_btn = tk.Button(frame, text="Show List of Books", bg="#DA068E",
                                      fg="white", padx=15, command=lambda: libDatabase_instance.getAllBooks())

        get_all_books_btn.grid(row=3, column=0, columnspan=2, padx=5,
                               pady=5, )

        # this  buttons calls the get_all_user() function from libdatabase to get all users.
        getAll_user_btn = tk.Button(frame, text="Get All User", bg="#85cf04",
                                    fg="white", padx=5, command=lambda: libDatabase_instance.getAllUser()
                                    )
        getAll_user_btn.grid(row=3, column=2, columnspan=2, padx=0,
                             pady=5, )

        # this  buttons calls the getAllBorrowedBooks() function from libdatabase to get all borrowed books.
        getAll_borrowedbook_btn = tk.Button(frame, text="Get All borrowed Details", bg="#0950e8",
                                            fg="white", padx=5, command=lambda: libDatabase_instance.getAllBorrowedBooks()
                                            )
        getAll_borrowedbook_btn.grid(row=3, column=4, columnspan=2, padx=0,
                                     pady=5, )

        # this  buttons calls the getAllReservedBooks() function from libdatabase to get all reserved books.
        getAll_reservedbook_btn = tk.Button(frame, text="Get All Reserved Books", bg="#1CDA06",
                                            fg="white", padx=5, command=lambda: libDatabase_instance.getAllReservedBooks()
                                            )
        getAll_reservedbook_btn.grid(row=3, column=6, columnspan=2, padx=5,
                                     pady=5, )

        # this  buttons calls the getAllAccountDetails() function from libdatabase to get all account details.
        getAll_accountDetails_btn = tk.Button(frame, text="Get All Account Details", bg="#ad08bf",
                                              fg="white", padx=5, command=lambda: libDatabase_instance.getAllAccountDetails()
                                              )
        getAll_accountDetails_btn.grid(row=4, column=0, columnspan=2, padx=5,
                                       pady=5, )

        # this  buttons calls the searchBook() function from libdatabase to search book.
        search_btn = tk.Button(frame, text="Search for Books", bg="#e67e22",
                               fg="white", padx=5, command=lambda: libDatabase_instance.searchBook()
                               )
        search_btn.grid(row=4, column=2, columnspan=2, padx=15,
                        pady=5, )

        librarian_menu.mainloop()
