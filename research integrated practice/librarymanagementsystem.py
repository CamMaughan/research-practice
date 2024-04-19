# librarymanagementsystem.py
# Author: C.Maughan
# Date: 19/4/24

'''

This is a project to practice OOP principles. I will focus on integrating the principles I have learned so far in
this repository; inheritance, encapsulation, open closed principle, property decorators and single responsibility
principle.

The project is a library management system. It will have a library class, a book class and a user class. The library
class will be responsible for loaning books to users. The book class will be responsible for
creating book objects. The user class will be responsible for creating user objects.

'''

# Import regular expression module
import re


class Books:
    def __init__(self, title, author, genre, status, isbn):
        self.title = title
        self.author = author
        self.genre = genre
        self.status = status
        self.isbn = isbn

    # Get private status attribute
    @property
    def status(self):
        return self._status

    # Ensure status is either 'available' or 'borrowed'
    @status.setter
    def status(self, value):
        if value in ['available', 'borrowed']:
            self._status = value
        else:
            raise ValueError("Status must be either 'available' or 'borrowed'")


class User:
    def __init__(self, library_id, first_name, last_name, email):
        self.library_id = library_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    # Get private email attribute
    @property
    def email(self):
        return self._email

    # Ensure email is in correct format
    @email.setter
    def email(self, value):
        if re.match(r"[^@]+@[^@]+\.[^@]+", value):  # Check email format
            self._email = value
        else:
            raise ValueError("Invalid email address")


class Library:
    def __init__(self):
        self.books = []  # List to store book objects
        self.users = []  # List to store user objects

    def add_book(self, book):
        self.books.append(book)

    def add_user(self, user):
        self.users.append(user)

    def lend_book(self, user_id, book_isbn):
        for book in self.books:  # Loop through books
            if book.isbn == book_isbn:  # If book isbn matches
                if book.status == 'available':
                    book.status = 'borrowed'
                    return f"{book.title} has been loaned to user {user_id}"
                else:
                    return f"{book.title} is not available"
        return f"Book with ISBN {book_isbn} not found"

    def return_book(self, user_id, book_isbn):
        for book in self.books:  # Loop through books
            if book.isbn == book_isbn:  # If book isbn matches
                if book.status == 'borrowed':
                    book.status = 'available'
                    return f"{book.title} has been returned by user {user_id}"
                else:
                    return f"{book.title} is not borrowed"
        return f"Book with ISBN {book_isbn} not found"


# Set main function for user input

def main():
    while True:
        print("\nWelcome to the library management system")
        print("1. Add a book")
        print("2. Add a user")
        print("3. Loan a book")
        print("4. Return a book")
        print("5. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            genre = input("Enter book genre: ")
            isbn = input("Enter book ISBN: ")
            while True:
                try:  # Ensure status is either 'available' or 'borrowed'
                    status = input("Enter book status: ")
                    book = Books(title, author, genre, status, isbn)
                    library.add_book(book)
                    print(f"{book.title} has been added to the library")
                    break
                except ValueError as e:
                    print(e)

        elif choice == "2":
            library_id = input("Enter library ID: ")
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            while True:
                try:  # Ensure email is in correct format
                    email = input("Enter email: ")
                    user = User(library_id, first_name, last_name, email)
                    library.add_user(user)
                    print(f"{user.first_name} {user.last_name} has been added to the library")
                    break
                except ValueError as e:
                    print(e)

        elif choice == "3":
            user_id = input("Enter user ID: ")
            book_isbn = input("Enter book ISBN: ")
            print(library.lend_book(user_id, book_isbn))

        elif choice == "4":
            user_id = input("Enter user ID: ")
            book_isbn = input("Enter book ISBN: ")
            print(library.return_book(user_id, book_isbn))

        elif choice == "5":
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    library = Library()
    main()

'''
The main function acts as the responsibility for interacting with the user. This has been good practice for the
single responsibility principle. The main function is for user input, to verify that input, then
to call the appropriate methods in the Library class. The other three classes stick to their own responsibilities. 
Which makes them open for extension but closed for modification. 

The property decorators have been used to ensure that the status attribute in the Books class and the email attribute
in the User class are in the correct format. This is an example of encapsulation.

Inheritance has not been necessary for this project.

The code has been refactored to keep tidy, though I am not confident on the best way to keep the main function tidy.
I noticed that the main function is quite long and could possibly be broken down into smaller functions. Though
I am not sure if this is the best way to keep the code abiding to the best programming principles.

'''