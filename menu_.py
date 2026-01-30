import tkinter as tk

class MenuWindow:
    def __init__(self):
        self.choice = None
        self.root = tk.Tk()
        self.root.title("Library Menu")
        self.root.geometry("600x500")
        self.root.configure(bg="#ecf0f1")
        
        # Colors
        self.primary_color = "#2c3e50"
        self.secondary_color = "#3498db"
        self.accent_color = "#e74c3c"
        self.bg_color = "#ecf0f1"
        
        self.create_menu()
        
    def create_menu(self):
        # Header
        header_frame = tk.Frame(self.root, bg=self.primary_color, height=80)
        header_frame.pack(fill="x")
        
        tk.Label(
            header_frame,
            text="Library Management System",
            font=("Helvetica", 20, "bold"),
            bg=self.primary_color,
            fg="white"
        ).pack(pady=20)
        
        # Main content area
        content_frame = tk.Frame(self.root, bg=self.bg_color)
        content_frame.pack(fill="both", expand=True, padx=50, pady=50)
        
        # Button styling
        button_config = {
            "font": ("Helvetica", 14),
            "bg": self.secondary_color,
            "fg": "white",
            "width": 25,
            "height": 2,
            "cursor": "hand2",
            "relief": "flat"
        }
        
        # Create buttons
        buttons = [
            ("📚 List All Books", "1"),
            ("➕ Add Books", "2"),
            ("📖 Loan Books", "3"),
            ("✅ Clear Patron", "4"),
            ("🚪 Exit", "5")
        ]
        
        for text, choice_value in buttons:
            btn = tk.Button(
                content_frame, 
                text=text, 
                command=lambda c=choice_value: self.select_choice(c),
                **button_config
            )
            btn.pack(pady=10)
            
            # Hover effect
            if choice_value == "5":
                btn.configure(bg=self.accent_color)
                btn.bind("<Enter>", lambda e, b=btn: b.configure(bg="#c0392b"))
                btn.bind("<Leave>", lambda e, b=btn: b.configure(bg=self.accent_color))
            else:
                btn.bind("<Enter>", lambda e, b=btn: b.configure(bg=self.primary_color))
                btn.bind("<Leave>", lambda e, b=btn: b.configure(bg=self.secondary_color))
    
    def select_choice(self, choice_value):
        self.choice = choice_value
        self.root.destroy()
        
    def run(self):
        self.root.mainloop()
        return self.choice


def main_menu():
    """Function to be called by Main_LMS.py"""
    menu_window = MenuWindow()
    return menu_window.run()


if __name__ == "__main__":
    choice = main_menu()
    print(f"Selected choice: {choice}")
