import uuid


class Book:

    def __init__(self, name, author_name: str):
        self.id = uuid.uuid4().hex
        self.author_name = author_name
        self.name = name

    def __str__(self):
        return f"{self.author_name}: {self.name}. id: {self.id}"


class Library:
    def __init__(self, name: str):
        self.name = name
        self.books = []

    def add_book(self, work: Book):
        self.books.append(work)

    def delete_books(self, work: Book):
        for book in self.books:
            if book == work:
                self.books.remove(work)
                break


pass
