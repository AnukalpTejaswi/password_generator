# •	Password Generator – User chooses length and options (letters, numbers, symbols), program outputs random password.
# •	Password Generator – User chooses length and options (letters, numbers, symbols), program outputs random password.
import random
import string
import tkinter as tk
from tkinter import messagebox

def password_generator(length, user_letter, user_digit, user_symbols):
    letters = string.ascii_letters
    digits = string.digits
    symbols = "!@#$%&*"
    password = []

    temp = ""
    if user_letter:
        temp += letters
    if user_digit:
        temp += digits
    if user_symbols:
        temp += symbols

    if not temp:
        return ""

    for i in range(length):
        var = random.choice(temp)
        password.append(var)

    return "".join(password)


def generate_password():
    username = name_entry.get()
    
    try:
        length = int(length_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number for password length.")
        return

    user_letter = letters_var.get()
    user_digit = digits_var.get()
    user_symbols = symbols_var.get()

    password = password_generator(length, user_letter, user_digit, user_symbols)

    if not password:
        messagebox.showerror("Error", "Please select at least one option.")
        return

    result_label.config(
        text=f"{username}, your random password is:\n{password}"
    )


# ---------- GUI SETUP ----------
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x350")

# Username
tk.Label(root, text="Enter your name:").pack(pady=5)
name_entry = tk.Entry(root)
name_entry.pack()

# Password length
tk.Label(root, text="Password length:").pack(pady=5)
length_entry = tk.Entry(root)
length_entry.pack()

# Options
letters_var = tk.BooleanVar()
digits_var = tk.BooleanVar()
symbols_var = tk.BooleanVar()

tk.Checkbutton(root, text="Include Letters", variable=letters_var).pack()
tk.Checkbutton(root, text="Include Digits", variable=digits_var).pack()
tk.Checkbutton(root, text="Include Symbols", variable=symbols_var).pack()

# Generate button
tk.Button(root, text="Generate Password", command=generate_password).pack(pady=15)

# Result
result_label = tk.Label(root, text="", wraplength=350, fg="blue")
result_label.pack(pady=10)

root.mainloop()
