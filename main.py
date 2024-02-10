from tkinter import *
from tkinter import messagebox
import random
import json
FONT = ("Arial", 10, "bold")
PASSWORD_LET = 8
PASSWORD_SYM = 4
PASSWORD_NUM = 4
length = PASSWORD_NUM + PASSWORD_LET + PASSWORD_SYM
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
           "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R","S", "T", "U", "V", "S", "T", "U", "V", "W", "X", "Y", "Z"]
symbols = ["!", "£", "$", "^", "&", "*", "(", ")", "=", "+", "/", "{", "}", "[", "]"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]


def add_password():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }


    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        try:
            with open("data.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


def generate_password():
    password_blank = []
    password_entry.delete(0, END)
    for i in range(1, (PASSWORD_LET + 1)):
        letter = letters[random.randint(0, 49)]
        password_blank.append(letter)

    for j in range(1, (PASSWORD_SYM + 1)):
        symbol = symbols[random.randint(0, 14)]
        password_blank.append(symbol)

    for k in range(1, (PASSWORD_NUM + 1)):
        number = numbers[random.randint(0, 9)]
        password_blank.append(number)
    random.shuffle(password_blank)
    password_final = ''.join(password_blank)
    password_entry.insert(0, password_final)


def search():
    website = website_entry.get()
    if website == "":
        print("No value entered, please try again")
    else:
        try:
            with open("data.json", "r") as file:
                data = json.load(file)
        except FileNotFoundError as file_error:
            messagebox.showinfo(title="Error", message="No password database found")
        else:
            found_website = website in data
            if found_website:
                email = data[website]["email"]
                password = data[website]["password"]
                messagebox.showinfo(title="info", message=f"Email: {email}, Password: {password}")
            else:
                print("No data found matching your search query")
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #





window = Tk()
window.title("Password Manager")
window.config(padx=40, pady=40)

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

website_lbl = Label(text="Website: ", font=FONT)
website_lbl.grid(row=1, column=0)
email_lbl = Label(text="Email/Username: ", font=FONT)
email_lbl.grid(row=2, column=0)
password_lbl = Label(text="Password: ", font=FONT)
password_lbl.grid(row=3, column=0)

website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, sticky="W", columnspan=2)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.insert(0, "lewiscade27@gmail.com")
email_entry.grid(row=2, column=1, sticky="W", columnspan=2)
password_entry = Entry(width=35)
password_entry.grid(row=3, column=1, sticky="W")

gen_password_btn = Button(text="Generate", font=FONT, command=generate_password)
gen_password_btn.grid(row=3, column=2)
add_btn = Button(text="Add", font=FONT, width=12, command=add_password)
add_btn.grid(row=4, column=1, sticky="W", columnspan=2)
search_btn = Button(text="Search", font=FONT, command=search)
search_btn.grid(row=1, column=2)


window.mainloop()
