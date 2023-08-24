class Library:
    def __init__(self, name):
        self.name = name
        self.list_of_books = []
    
    def add_book(self, book):
        self.list_of_books.append(book)
    
    def remove_book(self, book):
        self.list_of_books.remove(book)
    
    def list_books(self):
        for book in self.list_of_books:
            print(book.name)  # Print the name of each book

class Book:
    def __init__(self, name, author):
        self.name = name
        self.author = author

rog = Book("Rog", "Annon")
lct = Library("lct")
lct.add_book(rog)
lct.list_books()  # Print the names of books in the library
