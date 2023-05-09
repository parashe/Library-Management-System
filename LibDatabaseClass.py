import insertCategoryFunction
import insertBookFunction
import getAllBooksFunction
import updateDeleteBookFunction
import getAllAccountDetailsFunction
import getAlluserListFunction
import getBorrowedBooksFunction
import getReservedBooksFunction
import searchBookFunction


# This class provides an interface to interact with the different functions .
# This class is called from the LibrarianMenuListClass.py
# This class is middlware for every function for library page to LibrarianMenuListClass.py

class LibDatabase:

    def __init__(self):
        pass

# This function calls the insert_category_ui() function from insertCategoryFunction.py
    def insertCategory(self):
        insertCategoryFunction.insert_category_ui()


# This function calls the insert_book_ui() function from insertBookFunction.py

    def insertBook(self):
        insertBookFunction.insert_book_ui()

# This function calls the updateBook() function from updateDeleteBookFunction.py
    def updateBook(self):
        updateDeleteBookFunction.get_isbn_to_update_book_ui()

# This function calls the deleteBook() function from updateDeleteBookFunction.py
    def deleteBook(self):
        updateDeleteBookFunction.get_isbn_to_delete_book_ui()

# This function calls the get_all_book() function from getAllBooksFunction.py
    def getAllBooks(self):
        getAllBooksFunction.get_all_book()

# This function calls the getAllUser() function from getAlluserListFunction.py
    def getAllUser(self):
        getAlluserListFunction.get_all_user()

# This function calls the getAllBorrowedBooks() function from getBorrowedBooksFunction.py
    def getAllBorrowedBooks(self):
        getBorrowedBooksFunction.get_all_borrowed_books()

# This function calls the getAllReservedBooks() function from getReservedBooksFunction.py
    def getAllReservedBooks(self):
        getReservedBooksFunction.get_all_reserved_books()

# This function calls the getAllAccountDetails() function from getAllAccountDetailsFunction.py
    def getAllAccountDetails(self):
        getAllAccountDetailsFunction.get_all_account_details()


# This function calls the search_book_window() function from searchBookFunction.py


    def searchBook(self):
        searchBookFunction.search_book_ui()
