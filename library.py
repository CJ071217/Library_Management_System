from book import Book
from member import Member

class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)

    def register_member(self, member):
        self.members.append(member)

    def find_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None

    def find_member(self, member_id):
        for member in self.members:
            if member.member_id == member_id:
                return member
        return None

    def borrow_book(self, member_id, isbn):
        member = self.find_member(member_id)
        book = self.find_book(isbn)
        if member and book:
            return member.borrow_book(book)
        return False

    def return_book(self, member_id, isbn):
        member = self.find_member(member_id)
        book = self.find_book(isbn)
        if member and book:
            return member.return_book(book)
        return False

    def list_available_books(self):
        return [book for book in self.books if not book.is_borrowed]

    def list_borrowed_books(self):
        return [book for book in self.books if book.is_borrowed]