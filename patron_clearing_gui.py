import tkinter as tk
from tkinter import messagebox
import pandas as pd

class PatronClearingWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Clear Patron / Return Book")
        self.root.geometry("700x500")
        self.root.configure(bg="#ecf0f1")
        
        # Colors
        self.primary_color = "#2c3e50"
        self.secondary_color = "#3498db"
        self.accent_color = "#e74c3c"
        self.bg_color = "#ecf0f1"
        
        # Load file
        self.book_file = "Book_list.csv"
        
        try:
            self.book_df = pd.read_csv(
                self.book_file,
                dtype={'book_id': str, 'student_id': str}
            )
        except Exception as e:
            messagebox.showerror("Error", f"Failed to read file: {e}")
            self.root.destroy()
            return
        
        self.current_book_id = None
        self.create_clearing_form()
        
    def create_clearing_form(self):
        # Header
        tk.Label(
            self.root,
            text="Return Book / Clear Patron",
            font=("Helvetica", 18, "bold"),
            bg=self.bg_color,
            fg=self.primary_color
        ).pack(pady=20)
        
        # Search section
        search_frame = tk.Frame(self.root, bg=self.bg_color, relief="groove", bd=2)
        search_frame.pack(padx=20, pady=10, fill="x")
        
        tk.Label(
            search_frame,
            text="Search Borrowed Book",
            font=("Helvetica", 14, "bold"),
            bg=self.bg_color
        ).pack(pady=10)
        
        # Radio buttons
        radio_frame = tk.Frame(search_frame, bg=self.bg_color)
        radio_frame.pack(pady=5)
        
        self.search_type = tk.StringVar(value="name")
        tk.Radiobutton(
            radio_frame,
            text="By Borrower Name",
            variable=self.search_type,
            value="name",
            bg=self.bg_color,
            font=("Helvetica", 11)
        ).pack(side="left", padx=10)
        tk.Radiobutton(
            radio_frame,
            text="By Student ID",
            variable=self.search_type,
            value="id",
            bg=self.bg_color,
            font=("Helvetica", 11)
        ).pack(side="left", padx=10)
        tk.Radiobutton(
            radio_frame,
            text="By Book ID",
            variable=self.search_type,
            value="book_id",
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
            command=self.search_borrowed_book,
            padx=15,
            pady=5,
            cursor="hand2"
        ).pack(side="left", padx=5)
        
        # Result section
        result_frame = tk.Frame(self.root, bg=self.bg_color, relief="groove", bd=2)
        result_frame.pack(padx=20, pady=10, fill="both", expand=True)
        
        tk.Label(
            result_frame,
            text="Book Details",
            font=("Helvetica", 14, "bold"),
            bg=self.bg_color
        ).pack(pady=10)
        
        self.info_label = tk.Label(
            result_frame,
            text="Search for a borrowed book to see details...",
            font=("Helvetica", 11),
            bg=self.bg_color,
            justify="left",
            wraplength=600
        )
        self.info_label.pack(pady=20, padx=20)
        
        # Buttons
        button_frame = tk.Frame(self.root, bg=self.bg_color)
        button_frame.pack(pady=20)
        
        self.return_btn = tk.Button(
            button_frame,
            text="Return Book",
            font=("Helvetica", 12, "bold"),
            bg="#27ae60",
            fg="white",
            command=self.return_book,
            padx=20,
            pady=8,
            cursor="hand2",
            state="disabled"
        )
        self.return_btn.pack(side="left", padx=5)
        
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
    
    def search_borrowed_book(self):
        search_value = self.search_entry.get().strip()
        
        if not search_value:
            messagebox.showwarning("Warning", "Please enter a search value!")
            return
        
        # Map search type to column
        column_map = {
            "name": "borrower_name",
            "id": "student_id",
            "book_id": "book_id"
        }
        column = column_map[self.search_type.get()]
        
        # Find matching borrowed books
        matches = self.book_df[
            (self.book_df[column].str.lower() == search_value.lower()) & 
            (self.book_df["borrower_name"].notna())
        ]
        
        if matches.empty:
            self.info_label.config(
                text="❌ No borrowed book found with this information.",
                fg=self.accent_color
            )
            self.return_btn.config(state="disabled")
            return
        
        if len(matches) > 1:
            # Multiple books found
            books_info = "Multiple books found:\n\n"
            for _, book in matches.iterrows():
                books_info += f"• {book['book_name']} (ID: {book['book_id']})\n"
            books_info += "\nPlease search by Book ID for specific book."
            self.info_label.config(text=books_info, fg=self.accent_color)
            self.return_btn.config(state="disabled")
            return
        
        # Single book found
        book = matches.iloc[0]
        self.current_book_id = book["book_id"]
        
        # Calculate fine if overdue
        returned_date = pd.Timestamp.now().normalize()
        due_date = pd.to_datetime(book["due_date"])
        
        info_text = f"📚 Book: {book['book_name']}\n"
        info_text += f"👤 Borrowed by: {book['borrower_name']}\n"
        info_text += f"🆔 Student ID: {book['student_id']}\n"
        info_text += f"📅 Issue Date: {book['issue_date']}\n"
        info_text += f"📅 Due Date: {due_date.date()}\n\n"
        
        if due_date < returned_date:
            delay = (returned_date - due_date).days
            fine = delay * 20
            info_text += f"⚠️ OVERDUE by {delay} days\n"
            info_text += f"💰 Fine: Rs. {fine}"
            self.info_label.config(text=info_text, fg=self.accent_color)
        else:
            info_text += "✅ Returned on time!"
            self.info_label.config(text=info_text, fg="green")
        
        self.return_btn.config(state="normal")
    
    def return_book(self):
        if self.current_book_id is None:
            messagebox.showwarning("Warning", "Please search for a book first!")
            return
        
        # Get book details for confirmation
        book = self.book_df[self.book_df["book_id"] == self.current_book_id].iloc[0]
        
        # Calculate fine
        returned_date = pd.Timestamp.now().normalize()
        due_date = pd.to_datetime(book["due_date"])
        
        confirm_msg = f"Confirm return of:\n\n"
        confirm_msg += f"Book: {book['book_name']}\n"
        confirm_msg += f"Borrower: {book['borrower_name']}\n"
        
        if due_date < returned_date:
            delay = (returned_date - due_date).days
            fine = delay * 20
            confirm_msg += f"\nFine: Rs. {fine}\n"
        
        if not messagebox.askyesno("Confirm Return", confirm_msg):
            return
        
        # Clear patron data
        self.book_df.loc[
            self.book_df["book_id"] == self.current_book_id,
            ["student_id", "borrower_name", "issue_date", "due_date"]
        ] = [None, None, None, None]
        
        self.book_df.to_csv(self.book_file, index=False)
        
        messagebox.showinfo("Success", "Book returned successfully!")
        
        # Clear form
        self.search_entry.delete(0, tk.END)
        self.info_label.config(
            text="Search for a borrowed book to see details...",
            fg=self.primary_color
        )
        self.current_book_id = None
        self.return_btn.config(state="disabled")
        
    def run(self):
        self.root.mainloop()


def patron_clearing():
    """Function to be called by Main_LMS.py"""
    window = PatronClearingWindow()
    window.run()


if __name__ == "__main__":
    patron_clearing()
