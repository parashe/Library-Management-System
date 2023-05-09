import borrowBookFunction
import returnBookFuntion
import reserveBookFunction
import renewBookFunction
import getAvailablebookFunction
import getBorrowedBooksFunction
import searchBookFunction
import getAllBooksFunction
import getReservedBooksFunction
import getAllBooksFunction


# This class provides an interface to interact with the different functions .
# This class is called from the StudentStaffMenuListClass.py
class StudentStaffAction:

    def __init__(self, uid):
        self.uid = uid


# This function calls the borrow_book_window() function from borrowBookFunction.py

    def borrowBook(self):
        borrowBookFunction.borrow_book_window(self.uid)

# This function calls the reserve_book_window() function from reserveBookFunction.py

    def reserveBook(self):
        reserveBookFunction.reserve_book_window(self.uid)

# This function calls the renew_book_window() function from renewBookFunction.py

    def renewBook(self):
        renewBookFunction.renew_book_window(self.uid)

# This function calls the return_book_window() function from returnBookFunction.py
    def returnBook(self):
        returnBookFuntion.return_book_window(self.uid)

# This function calls the get_reserved_book_by_UserID() function from getReservedBooksFunction.py

    def getReservedBooks(self):
        getReservedBooksFunction.get_reserved_book_by_UserID(self.uid)

# This function calls the get_borrowed_book_by_UserID() function from getBorrowedBooksFunction.py

    def getBorrowedBooks(self):
        getBorrowedBooksFunction.get_borrowed_book_by_UserID(self.uid)

# This function calls the get_available_book() function from getAvailablebookFunction.py
    def getAvailablebook(self):
        getAvailablebookFunction.get_available_book()

# This function calls the get_all_book() function from getAllBooksFunction.py
    def getAllBooks(self):
        getAllBooksFunction.get_all_book()


# This function calls the search_book_window() function from searchBookFunction.py


    def searchBook(self):
        searchBookFunction.search_book_ui()
