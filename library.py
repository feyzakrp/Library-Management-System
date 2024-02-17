"""
Library Management System
"""
import datetime


class Library:

    # constructor method
    def __init__(self):
        
        # Open books.txt in read and write mode(a+)
        # If the file does not exist, create it
        self.file = open("books.txt",mode="a+",encoding="utf-8")
        
        # To get the ID of the last added book, call the get_last_book_id() method and initialize the last_book_id property
        self.last_book_id = self.get_last_book_id()

    # returns list of books (id,book name, writer, release date, book pages and current date)
    def list_books(self):
        try:
            with open("books.txt", "r",encoding="utf-8") as self.file:
                # Read all lines in the file and put them in the books list 
                books = self.file.readlines()
                if not books:
                    # Notify the user if there is no book in the file
                    print("There are no books listed.")
                else:
                    
                    # If there are books, print the books to the screen
                    print("List of books:")
                    for book in books:
                        
                        # Print books by removing the newline character at the end of each line
                        print(book.splitlines())

        except FileNotFoundError:        
            # Print error message if file not found
            print("The file 'books.txt' does not exist.")

    def get_last_book_id(self):
        try:
            with open("books.txt", "r", encoding="utf-8") as file:
                # Read all lines in the file and put them in the lines list
                lines = file.readlines()
                if lines:
                    # If the file is not empty, select the last line and split it with split()
                    # Take the first piece i.e. ID and convert it to integer
                    last_line = lines[-1]
                    last_book_id = int(last_line.split(',')[0])
                else:
                    # If the file is empty, set the starting ID to 0
                    last_book_id = 0
                return last_book_id
        except FileNotFoundError:
            # If the file is not found, set the starting ID to 0
            return 0

    # Method used to add a new book with information received from the user
    def add_book(self):
        # Increase the ID of the last added book by one
        self.last_book_id += 1
        book_id = self.last_book_id
        book_name = input("Book Name: ")
        writer = input("Writer Name: ")
        release_date = input("Release Date: ")
        current_date = datetime.datetime.now().strftime("%Y-%m-%d")
        book_pages = input("Book Pages: ")

       # returns the add book function and print result
        try:
            with open("books.txt","a",encoding="utf-8") as file:
                # Write the information of the book to the file
                file.write(f"{book_id},{book_name},{writer},{release_date},{book_pages},{current_date}\n")
            print(f"{book_name} has been added successfully..")
        except Exception as e:
            print(f"Error occurred while adding the book: {e}")

    # Method used to remove a book with information received from the user
    def remove_book(self):
        book_name = input("Book Name: ")
        
        # checking whether the book exists
        with open("books.txt", "r", encoding="utf-8") as file:
            lines = file.readlines()

        found = False
        with open("books.txt", "w", encoding="utf-8") as file:
            for line in lines:
                if book_name in line:
                    found = True
                else:
                    # If the book is found, write to the file and remove it
                    file.write(line)
   
        if found:
            # print result
            print(f"{book_name} has been removed from the library.")
        else:
            print(f"{book_name} is not found in the library.")

    # Method that provides menu options to the user
    def menu(self):
        while True:
                print("******************MENU******************")
                # Get action option from user
                islem = input("1- List Books\n2- Add Book\n3- Remove Book\n4- Quit(You can quit with key 'q')\n")

                # Call the relevant method according to the user's option
                if islem ==  "1":
                    self.list_books()
                elif islem == "2":
                    self.add_book()
                elif islem == "3":
                    self.remove_book()
                # Exit the loop if the user enters the "q" key or option "4"
                elif islem.lower() == "q" or islem == "4":
                    break
                else:
                    # Print an error message to the user if an invalid option is entered
                    print("Invalid choice. Please enter a valid option.")
                
    # destructor method
    def __del__(self):
        # Close the file and print an information message to the user
        self.file.close()
        print(f"File has been closing...")


# Create an object from the Library class and call the menu
lib = Library()
lib.menu()


