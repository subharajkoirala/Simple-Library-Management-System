import tkinter as tk
from tkinter import messagebox, filedialog
import pandas as pd

class AddBooksWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Add Books")
        self.root.geometry("600x500")
        self.root.configure(bg="#ecf0f1")
        
        # Colors
        self.primary_color = "#2c3e50"
        self.secondary_color = "#3498db"
        self.accent_color = "#e74c3c"
        self.bg_color = "#ecf0f1"
        
        # Select file
        self.book_list = filedialog.askopenfilename(
            title="Select the book list CSV file",
            filetypes=[("CSV files", "*.csv")]
        )
        
        if not self.book_list:
            messagebox.showwarning("Warning", "No file selected!")
            self.root.destroy()
            return
        
        try:
            self.book_df = pd.read_csv(self.book_list, dtype={'book_id': str, 'student_id': str})
        except Exception as e:
            messagebox.showerror("Error", f"Failed to read file: {e}")
            self.root.destroy()
            return
        
        self.create_add_form()
        
    def create_add_form(self):
        # Header
        tk.Label(
            self.root,
            text="Add New Book",
            font=("Helvetica", 18, "bold"),
            bg=self.bg_color,
            fg=self.primary_color
        ).pack(pady=20)
        
        # Form frame
        form_frame = tk.Frame(self.root, bg=self.bg_color)
        form_frame.pack(pady=20)
        
        # Book ID
        tk.Label(
            form_frame, 
            text="Book ID:", 
            font=("Helvetica", 12), 
            bg=self.bg_color
        ).grid(row=0, column=0, sticky="e", padx=10, pady=10)
        self.book_id_entry = tk.Entry(form_frame, font=("Helvetica", 12), width=30)
        self.book_id_entry.grid(row=0, column=1, pady=10)
        
        # Book Name
        tk.Label(
            form_frame, 
            text="Book Name:", 
            font=("Helvetica", 12), 
            bg=self.bg_color
        ).grid(row=1, column=0, sticky="e", padx=10, pady=10)
        self.book_name_entry = tk.Entry(form_frame, font=("Helvetica", 12), width=30)
        self.book_name_entry.grid(row=1, column=1, pady=10)
        
        # Author
        tk.Label(
            form_frame, 
            text="Author:", 
            font=("Helvetica", 12), 
            bg=self.bg_color
        ).grid(row=2, column=0, sticky="e", padx=10, pady=10)
        self.author_entry = tk.Entry(form_frame, font=("Helvetica", 12), width=30)
        self.author_entry.grid(row=2, column=1, pady=10)
        
        # Status label
        self.status_label = tk.Label(
            self.root,
            text="",
            font=("Helvetica", 10),
            bg=self.bg_color,
            wraplength=500
        )
        self.status_label.pack(pady=10)
        
        # Buttons
        button_frame = tk.Frame(self.root, bg=self.bg_color)
        button_frame.pack(pady=20)
        
        tk.Button(
            button_frame,
            text="Add Book",
            font=("Helvetica", 12, "bold"),
            bg=self.secondary_color,
            fg="white",
            command=self.save_book,
            padx=20,
            pady=8,
            cursor="hand2"
        ).pack(side="left", padx=5)
        
        tk.Button(
            button_frame,
            text="Add Another",
            font=("Helvetica", 12),
            bg="#27ae60",
            fg="white",
            command=self.clear_form,
            padx=20,
            pady=8,
            cursor="hand2"
        ).pack(side="left", padx=5)
        
        tk.Button(
            button_frame,
            text="Close",
            font=("Helvetica", 12),
            bg=self.accent_color,
            fg="white",
            command=self.root.destroy,
            padx=20,
            pady=8,
            cursor="hand2"
        ).pack(side="left", padx=5)
    
    def save_book(self):
        book_id = self.book_id_entry.get().strip()
        book_name = self.book_name_entry.get().strip()
        author = self.author_entry.get().strip()
        
        # Validation
        if not all([book_id, book_name, author]):
            messagebox.showwarning("Warning", "Please fill all fields!")
            return
        
        # Check for duplicate
        if book_id in self.book_df["book_id"].values:
            messagebox.showerror("Error", "This Book ID already exists!")
            return
        
        # Add new book
        new_book = {
            "book_id": book_id,
            "book_name": book_name,
            "author": author,
            "student_id": None,
            "borrower_name": None,
            "issue_date": None,
            "due_date": None,
            "returned_date": None
        }
        
        self.book_df.loc[len(self.book_df)] = new_book
        self.book_df.to_csv(self.book_list, index=False)
        
        self.status_label.config(
            text=f"✅ Book '{book_name}' added successfully!",
            fg="green"
        )
        
        messagebox.showinfo("Success", f"Book '{book_name}' added successfully!")
        self.clear_form()
    
    def clear_form(self):
        self.book_id_entry.delete(0, tk.END)
        self.book_name_entry.delete(0, tk.END)
        self.author_entry.delete(0, tk.END)
        self.book_id_entry.focus()
        
    def run(self):
        self.root.mainloop()


def add_books():
    """Function to be called by Main_LMS.py"""
    window = AddBooksWindow()
    window.run()


if __name__ == "__main__":
    add_books()
