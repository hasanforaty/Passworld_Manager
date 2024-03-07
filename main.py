import tkinter as tk
from tkinter import messagebox as ms

Label_Fonts = ("Arial", 14)
from random import randint, choice, shuffle

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def create_password():
    letter_list = [choice(letters) for _ in range(randint(8, 10))]
    symbol_list = [choice(symbols) for _ in range(randint(2, 4))]
    number_list = [choice(numbers) for _ in range(randint(2, 4))]
    password_list = letter_list + symbol_list + number_list

    shuffle(password_list)

    password = "".join(password_list)
    return password


def generate_password_button():
    password_entry.delete(0, tk.END)
    password = create_password()
    password_entry.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_data():
    email = str(username_entry.get())
    password = str(password_entry.get())
    website = str(web_entry.get())
    if email == "" or password == "" or website == "":
        ms.showerror("Error", "Please enter all fields")
        return
    is_ok = ms.askyesno(title=website, message=f"This are the details entered : \n Email: {email} \n "
                                               f"Password: {password}\n is it oky to continue?")
    if is_ok:
        with open("data.txt", "a") as file:
            file.write(f'Website: {website} || Email: {email} || Password: {password}\n')
            password_entry.delete(0, tk.END)
            web_entry.delete(0, tk.END)


# ---------------------------- UI SETUP ------------------------------- #

windows = tk.Tk()
windows.title("Password Manager")
windows.config(padx=50, pady=50)
# Logo
canvas = tk.Canvas(windows, width=200, height=200)
logo_img = tk.PhotoImage(file="assets/logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)
# Labels
web_label = tk.Label(windows, text="Website:", font=Label_Fonts)
web_label.grid(column=0, row=1)
username_label = tk.Label(windows, text="Email/Username:", font=Label_Fonts)
username_label.grid(column=0, row=2)
password_label = tk.Label(windows, text="Password:", font=Label_Fonts)
password_label.grid(column=0, row=3)

# Entry's
web_entry = tk.Entry(font=Label_Fonts, width=40)
web_entry.grid(column=1, row=1, columnspan=2)
web_entry.focus()
username_entry = tk.Entry(font=Label_Fonts, width=40)
username_entry.grid(column=1, row=2, columnspan=2)
username_entry.insert(0, "hasanforaty@gmail.com")
password_entry = tk.Entry(font=Label_Fonts, width=20)
password_entry.grid(column=1, row=3)

# Buttons
generate_button = tk.Button(windows, text="Generate Password", font=Label_Fonts, command=generate_password_button)
generate_button.grid(column=2, row=3)
add_button = tk.Button(windows, text="Add Password", width=30, command=add_data)
add_button.grid(column=1, row=4, columnspan=2)

windows.mainloop()
