class TestBook:
    def test_book(self, book):
        assert book.id != 0

    def test_creating_book(self, book, library):
        library.add_book(book)
        assert book in library.books

    def test_removing_book(self, book, library):
        library.delete_books(book)
        assert book not in library.books
