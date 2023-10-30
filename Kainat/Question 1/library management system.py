class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.checked_out = False

    def check_out(self):
        if not self.checked_out:
            self.checked_out = True
            return f"Checked out: {self.title} by {self.author}"
        else:
            return f"{self.title} is already checked out."

    def return_book(self):
        if self.checked_out:
            self.checked_out = False
            return f"Returned: {self.title} by {self.author}"
        else:
            return f"{self.title} is not checked out."


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        print(f"Available books in {self.name}:")
        for book in self.books:
            if not book.checked_out:
                print(f"{book.title} by {book.author}")

    def remove_book(self, title):
        for book in self.books:
            if title.lower() in book.title.lower():
                self.books.remove(book)
                return f"Removed: {book.title} by {book.author}"
        return f"Book not found: {title}"


class MemberLibrary(Library):
    def __init__(self, name):
        super().__init__(name)
        self.members = {}

    def register_member(self, member_name):
        if member_name not in self.members:
            self.members[member_name] = []

    def view_checked_out_books(self, member_name):
        if member_name in self.members:
            checked_out_books = self.members[member_name]
            if checked_out_books:
                print(f"{member_name}'s checked-out books:")
                for book in checked_out_books:
                    print(f"{book.title} by {book.author}")
            else:
                print(f"{member_name} has no books checked out.")
        else:
            print(f"{member_name} is not a registered member of {self.name}.")

    def check_out_book(self, member_name, title):
        if member_name in self.members:
            for book in self.books:
                if title.lower() in book.title.lower() and not book.checked_out:
                    self.members[member_name].append(book)
                    return f"{member_name} checked out: {book.title} by {book.author}"
            return f"{member_name} cannot check out {title}. The book is already checked out or not available."
        else:
            return f"{member_name} is not a registered member of {self.name}."

    def return_book(self, member_name, title):
        if member_name in self.members:
            for book in self.members[member_name]:
                if title.lower() in book.title.lower():
                    self.members[member_name].remove(book)
                    book_status = book.return_book()
                    return f"{member_name} returned: {book_status}"
            return f"{member_name} does not have {title} checked out."
        else:
            return f"{member_name} is not a registered member of {self.name}"



if __name__ == "__main__":
    
    library = MemberLibrary("My Library")

    
    book1 = Book("Hum safar")
    book2 = Book("The great Leader")
    book3 = Book("Ego is enemy")

    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)

    library.list_books()

    print(library.remove_book("Alice","Hum safar"))

    library.register_member("Alice")

    print(library.check_out_book("Alice", "The great Leader"))
    library.view_checked_out_books("Alice")

    print(library.return_book("Alice", "Ego is enemy"))
    library.view_checked_out_books("Alice")
