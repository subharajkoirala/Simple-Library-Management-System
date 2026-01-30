import tkinter as tk
from tkinter import messagebox, filedialog
import pandas as pd
from datetime import date

class LoanBookWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Loan Books")
        self.root.geometry("700x600")
        self.root.configure(bg="#ecf0f1")
        
        # Colors
        self.primary_color = "#2c3e50"
        self.secondary_color = "#3498db"
        self.accent_color = "#e74c3c"
        self.bg_color = "#ecf0f1"
        
        # Select file
        self.book_list = filedialog.askopenfilename(
            title="Select the file for list of book",
            filetypes=[("csv files", "*.csv")]
        )
        
        if not self.book_list:
            messagebox.showwarning("Warning", "No file selected!")
            self.root.destroy()
            return
        
        try:
            self.book_df = pd.read_csv(
                self.book_list,
                parse_dates=['issue_date', 'due_date', 'returned_date'],
                dtype={'book_id': str, 'student_id': str, 'borrower_name': str}
            )
        except Exception as e:
            messagebox.showerror("Error", f"Failed to read file: {e}")
            self.root.destroy()
            return
        
        self.current_book_id = None
        self.create_loan_form()
        
    def create_loan_form(self):
        # Header
        tk.Label(
            self.root,
            text="Loan Book to Student",
            font=("Helvetica", 18, "bold"),
            bg=self.bg_color,
            fg=self.primary_color
        ).pack(pady=20)
        
        # Search section
        search_frame = tk.Frame(self.root, bg=self.bg_color, relief="groove", bd=2)
        search_frame.pack(padx=20, pady=10, fill="x")
        
        tk.Label(
            search_frame,
            text="Search for Book",
            font=("Helvetica", 14, "bold"),
            bg=self.bg_color
        ).pack(pady=10)
        
        # Radio buttons
        radio_frame = tk.Frame(search_frame, bg=self.bg_color)
        radio_frame.pack(pady=5)
        
        self.search_type = tk.StringVar(value="name")
        tk.Radiobutton(
            radio_frame,
            text="By Book Name",
            variable=self.search_type,
            value="name",
            bg=self.bg_color,
            font=("Helvetica", 11)
        ).pack(side="left", padx=10)
        tk.Radiobutton(
            radio_frame,
            text="By Book ID",
            variable=self.search_type,
            value="id",
            bg=self.bg_color,
            font=("Helvetica", 11)
        ).pack(side="left", padx=10)
        
        # Search entry
        entry_frame = tk.Frame(search_frame, bg=self.bg_color)
        entry_frame.pack(pady=10)
        
        tk.Label(
            entry_frame,
            text="Enter:",
            font=("Helvetica", 12),
            bg=self.bg_color
        ).pack(side="left", padx=5)
        
        self.search_entry = tk.Entry(entry_frame, font=("Helvetica", 12), width=30)
        self.search_entry.pack(side="left", padx=5)
        
        tk.Button(
            entry_frame,
            text="Search",
            font=("Helvetica", 11, "bold"),
            bg=self.secondary_color,
            fg="white",
            command=self.search_book,
            padx=15,
            pady=5,
            cursor="hand2"
        ).pack(side="left", padx=5)
        
        # Result label
        self.result_label = tk.Label(
            search_frame,
            text="",
            font=("Helvetica", 11),
            bg=self.bg_color,
            wraplength=600
        )
        self.result_label.pack(pady=10)
        
        # Student info section
        student_frame = tk.Frame(self.root, bg=self.bg_color, relief="groove", bd=2)
        student_frame.pack(padx=20, pady=10, fill="x")
        
        tk.Label(
            student_frame,
            text="Student Information",
            font=("Helvetica", 14, "bold"),
            bg=self.bg_color
        ).pack(pady=10)
        
        form_frame = tk.Frame(student_frame, bg=self.bg_color)
        form_frame.pack(pady=10)
        
        # Student ID
        tk.Label(
            form_frame,
            text="Student ID:",
            font=("Helvetica", 12),
            bg=self.bg_color
        ).grid(row=0, column=0, sticky="e", padx=10, pady=10)
        self.student_id_entry = tk.Entry(form_frame, font=("Helvetica", 12), width=30)
        self.student_id_entry.grid(row=0, column=1, pady=10)
        
        # Student Name
        tk.Label(
            form_frame,
            text="Student Name:",
            font=("Helvetica", 12),
            bg=self.bg_color
        ).grid(row=1, column=0, sticky="e", padx=10, pady=10)
        self.student_name_entry = tk.Entry(form_frame, font=("Helvetica", 12), width=30)
        self.student_name_entry.grid(row=1, column=1, pady=10)
        
        # Buttons
        button_frame = tk.Frame(self.root, bg=self.bg_color)
        button_frame.pack(pady=20)
        
        tk.Button(
            button_frame,
            text="Loan Book",
            font=("Helvetica", 12, "bold"),
            bg="#27ae60",
            fg="white",
            command=self.loan_book,
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
    
    def search_book(self):
        search_value = self.search_entry.get().strip()
        
        if not search_value:
            messagebox.showwarning("Warning", "Please enter a book name or ID!")
            return
        
        # Search based on type
        if self.search_type.get() == "name":
            if search_value.lower() not in self.book_df["book_name"].str.lower().values:
                self.result_label.config(
                    text="❌ Book not found!",
                    fg=self.accent_color
                )
                return
            
            matches = self.book_df[self.book_df["book_name"].str.lower() == search_value.lower()]
        else:
            if search_value not in self.book_df["book_id"].values:
                self.result_label.config(
                    text="❌ Book ID not found!",
                    fg=self.accent_color
                )
                return
            
            matches = self.book_df[self.book_df["book_id"] == search_value]
        
        # Check if book is borrowed
        borrowed_books = matches[matches["borrower_name"].notna()]
        
        if not borrowed_books.empty:
            book = borrowed_books.iloc[0]
            self.result_label.config(
                text=f"⚠️ Book is already borrowed by {book['borrower_name']} until {book['due_date']}",
                fg=self.accent_color
            )
            self.current_book_id = None
        else:
            book = matches.iloc[0]
            self.current_book_id = book["book_id"]
            self.result_label.config(
                text=f"✅ Book '{book['book_name']}' by {book['author']} is available!",
                fg="green"
            )
    
    def loan_book(self):
        if self.current_book_id is None:
            messagebox.showwarning("Warning", "Please search for an available book first!")
            return
        
        student_id = self.student_id_entry.get().strip()
        student_name = self.student_name_entry.get().strip()
        
        if not all([student_id, student_name]):
            messagebox.showwarning("Warning", "Please fill in student details!")
            return
        
        # Update book record
        issue_date = pd.to_datetime(date.today())
        due_date = issue_date + pd.Timedelta(days=15)
        
        self.book_df.loc[
            self.book_df["book_id"] == self.current_book_id,
            ["student_id", "borrower_name", "issue_date", "due_date"]
        ] = [student_id, student_name, issue_date, due_date]
        
        self.book_df.to_csv(self.book_list, index=False)
        
        messagebox.showinfo(
            "Success",
            f"Book loaned to {student_name}\nDue date: {due_date.date()}"
        )
        
        # Clear form
        self.search_entry.delete(0, tk.END)
        self.student_id_entry.delete(0, tk.END)
        self.student_name_entry.delete(0, tk.END)
        self.result_label.config(text="")
        self.current_book_id = None
        
    def run(self):
        self.root.mainloop()


def lending_book():
    """Function to be called by Main_LMS.py"""
    window = LoanBookWindow()
    window.run()


if __name__ == "__main__":
    lending_book()
