# 📚 Library Management System

A modern, GUI-based Library Management System built with Python and Tkinter. Manage your library's books, track loans, calculate fines, and maintain patron records with an intuitive graphical interface.

![Python Version](https://img.shields.io/badge/python-3.7+-blue.svg)
![Status](https://img.shields.io/badge/status-active-success.svg)

## ✨ Features

### 🔐 Secure Login System
- Password-protected access
- Clean, professional login interface

### 📖 Book Management
- **Add New Books**: Easily add books with ID, name, and author
- **List All Books**: View all books in an organized table format
- **Color-Coded Status**: 
  - 🟢 Green = Available
  - 🔴 Red = Currently borrowed

### 👥 Patron Management
- **Loan Books**: Issue books to students with automatic due date calculation
- **Track Borrowers**: See who has which books and when they're due
- **Return Books**: Process returns with automatic fine calculation

### 💰 Automatic Fine Calculation
- 15-day loan period
- Rs. 20 per day for overdue books
- Automatic calculation on return

## 🖥️ Screenshots

### Login Screen
```
┌─────────────────────────────────┐
│                                 │
│  Library Management System      │
│                                 │
│  Username: [____________]       │
│  Password: [____________]       │
│                                 │
│         [   Login   ]           │
│                                 │
└─────────────────────────────────┘
```

### Main Dashboard
```
┌─────────────────────────────────┐
│  Library Management System      │
├─────────────────────────────────┤
│                                 │
│    📚 List All Books            │
│    ➕ Add Books                 │
│    📖 Loan Books                │
│    ✅ Clear Patron              │
│    🚪 Exit                      │
│                                 │
└─────────────────────────────────┘
```

## 🚀 Getting Started

### Prerequisites

- Python 3.7 or higher
- Required libraries:
  ```bash
  pip install pandas
  ```
- Tkinter (usually comes with Python)

### Installation

1. **Clone or download the project**
   ```bash
   git clone https://github.com/yourusername/library-management-system.git
   cd library-management-system
   ```

2. **Install dependencies**
   ```bash
   pip install pandas
   ```

3. **Ensure you have the required files**
   ```
   Library_Management/
   ├── Main_LMS_.py
   ├── login_.py
   ├── menu_.py
   ├── add_books_.py
   ├── list_books_.py
   ├── loan_book_.py
   ├── patron_clearing_.py
   └── Book_list.csv
   ```

4. **Run the application**
   ```bash
   python Main_LMS_GUI.py
   ```

### First Time Setup

1. Make sure `Book_list.csv` exists in your project folder
2. The CSV should have these columns:
   ```
   book_id,book_name,author,student_id,borrower_name,issue_date,due_date,returned_date
   ```

## 📖 Usage Guide

### Login
- **Username**: `Librarian`
- **Password**: `2520`

### Adding Books
1. Click **➕ Add Books** from the main menu
2. Select your `Book_list.csv` file
3. Fill in:
   - Book ID (unique identifier)
   - Book Name
   - Author Name
4. Click **Add Book**
5. Click **Add Another** to add more books, or **Close** to finish

### Listing Books
1. Click **📚 List All Books**
2. Select your `Book_list.csv` file
3. View all books in a sortable table
4. Available books shown in green, borrowed books in red

### Loaning Books
1. Click **📖 Loan Books**
2. Select your `Book_list.csv` file
3. Search for book by name or ID
4. If available, enter student details:
   - Student ID
   - Student Name
5. Click **Loan Book**
6. Book is automatically set to return in 15 days

### Returning Books
1. Click **✅ Clear Patron**
2. Search by:
   - Borrower name
   - Student ID
   - Book ID
3. View book details and any fines
4. Click **Return Book** to confirm
5. Fines calculated automatically if overdue

## 🎨 Customization

### Changing Colors

Edit the color variables in any GUI file:

```python
# In any *_gui.py file
self.primary_color = "#2c3e50"      # Dark headers
self.secondary_color = "#3498db"    # Buttons
self.accent_color = "#e74c3c"       # Warning/Exit buttons
self.bg_color = "#ecf0f1"           # Background
```

### Popular Color Schemes

**Professional Blue** (Current):
```python
primary_color = "#2c3e50"
secondary_color = "#3498db"
accent_color = "#e74c3c"
```

**Modern Green**:
```python
primary_color = "#27ae60"
secondary_color = "#2ecc71"
accent_color = "#e67e22"
```

**Dark Theme**:
```python
primary_color = "#1a1a1a"
secondary_color = "#4a4a4a"
accent_color = "#ff6b6b"
```

### Changing Loan Period

In `loan_book_gui.py`, line ~230:
```python
due_date = issue_date + pd.Timedelta(days=15)  # Change 15 to your desired days
```

### Changing Fine Rate

In `patron_clearing_gui.py`, line ~150:
```python
fine = delay * 20  # Change 20 to your fine amount per day
```

## 📁 Project Structure

```
Library_Management_System/
│
├── Main_LMS_.py              # Main entry point
│
├── login_.py                 # Login module
│   └── LoginWindow class
│
├── menu_.py                  # Main menu module
│   └── MenuWindow class
│
├── add_books_.py             # Add books module
│   └── AddBooksWindow class
│
├── list_books_.py            # List books module
│   └── ListBooksWindow class
│
├── loan_book_.py             # Loan books module
│   └── LoanBookWindow class
│
├── patron_clearing_.py       # Return books module
│   └── PatronClearingWindow class
│
├── Book_list.csv                # Database file
│
├── README.md                    # This file
├── SETUP_GUIDE.md              # Detailed setup instructions
```

## 🔧 Technical Details

### Technologies Used
- **Python 3.7+**: Core programming language
- **Tkinter**: GUI framework
- **Pandas**: Data management and CSV operations
- **datetime**: Date and time handling

### Data Storage
- All data stored in `Book_list.csv`
- CSV format for easy backup and portability
- Real-time updates on all operations

### Key Classes
- `LoginWindow`: Handles user authentication
- `MenuWindow`: Main navigation dashboard
- `AddBooksWindow`: Book addition interface
- `ListBooksWindow`: Book viewing with table display
- `LoanBookWindow`: Book checkout system
- `PatronClearingWindow`: Book return and fine processing

## 🐛 Troubleshooting

### Common Issues

**Q: Program won't start**
```bash
# Check Python version
python --version

# Reinstall pandas
pip install --upgrade pandas
```

**Q: "No module named 'tkinter'"**
```bash
# On Ubuntu/Debian
sudo apt-get install python3-tk

# On macOS (should be included)
# On Windows, reinstall Python with "tcl/tk" option checked
```

**Q: CSV file not found**
- Ensure `Book_list.csv` is in the same folder as the Python files
- Check file name spelling (case-sensitive on Linux/Mac)

**Q: Window appears off-screen**
- Try Alt+Tab (Windows/Linux) or Cmd+Tab (Mac)
- Restart the program

**Q: Colors look different**
- This is normal across different operating systems
- Tkinter rendering varies slightly between OS



## 👨‍💻 Authors

- **Subharaj Koirala** - *Initial work and GUI development*

## 📞 Support

Having issues? Need help?

- 📧 Email: subharajkoirala@gmail.com
- 💬 Questions? Check the `SETUP_GUIDE.md` 


*Last Updated: January 2026*
