from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]

    shuffle(password_list)

    password = "".join(password_list)

    txt_password.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = txt_website.get()
    username = txt_username.get()
    password = txt_password.get()
    new_data = {
        website : {
            "email": username,
            "password" : password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(title="Invalid info", message="Something does not seem right with your entries. Please"
                                                           "make sure you haven't left anything empty")
    else:
        with open("data.json", "r") as data_file:
            # Reading old data
            data = json.load(data_file)
            # Updating old data with new data
            data.update(new_data)
            
        # Save updated data
        with open("data.json", "w") as data_file:
            json.dump(data, data_file, indent=4)
            txt_website.delete(0, END)
            txt_password.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Logo
canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

# Labels
lbl_website = Label(text="Website:")
lbl_website.grid(row=1, column=0)
lbl_username = Label(text="Email/Username:")
lbl_username.grid(row=2, column=0)
lbl_password = Label(text="Password:")
lbl_password.grid(row=3, column=0)

# Entries
txt_website = Entry(width=35)
txt_website.grid(row=1, column=1, columnspan=2)
txt_website.focus()
txt_username = Entry(width=35)
txt_username.insert(0, "username@mail.com")
txt_username.grid(row=2, column=1, columnspan=2)
txt_password = Entry(width=21)
txt_password.grid(row=3, column=1)

# Buttons
btn_password = Button(text=" Generate Password", command=generate)
btn_password.grid(row=3, column=2)
btn_add = Button(width=36, text="Add", command=save)
btn_add.grid(row=4, column=1, columnspan=2)


window.mainloop()
