from tkinter import *
from tkinter import messagebox
from random import *
import pyperclip
import json

file = "C:/Users/USER/3D Objects/Passwords/save_file.json"

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
    # Window Configuration
    window = Tk()
    window.title("Home Window")
    window.config(padx=50, pady=25)

    # Canvas Setup3
    icon = PhotoImage(file="./logo.png")
    canvas = Canvas(master=window, width=200, height=200)
    canvas.create_image(100, 100, image=icon)
    canvas.grid(column=1, row=0)

    # Button & Text Setup
    welcome_text = Label(text="Welcome User, Please Select an option", pady=10)
    welcome_text.grid(column=1, row=1)

    button1 = Button(text="Open Password Manager", command=lambda: open_window(password_window, window))
    button1.grid(column=1, row=2)

    button2 = Button(text="Settings", command=lambda :open_window(settings_window, window))
    button2.grid(column=1, row=3)

    window.mainloop()


def password_window():
    with open("settings.json") as settings:
        settings_data = json.load(settings)
        def_mail = settings_data["email"]
        def_num = settings_data["numbers"]
        def_sym = settings_data["symbols"]
        def_let = settings_data["letters"]

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
                with open(file, "r") as save_file:
                    data = json.load(save_file)
            except FileNotFoundError:
                with open(file, "w") as save_file:
                    json.dump(new_data, save_file)
            else:
                data.update(new_data)
                with open(file, "w") as save_file:
                    json.dump(data, save_file, indent=4)
            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)

    def generate_password():
        nr_letters = int(def_let)
        nr_symbols = int(def_sym)
        nr_numbers = int(def_num)

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
            with open(file, "r") as save_file:
                data: dict = json.load(save_file)
                details = data.get(website_entry.get())
                if details is None:
                    raise KeyError
                messagebox.showinfo(title=website_entry.get(), message=f"Email: {details["email"]} "
                                                                       f"\nPassword: {details["password"]}"
                                                                       f"\nPassword has been copied to clipboard")
                pyperclip.copy(details["password"])
                email_entry.delete(0, END)
                email_entry.insert(0, details["email"])
                password_entry.delete(0, END)
                password_entry.insert(0, details["password"])
        except (FileNotFoundError, KeyError):
            messagebox.showinfo(title="Error", message=f"No Details for {website_entry.get()}")

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
    email_entry.insert(END, def_mail)
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


def settings_window():
    def save_settings():
        new_settings = {
            "email": email_entry.get(),
            "letters": letter_entry.get(),
            "symbols": symbol_entry.get(),
            "numbers": number_entry.get(),
            "file": "save_file.json"
        }

        with open("settings.json", "r") as settings_file:
            save_data: dict = json.load(settings_file)
            save_data.update(new_settings)

        with open("settings.json", "w") as settings_file:
            json.dump(save_data, settings_file, indent=4)

        messagebox.showinfo(title="Saved", message="Settings have been saved")
        window.destroy()
        open_window(home_window)

    # Window Configuration
    window = Tk()
    window.title("Settings")
    window.config(padx=50, pady=20)

    # Title Setup
    email_label = Label(text="Settings", font=("Cambria", 20, "bold"))
    email_label.grid(column=1, row=0)

    # Labels
    email_label = Label(text="Default Mail:")
    email_label.grid(column=0, row=1)
    number_label = Label(text="Number Count:")
    number_label.grid(column=0, row=2)
    symbol_label = Label(text="Symbol Count:")
    symbol_label.grid(column=0, row=4)
    letter_label = Label(text="Letter Count:")
    letter_label.grid(column=0, row=3)

    with open("settings.json") as file:
        data = json.load(file)

    # Entries
    email_entry = Entry(width=35)
    email_entry.grid(column=1, row=1, columnspan=2, sticky="EW")
    email_entry.insert(0, data["email"])
    number_entry = Entry(width=35)
    number_entry.grid(column=1, row=2, columnspan=2, sticky="EW")
    number_entry.insert(0, data["numbers"])
    letter_entry = Entry(width=35)
    letter_entry.grid(column=1, row=3, columnspan=2, sticky="EW")
    letter_entry.insert(0, data["letters"])
    symbol_entry = Entry(width=35)
    symbol_entry.grid(column=1, row=4, columnspan=2, sticky="EW")
    symbol_entry.insert(0, data["symbols"])

    # Button
    save_button = Button(text="Save", command=save_settings)
    save_button.grid(column=1, row=5, sticky="EW")

    window.protocol("WM_DELETE_WINDOW", lambda: open_window(home_window, window))
    window.mainloop()


home_window()
