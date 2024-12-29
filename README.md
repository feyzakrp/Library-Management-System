# Library Management System

## Overview
The Library Management System is a simple Python application that allows users to manage a collection of books. Users can list, add, and remove books from the library. The data is stored in a file named `books.txt` to maintain a persistent record of the books in the library.

## Features
- **List Books**: Displays all the books currently in the library.
- **Add Book**: Allows the user to add a new book by entering its details.
- **Remove Book**: Enables the user to remove a book from the library by its name.
- **Persistent Storage**: All book data is stored in `books.txt` for future reference.

## Requirements
- Python 3.x
- A writable file system to create and store the `books.txt` file.

## File Structure
- `books.txt`: This file is used to store the book records in the format:
  ```
  book_id,book_name,writer,release_date,book_pages,current_date
  ```
  Example:
  ```
  1,The Great Gatsby,F. Scott Fitzgerald,1925,218,2024-12-29
  2,1984,George Orwell,1949,328,2024-12-29
  ```
- `Library` class: Contains all the methods for managing books.

## How to Use
1. **Run the Program**:
   Execute the script in a Python environment:
   ```
   python library_management_system.py
   ```
2. **Menu Options**:
   - **1. List Books**: Displays all books in the library.
   - **2. Add Book**: Prompts the user to enter details about the book, including:
     - Book Name
     - Writer Name
     - Release Date
     - Number of Pages
   - **3. Remove Book**: Prompts the user to enter the name of the book they want to remove.
   - **4 or q**: Exits the program.

## Class and Method Details
### `Library` Class
- **Constructor (`__init__`)**:
  - Opens or creates `books.txt`.
  - Initializes the last book ID by reading the file.

- **`list_books()`**:
  - Reads and displays all books in `books.txt`.
  - Notifies the user if no books are present.

- **`get_last_book_id()`**:
  - Retrieves the ID of the last book in `books.txt`.

- **`add_book()`**:
  - Prompts the user for book details.
  - Appends the book information to `books.txt`.

- **`remove_book()`**:
  - Prompts the user for the name of the book to remove.
  - Removes the specified book from `books.txt` if it exists.

- **`menu()`**:
  - Displays a menu of options.
  - Calls the appropriate method based on the user's choice.

- **Destructor (`__del__`)**:
  - Closes the file and notifies the user.

## Error Handling
- If `books.txt` does not exist, it will be created automatically.
- If an invalid menu option is entered, the program displays an error message.

## Example Usage
```text
******************MENU******************
1- List Books
2- Add Book
3- Remove Book
4- Quit(You can quit with key 'q')
```
- **Option 1 (List Books)**:
  ```text
  List of books:
  ['1,The Great Gatsby,F. Scott Fitzgerald,1925,218,2024-12-29']
  ```
- **Option 2 (Add Book)**:
  ```text
  Book Name: Brave New World
  Writer Name: Aldous Huxley
  Release Date: 1932
  Book Pages: 311
  Brave New World has been added successfully..
  ```
- **Option 3 (Remove Book)**:
  ```text
  Book Name: The Great Gatsby
  The Great Gatsby has been removed from the library.
  ```
- **Option 4 or q (Quit)**:
  ```text
  File has been closing...
  ```



