import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3
import random


# This function insert category into the database table
# This function is used by librarian to insert category into the database
# this function is called in LibDatabaseClass.py
# This function verify the category already exists or not

def insert_category(category):
    # connecting to database
    conn = sqlite3.connect('library.db')
    cursorObject = conn.cursor()

    try:
        with conn:
            # checking gor fields
            if category == "":
                messagebox.showerror("Error", "Please fill all the fields")

            # checkin if the category already exists
            elif cursorObject.execute("SELECT * FROM category WHERE category = :category", {'category': category}):
                result = cursorObject.fetchone()
                if result:
                    messagebox.showerror(
                        "Error", "Category with the given name already exists")
                else:

                    # creating a unique category_id

                    cur3 = cursorObject.execute(
                        'SELECT Count(category_id) FROM category')
                    max_id = cur3.fetchone()[0]

                    print('max_id', max_id)
                    generated_category_id = max_id + random.randint(1, 1000)
                    print('reserve_id:', generated_category_id)

                    cursorObject.execute("INSERT INTO category VALUES(:category_id,:category)", {
                        'category_id': generated_category_id, 'category': category})
                    messagebox.showinfo("Category has been created Successfully",
                                        "You have successfully Added Category!")

    except Exception as e:

        messagebox.showerror(
            "Error", e)


# this is Gui for insert category
def insert_category_ui():

    # creating  new instance of a Tkinter

    insercategory = tk.Tk()

    # set the title, size, background color and disable the resizing property of the window
    insercategory.title("Library Management System ")
    insercategory.geometry("400x250")
    insercategory.config(bg="gray")

    # Create a frame to hold the widgets
    tk.Label(insercategory, text="Add Category", font=("Times", "14", "bold "),
             pady=10, bg="gray").pack()

    frame = tk.Frame(insercategory, bg="gray")
    frame.pack(pady=5)

    # Create the widgets
    category_label = tk.Label(frame, text="Category",
                              font=("Times", "12", "bold "), bg="gray")
    category_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")

    category_entry = tk.Entry(
        frame, font=("Times", "12", "bold "), width=25, highlightthickness=2, highlightcolor="red")

    category_entry.grid(row=1, column=1, padx=10, pady=10)

    insertCategory_btn = tk.Button(frame, text="Add Category", bg="#18C809", font=("Times", "10", "bold "),
                                   fg="black", padx=15, command=lambda: insertCategory_btns())
    insertCategory_btn.grid(row=5, column=0, columnspan=2, padx=5,
                            pady=5, )


# this function is called when borrow button is clicked

    def insertCategory_btns():
        insert_category(category_entry.get())
        category_entry.delete(0, tk.END)

    insercategory.mainloop()
