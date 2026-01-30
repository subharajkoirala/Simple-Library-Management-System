import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import pandas as pd

class ListBooksWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("List Books")
        self.root.geometry("1000x600")
        self.root.configure(bg="#ecf0f1")
        
        # Colors
        self.primary_color = "#2c3e50"
        self.bg_color = "#ecf0f1"
        
        self.show_books()
        
    def show_books(self):
        # Select file
        book_list = filedialog.askopenfilename(
            title="Select the file for list of book", 
            filetypes=[("csv files", "*.csv")]
        )
        
        if not book_list:
            messagebox.showwarning("Warning", "No file selected!")
            self.root.destroy()
            return
        
        try:
            book_df = pd.read_csv(book_list, dtype={"book_id": str, "student_id": str})
        except Exception as e:
            messagebox.showerror("Error", f"Failed to read file: {e}")
            self.root.destroy()
            return
        
        # Header
        tk.Label(
            self.root,
            text="Library Books",
            font=("Helvetica", 18, "bold"),
            bg=self.bg_color,
            fg=self.primary_color
        ).pack(pady=20)
        
        # Create Treeview
        frame = tk.Frame(self.root)
        frame.pack(fill="both", expand=True, padx=20, pady=10)
        
        # Scrollbars
        y_scroll = tk.Scrollbar(frame)
        y_scroll.pack(side="right", fill="y")
        
        x_scroll = tk.Scrollbar(frame, orient="horizontal")
        x_scroll.pack(side="bottom", fill="x")
        
        columns = list(book_df.columns)
        tree = ttk.Treeview(
            frame,
            columns=columns,
            show="headings",
            yscrollcommand=y_scroll.set,
            xscrollcommand=x_scroll.set
        )
        
        y_scroll.config(command=tree.yview)
        x_scroll.config(command=tree.xview)
        
        # Configure columns
        for col in columns:
            tree.heading(col, text=col.replace("_", " ").title())
            tree.column(col, width=120)
        
        # Insert data with color coding
        for _, row in book_df.iterrows():
            values = list(row)
            # Add tags for borrowed books
            if pd.notna(row.get("borrower_name")):
                tree.insert("", "end", values=values, tags=("borrowed",))
            else:
                tree.insert("", "end", values=values, tags=("available",))
        
        # Configure tags
        tree.tag_configure("borrowed", background="#ffe6e6")  # Light red
        tree.tag_configure("available", background="#e6ffe6")  # Light green
        
        tree.pack(fill="both", expand=True)
        
        # Legend
        legend_frame = tk.Frame(self.root, bg=self.bg_color)
        legend_frame.pack(pady=10)
        
        tk.Label(
            legend_frame,
            text="● Available",
            bg="#e6ffe6",
            font=("Helvetica", 10),
            padx=10,
            pady=5
        ).pack(side="left", padx=5)
        
        tk.Label(
            legend_frame,
            text="● Borrowed",
            bg="#ffe6e6",
            font=("Helvetica", 10),
            padx=10,
            pady=5
        ).pack(side="left", padx=5)
        
        # Close button
        tk.Button(
            self.root,
            text="Close",
            font=("Helvetica", 12),
            bg="#e74c3c",
            fg="white",
            command=self.root.destroy,
            padx=20,
            pady=5,
            cursor="hand2"
        ).pack(pady=10)
        
    def run(self):
        self.root.mainloop()


def list_books():
    """Function to be called by Main_LMS.py"""
    window = ListBooksWindow()
    window.run()


if __name__ == "__main__":
    list_books()
