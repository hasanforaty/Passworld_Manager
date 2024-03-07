import tkinter as tk

Label_Fonts = ("Arial", 14)
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

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
web_entry = tk.Entry(font=Label_Fonts, width=35)
web_entry.grid(column=1, row=1, columnspan=2)
username_entry = tk.Entry(font=Label_Fonts, width=35)
username_entry.grid(column=1, row=2, columnspan=2)
password_entry = tk.Entry(font=Label_Fonts, width=21)
password_entry.grid(column=1, row=3)

# Buttons
generate_button = tk.Button(windows, text="Generate Password", font=Label_Fonts,)
generate_button.grid(column=2, row=3)
add_button = tk.Button(windows, text="Add Password", width=36)
add_button.grid(column=1, row=4, columnspan=2)

windows.mainloop()
