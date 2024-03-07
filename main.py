import tkinter as tk
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

windows = tk.Tk()
windows.title("Password Manager")
windows.config(padx=20, pady=20)

canvas = tk.Canvas(windows, width=200, height=200)
logo_img = tk.PhotoImage(file="assets/logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=0, row=0)


windows.mainloop()
