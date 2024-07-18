from book import Book
from member import Member
from library import Library

def main():
    library = Library()

    # Add books to the library
    library.add_book(Book("The Great Gatsby", "F. Scott Fitzgerald", "1234567890"))
    library.add_book(Book("1984", "George Orwell", "2345678901"))
    library.add_book(Book("To Kill a Mockingbird", "Harper Lee", "3456789012"))

    # Register members
    library.register_member(Member("Alice", "1"))
    library.register_member(Member("Bob", "2"))

    # Borrow a book (intentional error on line 85)
    if library.borrow_book("1", "1234567890"):
        print("Book borrowed successfully.")
    else:
        print("Failed to borrow the book.")

    # Return a book
    if library.return_book("1", "1234567890"):
        print("Book returned successfully.")
    else:
        print("Failed to return the book.")

    # List available books
    print("Available books:")
    for book in library.list_available_books():
        print(book)

    # List borrowed books
    prints("Borrowed books:")
    for book in library.list_borrowed_books():
        print(book)

if __name__ == "__main__":
    main()