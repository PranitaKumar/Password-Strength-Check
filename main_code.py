import tkinter as tk
from tkinter import ttk
import re

class PasswordStrengthChecker(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Password Strength Checker")
        self.geometry("600x400")
        self.configure(bg="#f0f4f8")  # Soft pastel background
        self.create_widgets()

    def create_widgets(self):
        # Title
        tk.Label(self, text="Password Strength Checker", font=("Verdana", 24, "bold"), bg="#f0f4f8", fg="#2c3e50").pack(pady=20)
        
        # Password entry
        tk.Label(self, text="Enter your password:", font=("Verdana", 14), bg="#f0f4f8").pack(pady=5)
        self.password_entry = tk.Entry(self, font=("Verdana", 14), show="*", width=30)
        self.password_entry.pack(pady=10)
        self.password_entry.bind("<KeyRelease>", self.check_strength)
        
        # Progress bar for strength
        self.strength_var = tk.IntVar()
        self.progress_bar = ttk.Progressbar(self, length=400, maximum=100, variable=self.strength_var)
        self.progress_bar.pack(pady=10)
        
        # Strength feedback
        self.strength_label = tk.Label(self, text="", font=("Verdana", 14), bg="#f0f4f8")
        self.strength_label.pack(pady=10)

    def check_strength(self, event=None):
        password = self.password_entry.get()
        strength_score = self.calculate_strength(password)
        self.strength_var.set(strength_score)
        
        if strength_score < 30:
            self.strength_label.config(text="Weak Password", fg="red")
        elif 30 <= strength_score < 70:
            self.strength_label.config(text="Moderate Password", fg="orange")
        else:
            self.strength_label.config(text="Strong Password", fg="green")

    def calculate_strength(self, password):
        score = 0
        if len(password) >= 8:
            score += 20
        if re.search(r"[A-Z]", password):
            score += 20
        if re.search(r"[0-9]", password):
            score += 20
        if re.search(r"[!@#$%^&*(),.?":{}|<>]", password):
            score += 20
        if len(password) >= 12:
            score += 20
        return score

if __name__ == "__main__":
    app = PasswordStrengthChecker()
    app.mainloop()
