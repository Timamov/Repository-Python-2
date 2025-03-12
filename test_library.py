class TestLibrary:
    def test_library(self, library):
        assert library.name == "Aristotel Library"

    def library_operations_add(self, library):
        assert library.books is not None
        assert library.new_book is not None

    def library_operations_delete(self, library):
        assert library.delete_book is not None
