# many_to_many.py

# -------------------------------
# Book Class
# -------------------------------
class Book:
    """
    Represents a Book.
    Tracks all books in the class-level list `all`.
    """
    all = []  # Class attribute storing all Book instances

    def __init__(self, title):
        """
        Initialize a book with a title.
        Raises an exception if title is not a string.
        """
        if not isinstance(title, str):
            raise Exception("Title must be a string")
        self.title = title
        Book.all.append(self)  # Add the new book to the class list

    def contracts(self):
        """
        Returns a list of all Contract instances related to this book.
        Uses Contract.all as the source.
        """
        return [c for c in Contract.all if c.book == self]

    def authors(self):
        """
        Returns a list of unique Author instances associated with this book.
        Uses contracts() as an intermediary.
        """
        return list({c.author for c in self.contracts()})

    def __repr__(self):
        """Readable representation of Book for debugging."""
        return f"<Book: {self.title}>"


# -------------------------------
# Author Class
# -------------------------------
class Author:
    """
    Represents an Author.
    Tracks all authors in the class-level list `all`.
    """
    all = []  # Class attribute storing all Author instances

    def __init__(self, name):
        """
        Initialize an author with a name.
        Raises an exception if name is not a string.
        """
        if not isinstance(name, str):
            raise Exception("Name must be a string")
        self.name = name
        Author.all.append(self)  # Add new author to class list

    def contracts(self):
        """
        Returns a list of all Contract instances related to this author.
        """
        return [c for c in Contract.all if c.author == self]

    def books(self):
        """
        Returns a list of unique Book instances associated with this author.
        Uses contracts() as an intermediary.
        """
        return list({c.book for c in self.contracts()})

    def sign_contract(self, book, date, royalties):
        """
        Create a new Contract instance connecting this author with a book.
        Returns the newly created Contract.
        """
        return Contract(self, book, date, royalties)

    def total_royalties(self):
        """
        Calculates and returns the total royalties this author has earned
        from all their contracts.
        """
        return sum(c.royalties for c in self.contracts())

    def __repr__(self):
        """Readable representation of Author for debugging."""
        return f"<Author: {self.name}>"


# -------------------------------
# Contract Class
# -------------------------------
class Contract:
    """
    Represents a Contract linking an Author and a Book.
    Stores date and royalties information.
    Tracks all contracts in the class-level list `all`.
    """
    all = []  # Class attribute storing all Contract instances

    def __init__(self, author, book, date, royalties):
        """
        Initialize a contract.
        Validates:
        - author is an Author instance
        - book is a Book instance
        - date is a string
        - royalties is an integer
        Adds the new contract to Contract.all.
        """
        if not isinstance(author, Author):
            raise Exception("author must be Author instance")
        if not isinstance(book, Book):
            raise Exception("book must be Book instance")
        if not isinstance(date, str):
            raise Exception("date must be string")
        if not isinstance(royalties, int):
            raise Exception("royalties must be integer")

        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties

        Contract.all.append(self)  # Track all contracts

    @classmethod
    def contracts_by_date(cls, date):
        """
        Class method.
        Returns a list of all Contract instances that match the given date.
        Useful for filtering contracts by date.
        """
        return [c for c in cls.all if c.date == date]

    def __repr__(self):
        """Readable representation of Contract for debugging."""
        return f"<Contract {self.author.name} - {self.book.title} ({self.date})>"