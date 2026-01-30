"""
Library Management System - GUI Version
Main Entry Point

This is the main file to run the Library Management System with GUI.
It imports and uses all the GUI modules.
"""

from login_ import login
from menu_ import main_menu
from add_books_ import add_books
from list_books_ import list_books
from loan_book_ import lending_book
from patron_clearing_ import patron_clearing


def main():
    """Main function to run the Library Management System"""
    
    # Show login screen
    if login():
        # Login successful, show main menu loop
        while True:
            choice = main_menu()
            
            # If user closed the window without selecting, exit
            if choice is None:
                print("Program closed.")
                break
            
            # Handle menu choices
            if choice == "1":
                # List all books
                list_books()
                
            elif choice == "2":
                # Add new books
                add_books()
                
            elif choice == "3":
                # Loan books to students
                lending_book()
                
            elif choice == "4":
                # Clear patron / return books
                patron_clearing()
                
            elif choice == "5":
                # Exit program
                print("Exiting program...")
                break
                
            else:
                print("Invalid choice.")
    else:
        print("Login failed. Exiting program.")


if __name__ == "__main__":
    main()
