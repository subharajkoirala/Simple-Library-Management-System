# GUI Library Management System - Setup Guide

## Files You Need

Replace your old text-based files with these new GUI versions:

### Core Files (Replace these):
1. **Main_LMS_GUI.py** - Main program (run this!)
2. **login_gui.py** - Login screen
3. **menu_gui.py** - Main menu dashboard
4. **add_books_gui.py** - Add books module
5. **list_books_gui.py** - List books module
6. **loan_book_gui.py** - Loan books module
7. **patron_clearing_gui.py** - Return books module

### Keep These:
- **Book_list.csv** - Your book database

## Installation Steps

### Step 1: Copy Files
Put all the new GUI files in the same folder as your `Book_list.csv`

### Step 2: File Structure
Your folder should look like:
```
Library_Management/
├── Main_LMS_GUI.py          ← Run this file!
├── login_gui.py
├── menu_gui.py
├── add_books_gui.py
├── list_books_gui.py
├── loan_book_gui.py
├── patron_clearing_gui.py
└── Book_list.csv
```

### Step 3: Run the Program
```bash
python Main_LMS_GUI.py
```

## How to Use

### 1. Login Screen
- **Username:** Librarian
- **Password:** 2520
- Press "Login" or hit Enter

### 2. Main Menu
Click any button:
- 📚 **List All Books** - View all books in a table
- ➕ **Add Books** - Add new books to library
- 📖 **Loan Books** - Loan books to students
- ✅ **Clear Patron** - Return books / Clear fines
- 🚪 **Exit** - Close the program

### 3. Each Function Opens a New Window
- Fill in the forms
- Click buttons to perform actions
- Close window to return to menu

## Features

### ✅ What's New
- Beautiful graphical interface
- Color-coded book status (green = available, red = borrowed)
- Automatic fine calculation
- Error messages and confirmations
- Easy-to-use forms
- Professional styling

### 🎨 Customization
Want to change colors? Edit these lines in each file:
```python
self.primary_color = "#2c3e50"      # Dark blue-grey
self.secondary_color = "#3498db"    # Bright blue
self.accent_color = "#e74c3c"       # Red
self.bg_color = "#ecf0f1"           # Light grey
```

## Troubleshooting

### Problem: "No module named 'pandas'"
**Solution:**
```bash
pip install pandas
```

### Problem: "No module named 'tkinter'"
**Solution:**
- Tkinter comes with Python
- If missing, reinstall Python and check "tcl/tk" option

### Problem: Program closes immediately
**Solution:**
- Make sure `Book_list.csv` exists in the same folder
- Check file has correct columns

### Problem: Can't see the window
**Solution:**
- Check if window opened behind other windows
- Try Alt+Tab to find it

## Tips

1. **File Selection**: When adding/listing/loaning books, you'll be asked to select the CSV file. Choose `Book_list.csv`

2. **Multiple Operations**: After completing an operation, you return to the main menu to do more

3. **Data Safety**: All changes are automatically saved to `Book_list.csv`

4. **Overdue Books**: System automatically calculates fines at Rs. 20 per day

## Quick Reference

### Login Credentials
```
Username: Librarian
Password: 2520
```

### File Selection
Always select: `Book_list.csv`

### Fine Calculation
- Loan period: 15 days
- Fine: Rs. 20 per day after due date

## Need Help?

Check the `GUI_Development_Guide.md` file for:
- How the code works
- How to modify it
- Learning tkinter basics
- Adding new features

---

**Ready to use your new GUI system!** 🚀

Just run: `python Main_LMS_GUI.py`
