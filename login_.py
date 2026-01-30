import tkinter as tk
from tkinter import messagebox

class LoginWindow:
    def __init__(self):
        self.login_successful = False
        self.root = tk.Tk()
        self.root.title("Library Login")
        self.root.geometry("500x400")
        self.root.configure(bg="#56ceec")
        
        # Colors
        self.primary_color = "#2c3e50"
        self.secondary_color = "#3498db"
        self.bg_color = "#ecf0f1"
        
        self.create_login_screen()
        
    def create_login_screen(self):
        # Login frame
        login_frame = tk.Frame(self.root, bg=self.bg_color, padx=40, pady=40)
        login_frame.place(relx=0.5, rely=0.5, anchor="center")
        
        # Title
        title_label = tk.Label(
            login_frame, 
            text="Library Management System",
            font=("Helvetica", 24, "bold"),
            bg=self.bg_color,
            fg=self.primary_color
        )
        title_label.grid(row=0, column=0, columnspan=2, pady=(0, 30))
        
        # Username
        tk.Label(
            login_frame,
            text="Username:",
            font=("Helvetica", 12),
            bg=self.bg_color,
            fg=self.primary_color
        ).grid(row=1, column=0, sticky="e", padx=10, pady=10)
        
        self.username_entry = tk.Entry(login_frame, font=("Helvetica", 12), width=20)
        self.username_entry.grid(row=1, column=1, pady=10)
        
        # Password
        tk.Label(
            login_frame,
            text="Password:",
            font=("Helvetica", 12),
            bg=self.bg_color,
            fg=self.primary_color
        ).grid(row=2, column=0, sticky="e", padx=10, pady=10)
        
        self.password_entry = tk.Entry(login_frame, font=("Helvetica", 12), width=20, show="*")
        self.password_entry.grid(row=2, column=1, pady=10)
        
        # Login button
        login_btn = tk.Button(
            login_frame,
            text="Login",
            font=("Helvetica", 12, "bold"),
            bg=self.secondary_color,
            fg="white",
            padx=30,
            pady=10,
            cursor="hand2",
            command=self.verify_login
        )
        login_btn.grid(row=3, column=0, columnspan=2, pady=20)
        
        # Bind Enter key
        self.password_entry.bind("<Return>", lambda e: self.verify_login())
        
    def verify_login(self):
        username = self.username_entry.get().strip()
        password = self.password_entry.get().strip()
        
        if username == "Librarian" and password == "2520":
            self.login_successful = True
            self.root.destroy()
        else:
            messagebox.showerror("Error", "Invalid username or password!")
            
    def run(self):
        self.root.mainloop()
        return self.login_successful


def login():
    """Function to be called by Main_LMS.py"""
    login_window = LoginWindow()
    return login_window.run()


if __name__ == "__main__":
    result = login()
    print(f"Login result: {result}")
