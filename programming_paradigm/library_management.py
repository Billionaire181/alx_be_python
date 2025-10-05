class Book:
    def __init__(self, title, author):
        self.author = author
        sekf.title = title
        self.is_checked_out = False


class Library:
    def __init__(self):
        # Initialize an empty list to hold all Book objects
        self._books = []

    def add_book(self, book):
        """Add a new book (Book object) to the library"""
        self._books.append(book)
        print(f"Book '{book.title}' by {book.author} added to the library.")

    def list_available_books(self):
        """List all books that are not checked out"""
        available_books = [book for book in self._books if not book._is_checked_out]
        
        if not available_books:
            print("No books are currently available.")
        else:
            print("Available books:")
            for book in available_books:
                print(f"- {book.title} by {book.author}")

    def check_out_book(self, title):
        """Mark a book as checked out if it’s available"""
        for book in self._books:
            if book.title == title:
                if not book._is_checked_out:
                    book._is_checked_out = True
                    print(f"You have checked out '{book.title}'.")
                else:
                    print("Sorry, this book is already checked out.")
                return
        print("Book not found in the library.")

    def return_book(self, title):
        """Mark a book as returned (available again)"""
        for book in self._books:
            if book.title == title:
                if book._is_checked_out:
                    book._is_checked_out = False
                    print(f"'{book.title}' has been returned.")
                else:
                    print("This book wasn’t checked out.")
                return
        print("Book not found in the library.")
