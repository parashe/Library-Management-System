import sqlite3
from tkinter import messagebox
from StudentStaffMenulistClass import Student_Staff_MenuList
from LibrarianMenuListClass import Librarian_MenuList


# this class verify the user and provide the menu according to userType
# User is parent class and student and staff  and librarian are child class
# inheritance is implemented here
# multiple verification is done first in the login side and another in User the userType validation.
# according to the usetype the menu is provided to the user
# if user is student/staff then it will goes to Student_Staff_MenuList class
# if user is librarian then it will goes to Librarian_MenuList class

class User:
    conn = sqlite3.connect("library.db")
    cursorObject = conn.cursor()

    def __init__(self, name, uid, UserType, deptorclass):
        self.name = name
        self.uid = uid,
        self.UserType = UserType
        self.deptorclass = deptorclass

    def __repr__(self):
        return f"{self.name}"

    # checking credentials according to the class diagram given

    def verify_user(self, uid, password, UserType):

        try:
            with self.conn:
                self.cursorObject.execute("SELECT * FROM Users WHERE UserID=? AND UserType=? AND Password=?",
                                          (uid, UserType, password))
                result = self.cursorObject.fetchone()

                # result[3]=UserType
                # if userType is student then it will return true
                if result[3] == "Student":
                    print("Successfully Verified")
                    messagebox.showinfo("Successfully Verified",
                                        "yeah ! you are logged in as Student")
                    self.name = result[1]
                    self.uid = result[2]
                    self.UserType = result[3]
                    self.deptorclass = result[4]
                    return True

                # if userType is staff then it will return true and verified
                elif result[3] == "Staff":
                    print("Successfully Verified")
                    messagebox.showinfo("Successfully Verified",
                                        "yeah ! you are logged in  as Staff")
                    self.name = result[1]
                    self.uid = result[2]
                    self.uid = result[3]
                    self.uid = result[4]
                    return True

                # if userType is librarian then it will return true and verified
                elif result[3] == "Librarian":
                    print("Successfully Verified")
                    messagebox.showinfo("Successfully Verified",
                                        "yeah ! you are logged in as Librarian")
                    self.name = result[1]
                    self.uid = result[2]
                    self.uid = result[3]
                    return True

                else:
                    print("Invalid credentials")
                    messagebox.showinfo("Invalid credentials",
                                        "Invalid credentials Please try again")
                    return False
        except Exception as e:
            print(e)
            messagebox.showinfo("Error", "Failed to verify user")


class Student(User):
    def __init__(self, name, uid, UserType, sClass):
        super().__init__(name, uid, UserType, sClass)
        self.sClass = sClass
        self.uid = uid
        self.name = name
        self.UserType = UserType

    # def foo(self):

    def menu(self):
        while True:

            # creating an instance of Student_Staff_MenuList class that is in StudentStaffMenulist.py
            menulist_instance = Student_Staff_MenuList(
                self.uid, self.name, self.UserType)

            # calling the menu_Window function  that is in StudentStaffMenulist.py to get menu for staff

            menulist_instance.menu_Window()


class Staff(User):

    def __init__(self, name, uid, UserType, sDept):
        super().__init__(name, uid, UserType, sDept)
        self.sDept = sDept
        self.uid = uid
        self.name = name
        self.UserType = UserType

    # menu list for staff and student is same.

    def menu(self):
        while True:

            # creating an instance of Student_Staff_MenuList class that is in StudentStaffMenulist.py file/module

            menulist_instance = Student_Staff_MenuList(
                self.uid, self.name, self.UserType)

            # calling the menu_Window function  that is in StudentStaffMenulist.py to get menu for staff
            menulist_instance.menu_Window()


class Librarian(User):
    def __init__(self, name, uid, UserType, password):
        self.name = name
        self.id = uid
        self.password = password
        self.UserType = UserType

        #  calling the parent function verify_user to verify the user
        # user id and password  and userType is passed to verify_user to verified here
        super().verify_user(uid, password, UserType)

    def menu(self):
        while True:

            # creating an instance of Lbrarian_MenuList class

            Librarian_MenuList_instance = Librarian_MenuList(
                self.uid, self.name, self.UserType)

            # calling librarian_menu_window function that is in LibrarianMenuList.py to get menu for librarian
            # passing value uid, name, UserType to the function
            Librarian_MenuList_instance.librairan_menu_window()
