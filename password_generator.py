import random
import string
import tkinter as tk
from tkinter import ttk, messagebox


def init_window():
    # Initialize the main window
    root = tk.Tk()
    root.title("Password Generator")
    root.geometry("600x450")
    root.tk.call("source", "azure.tcl")
    root.tk.call("set_theme", "light")
    return root


def generate_password():
    try:
        password_chars = (
            random.choices(string.ascii_uppercase, k=upper_var.get()) +
            random.choices(string.ascii_lowercase, k=lower_var.get()) +
            random.choices(string.digits, k=digit_var.get()) +
            random.choices(string.punctuation, k=symbol_var.get())
        )
        random.shuffle(password_chars)
        password_var.set("".join(password_chars))
    except ValueError:
        password_var.set("Invalid input")


def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(password_var.get())
    root.update()
    messagebox.showinfo("Copied", "Password copied to clipboard")


def change_theme():
    current_theme = root.tk.call("ttk::style", "theme", "use")
    new_theme = "light" if current_theme == "azure-dark" else "dark"
    root.tk.call("set_theme", new_theme)


def create_scale(parent, label, var, row):
    # Function to create a labeled scale
    ttk.Label(parent, text=label).grid(row=row, column=0, sticky="w", padx=10, pady=5)
    ttk.Label(parent, textvariable=var, width=1).grid(row=row, column=1, sticky="e", padx=5)
    ttk.Scale(parent, style='Tick.TScale', from_=0, to=10, variable=var, orient="horizontal", length=200).grid(row=row, column=2, padx=10, pady=5)


root = init_window()

# Variables
upper_var, lower_var, digit_var, symbol_var = (tk.IntVar(value=0) for _ in range(4))
password_var = tk.StringVar()

# UI Components
frame = ttk.Frame(root, padding=30)
frame.pack(expand=True)

# Label Frame for UI grouping
ttk.LabelFrame(frame, text="Generate a Random Password", height=350).grid(
    row=0, column=0, padx=0, pady=0, sticky="nsew", rowspan=9, columnspan=12)

# Create scales
create_scale(frame, "Uppercase Letters:", upper_var, 2)
create_scale(frame, "Lowercase Letters:", lower_var, 3)
create_scale(frame, "Digits:", digit_var, 4)
create_scale(frame, "Symbols:", symbol_var, 5)

# Buttons
ttk.Button(frame, text="Generate", command=generate_password).grid(row=6, column=0, columnspan=3, pady=5)
ttk.Entry(frame, textvariable=password_var, state="readonly", width=40, font=("Arial", 14)).grid(row=7, column=0, columnspan=3, pady=0)
ttk.Button(frame, text="Copy", command=copy_to_clipboard).grid(row=8, column=0, columnspan=3, pady=5)

# Theme Switcher
switch = ttk.Checkbutton(frame, text="Switch mode", style='Switch.TCheckbutton', command=change_theme)
switch.grid(row=9, column=0, columnspan=3, pady=10)


root.mainloop()

