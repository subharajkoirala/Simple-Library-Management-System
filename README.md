# 📚 Library Management System

A modern, GUI-based Library Management System built with Python and Tkinter. Manage your library's books, track loans, calculate fines, and maintain patron records with an intuitive graphical interface.

![Python Version](https://img.shields.io/badge/python-3.7+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
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
   ├── Main_LMS_GUI.py
   ├── login_gui.py
   ├── menu_gui.py
   ├── add_books_gui.py
   ├── list_books_gui.py
   ├── loan_book_gui.py
   ├── patron_clearing_gui.py
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
├── Main_LMS_GUI.py              # Main entry point
│
├── login_gui.py                 # Login module
│   └── LoginWindow class
│
├── menu_gui.py                  # Main menu module
│   └── MenuWindow class
│
├── add_books_gui.py             # Add books module
│   └── AddBooksWindow class
│
├── list_books_gui.py            # List books module
│   └── ListBooksWindow class
│
├── loan_book_gui.py             # Loan books module
│   └── LoanBookWindow class
│
├── patron_clearing_gui.py       # Return books module
│   └── PatronClearingWindow class
│
├── Book_list.csv                # Database file
│
├── README.md                    # This file
├── SETUP_GUIDE.md              # Detailed setup instructions
└── GUI_Development_Guide.md    # GUI development tutorial
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

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Ideas for Contributions
- Add book search functionality
- Implement user roles (admin, librarian, student)
- Add book categories/genres
- Create reports (most borrowed books, overdue reports)
- Add database backend (SQLite)
- Email notifications for due dates
- Barcode scanning support

## 📝 License

This project is licensed under the MIT License - see below for details:

```
MIT License

Copyright (c) 2026 Library Management System

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## 👨‍💻 Authors

- **Your Name** - *Initial work and GUI development*

## 🙏 Acknowledgments

- Built with Python and Tkinter
- Pandas library for CSV operations
- Inspired by the need for simple, efficient library management

## 📞 Support

Having issues? Need help?

- 📧 Email: your.email@example.com
- 🐛 Report bugs in the [Issues](https://github.com/yourusername/library-management-system/issues) section
- 💬 Questions? Check the `SETUP_GUIDE.md` and `GUI_Development_Guide.md`

## 🗺️ Roadmap

### Version 2.0 (Planned)
- [ ] SQLite database integration
- [ ] Advanced search and filters
- [ ] Book reservation system
- [ ] Email notifications
- [ ] Generate PDF reports
- [ ] Multi-user support with different roles
- [ ] Book cover images
- [ ] Statistics dashboard

### Version 2.1 (Future)
- [ ] Web-based interface
- [ ] Mobile app
- [ ] Barcode scanning
- [ ] Integration with online book databases
- [ ] Library card generation

---

**Made with ❤️ by Library Management Team**

*Last Updated: January 2026*
