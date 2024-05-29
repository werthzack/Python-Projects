from tkinter import *
from tkinter import messagebox
from random import *
import pyperclip
import os
import json

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
           'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
           'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def open_window(func, window=None):
    if window:
        window.destroy()
    func()


def home_window():
    def open_file():
        if os.path.exists("save_file.txt"):
            os.startfile("save_file.txt")
        else:
            messagebox.showinfo(title="Error", message="No Save Data Detected")
    # Window Configuration
    window = Tk()
    window.title("Home Window")
    window.config(padx=50, pady=25)

    # Canvas Setup3
    icon = PhotoImage(file="logo.png")
    canvas = Canvas(master=window, width=200, height=200)
    canvas.create_image(100, 100, image=icon)
    canvas.grid(column=1, row=0)

    # Button & Text Setup
    welcome_text = Label(text="Welcome User, Please Select an option", pady=10)
    welcome_text.grid(column=1, row=1)

    button1 = Button(text="Open Password Manager", command=lambda: open_window(password_window, window))
    button1.grid(column=1, row=2)

    button2 = Button(text="Settings", command=open_file)
    button2.grid(column=1, row=3)

    window.mainloop()


def password_window():
    # Functions
    def add_password():
        if email_entry.get() == "" or password_entry.get() == "" or website_entry.get() == "":
            messagebox.showinfo(title="Missing Fields", message="Error, not all fields have been filled")
            return

        confirm = messagebox.askokcancel(title=website_entry.get(), message=f"These are the details you entered:"
                                                                            f"\nEmail:{email_entry.get()}\nPassword:"
                                                                            f"{password_entry.get()}\nDo you want to "
                                                                            f"proceed?")
        if confirm:
            new_data = {
                website_entry.get(): {
                    "email": email_entry.get(),
                    "password": password_entry.get()
                }
            }
            messagebox.showinfo(title="Success", message="Your Details have been saved successfully")
            try:
                with open("save_file.json", "r") as save_file:
                    data = json.load(save_file)
            except FileNotFoundError:
                with open("save_file.json", "w") as save_file:
                    json.dump(new_data, save_file)
            else:
                data.update(new_data)
                with open("save_file.json", "w") as save_file:
                    json.dump(data, save_file, indent=4)
            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)

    def generate_password():
        nr_letters = randint(8, 10)
        nr_symbols = randint(2, 4)
        nr_numbers = randint(2, 4)

        char_list = [choice(letters) for _ in range(nr_letters)]
        symbol_list = [choice(symbols) for _ in range(nr_symbols)]
        number_list = [choice(numbers) for _ in range(nr_numbers)]

        password_list = char_list + symbol_list + number_list

        shuffle(password_list)

        password = "".join(password_list)

        password_entry.delete(0, END)
        password_entry.insert(0, password)
        pyperclip.copy(password)

    def find_info():
        try:
            with open("save_file.json", "r") as save_file:
                data: dict = json.load(save_file)
                details = data.get(website_entry.get())
        except (FileNotFoundError, KeyError):
            messagebox.showinfo(title="Error", message="Website details does not exist")
        else:
            data.update(new_data)
            with open("save_file.json", "w") as save_file:
                json.dump(data, save_file, indent=43)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

    # Window Configuration
    window = Tk()
    window.title("Password Window")
    window.config(padx=50, pady=20)

    # Canvas Setup
    icon = PhotoImage(file="logo.png")
    canvas = Canvas(master=window, width=200, height=200)
    canvas.create_image(100, 100, image=icon)
    canvas.grid(column=1, row=0, sticky="EW")

    # Button & Text Setup
    website_label = Label(text="Website:", width=10)
    website_label.grid(column=0, row=1, sticky="E")
    email_label = Label(text="Email:", width=10)
    email_label.grid(column=0, row=2, sticky="E")
    password_label = Label(text="Password:", width=10)
    password_label.grid(column=0, row=3, sticky="E")

    website_entry = Entry(width=35)
    website_entry.grid(column=1, row=1, columnspan=2, sticky="EW")
    website_entry.focus()
    email_entry = Entry(width=35)
    email_entry.grid(column=1, row=2, columnspan=2, sticky="EW")
    email_entry.insert(END, "@gmail.com")
    password_entry = Entry(width=21)
    password_entry.grid(column=1, row=3, sticky="EW")

    search_button = Button(text="Search", command=find_info)
    search_button.grid(column=2, row=1, sticky="EW")
    generate_button = Button(text="Generate Password", command=generate_password)
    generate_button.grid(column=2, row=3, sticky="EW")
    add_button = Button(text="Add", width=10, command=add_password)
    add_button.grid(column=1, row=4, columnspan=2, sticky="EW")

    window.protocol("WM_DELETE_WINDOW", lambda: open_window(home_window, window))
    window.mainloop()


home_window()
