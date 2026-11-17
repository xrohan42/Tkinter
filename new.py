
import tkinter as tk
from tkinter import messagebox


#LOGIN

def login():
    username = username_entry.get()
    password = password_entry.get()''

    if username == "admin" and password == "1234":
        login_window.destroy()
        open_cipherx()
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")


def open_cipherx():
    root = tk.Tk()
    root.title("CipherX - Caesar Cipher")
    root.geometry("500x580")
    root.configure(bg="#f3f4f6")
    root.resizable(False, False)

    def encrypt_decrypt(decrypt=False):
        text = input_text.get("1.0", "end-1c")

        if not text.strip():
            messagebox.showwarning("Warning", "Please enter some text")
            return

        try:
            key = int(key_entry.get())

            if key < 1 or key > 25:
                raise ValueError
        except ValueError:
            messagebox.showerror(
                "Invalid Key", "Enter a number between 1 and 25"
            )
            return

        if decrypt:
            key = -key

        result = ""

        for char in text:
            if char.isascii() and char.isalpha():
                base = ord("A") if char.isupper() else ord("a")
                result += chr((ord(char) - base + key) % 26 + base)
            else:
                result += char

        output_text.config(state="normal")
        output_text.delete("1.0", "end")
        output_text.insert("1.0", result)
        output_text.config(state="disabled")

    def copy_result():
        result = output_text.get("1.0", "end-1c")

        if not result:
            messagebox.showwarning("Warning", "No result to copy")
            return

        root.clipboard_clear()
        root.clipboard_append(result)
        messagebox.showinfo("Copied", "Result copied successfully!")

    def clear_all():
        input_text.delete("1.0", "end")
        output_text.config(state="normal")
        output_text.delete("1.0", "end")
        output_text.config(state="disabled")
        key_entry.delete(0, "end")
        key_entry.insert(0, "3")

    # Title
    tk.Label(
        root, text="CipherX", font=("Arial", 24, "bold"),
        bg="#f3f4f6", fg="#111111"
    ).pack(pady=(20, 5))

    tk.Label(
        root, text="Caesar Cipher Encryption Tool",
        font=("Arial", 11), bg="#f3f4f6", fg="#555555"
    ).pack(pady=(0, 20))

    # Input
    tk.Label(
        root, text="Enter your text", font=("Arial", 11, "bold"),
        bg="#f3f4f6", fg="#222222"
    ).pack(anchor="w", padx=35)

    input_text = tk.Text(
        root, height=5, width=48, font=("Arial", 11),
        bg="white", fg="#111111", relief="solid", bd=1
    )
    input_text.pack(padx=30, pady=8)

    # Key
    tk.Label(
        root, text="Encryption Key (1-25)",
        font=("Arial", 11, "bold"), bg="#f3f4f6", fg="#222222"
    ).pack(anchor="w", padx=35, pady=(8, 3))

    key_entry = tk.Entry(
        root, font=("Arial", 11), width=10,
        bg="white", fg="#111111", relief="solid", bd=1
    )
    key_entry.pack(anchor="w", padx=35)
    key_entry.insert(0, "3")

    # Buttons
    button_frame = tk.Frame(root, bg="#f3f4f6")
    button_frame.pack(pady=18)

    tk.Button(
        button_frame, text="Encrypt", width=12,
        bg="#222222", fg="white", command=lambda: encrypt_decrypt(False)
    ).grid(row=0, column=0, padx=5)

    tk.Button(
        button_frame, text="Decrypt", width=12,
        bg="#555555", fg="white", command=lambda: encrypt_decrypt(True)
    ).grid(row=0, column=1, padx=5)

    # Output
    tk.Label(
        root, text="Result", font=("Arial", 11, "bold"),
        bg="#f3f4f6", fg="#222222"
    ).pack(anchor="w", padx=35)

    output_text = tk.Text(
        root, height=5, width=48, font=("Arial", 11),
        bg="#e5e7eb", fg="#111111", relief="solid", bd=1
    )
    output_text.pack(padx=30, pady=8)
    output_text.config(state="disabled")

    # Copy and Clear
    bottom_frame = tk.Frame(root, bg="#f3f4f6")
    bottom_frame.pack(pady=10)

    tk.Button(
        bottom_frame, text="Copy Result", width=12,
        bg="#444444", fg="white", command=copy_result
    ).grid(row=0, column=0, padx=5)

    tk.Button(
        bottom_frame, text="Clear All", width=12,
        bg="#d1d5db", fg="#111111", command=clear_all
    ).grid(row=0, column=1, padx=5)

    root.mainloop()


login_window = tk.Tk()
login_window.title("CipherX - Login")
login_window.geometry("350x300")
login_window.configure(bg="#f3f4f6")
login_window.resizable(False, False)

tk.Label(
    login_window, text="CipherX",
    font=("Arial", 25, "bold"), bg="#f3f4f6", fg="#111111"
).pack(pady=(25, 5))

tk.Label(
    login_window, text="Please log in to continue",
    font=("Arial", 10), bg="#f3f4f6", fg="#555555"
).pack(pady=(0, 20))

tk.Label(
    login_window, text="Username",
    bg="#f3f4f6", fg="#222222"
).pack()

username_entry = tk.Entry(
    login_window, font=("Arial", 11), width=25
)
username_entry.pack(pady=5)
username_entry.insert(0, "")

tk.Label(
    login_window, text="Password",
    bg="#f3f4f6", fg="#222222"
).pack()

password_entry = tk.Entry(
    login_window, font=("Arial", 11), width=25, show="*"
)
password_entry.pack(pady=5)

tk.Button(
    login_window, text="Login", width=15,
    bg="#222222", fg="white", command=login
).pack(pady=15)

login_window.bind("<Return>", lambda event: login())
username_entry.focus()

login_window.mainloop()
