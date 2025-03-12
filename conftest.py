import pytest

from models import Person
from test_book_models import Book, Library


@pytest.fixture()
def person() -> Person:
    oleg = Person("oleg")
    return oleg


@pytest.fixture()
def another_person() -> Person:
    oleg = Person("oleg")
    return oleg


@pytest.fixture()
def book() -> Book:
    famous_book = Book("Robert B Weide: Before he became famous", "Robert B Weide")
    return famous_book


@pytest.fixture()
def library() -> Library:
    aristotel_library = Library("Aristotel Library")
    return aristotel_library
