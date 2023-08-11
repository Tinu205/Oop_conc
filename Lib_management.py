# TODO: Define Classes

# TODO: Library Class
# - Attributes: name, location, list_of_books, list_of_patrons
# - Methods: add_book(book), remove_book(book), add_patron(patron), remove_patron(patron), display_books(), display_patrons()

# TODO: Book Class
# - Attributes: title, author, genre, publication_year, ISBN, is_available
# - Methods: mark_as_available(), mark_as_unavailable(), display_info()

# TODO: Patron Class
# - Attributes: name, contact_info, membership_status
# - Methods: update_contact_info(info), update_membership_status(status), display_info()

# TODO: Transaction Class
# - Attributes: book, patron, transaction_date
# - Methods: None (attributes to record transaction details)

# TODO: Define Class Relationships

# TODO: Library
# - Relationship: A Library has a list of books and patrons.

# TODO: Book
# - Relationship: A Book is part of a Library's collection and can have multiple Transactions.
# - Relationship: A Book can be marked as available/unavailable.

# TODO: Patron
# - Relationship: A Patron is a member of a Library and can have multiple Transactions.
# - Relationship: A Patron can update their contact info and membership status.

# TODO: Transaction
# - Relationship: A Transaction involves a specific Book and a specific Patron.

# TODO: Implement Methods and Attributes

# TODO: Library Class
# - Method: add_book(book) - Adds a book to the list_of_books.
# - Method: remove_book(book) - Removes a book from the list_of_books.
# - Method: add_patron(patron) - Adds a patron to the list_of_patrons.
# - Method: remove_patron(patron) - Removes a patron from the list_of_patrons.
# - Method: display_books() - Displays information about available books.
# - Method: display_patrons() - Displays information about patrons.

# TODO: Book Class
# - Method: mark_as_available() - Sets is_available attribute to True.
# - Method: mark_as_unavailable() - Sets is_available attribute to False.
# - Method: display_info() - Displays detailed information about the book.

# TODO: Patron Class
# - Method: update_contact_info(info) - Updates the contact_info attribute.
# - Method: update_membership_status(status) - Updates the membership_status attribute.
# - Method: display_info() - Displays detailed information about the patron.

# TODO: Transaction Class
# - Attributes: Holds attributes for book, patron, transaction_date.

# TODO: Additional Steps

# TODO: Create instances of Library, Book, and Patron classes to simulate interactions.

# TODO: Implement user interfaces to interact with the library system.

# TODO: Add error handling to ensure smooth execution and user-friendly experience.

# TODO: Implement data persistence using file handling or a database.

# TODO: Write comprehensive unit tests to validate class methods.

# TODO: Create clear and concise documentation explaining class purpose and usage.

# TODO: Summarize project goals and how it demonstrates understanding of OOP concepts.

# TODO: Conclude the project description with a thank you or final thoughts.

class Library:
    def __init__(self,name,location):
        self.name = name
        self.location = location
        self.list_of_books  = []
        self.list_of_patrons = []
    
    def add_book(self,book):
        self.list_of_books.append(book)

    def remove_book(self,book):
        self.list_of_books.remove(book)

    def add_patrons(self,patron):
        self.list_of_patrons.append(patron)

    def remove_patron(self,patron):
        self.list_of_patrons.remove(patron)

    def display_books(self):
        for book in self.list_of_books:
            print(book)
        
    def display_patron(self):
        for patron in self.list_of_patrons:
            print(patron)

class Book:
    def __init__(self,title,author,genre,isbn):
        self.title = title
        self.author = author
        self.genre = genre
        self.isbn = isbn
        self.is_available = None

    def mark_as_available(self):
        self.is_available = True

    def mark_as_unavailable(self):
        self.is_available = False

    def display_info(self):
        print(f"Book name ->{self.title}\nAuthor ->{self.author}\nGenre -> {self.genre}\nISBN -> {self.isbn}")
        if(self.is_available):
            print("Available")
        else:
            print("Not available")

class Patron:
    def __init__(self,name,contact_info):
        self.name = name
        self.contact_info = contact_info
        self.membership_status = True

    def update_contact_info(self,new_info):
        self.contact_info = new_info

    def update_membership_status(self,status):
        self.membership_status = status
    
    def display_info(self):
        print(f"Name -> {self.name}\nContact info -> {self.contact_info}")
        if(self.membership_status):
            print("Membership status: Is a member")
        else:
            print("Membership status: Not a member")
    
