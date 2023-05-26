from unittest import TestCase

from project.library import Library


class LibraryTests(TestCase):
    NAME = "Test"
    AUTHOR = "TestAuthor"
    TITLE = "TestBookTitle"

    def setUp(self) -> None:
        self.library = Library(self.NAME)

    def test_init_work_correct(self):
        self.library.books_by_authors = {"TestAuthor": ["TestBookTitle"]}
        self.library.readers = {"TestReader": [{"TestAuthor": ["TestBookTitle"]}]}
        self.assertEqual(self.NAME, self.library.name)
        self.assertEqual({"TestAuthor": ["TestBookTitle"]}, self.library.books_by_authors)
        self.assertEqual({"TestReader": [{"TestAuthor": ["TestBookTitle"]}]}, self.library.readers)

    def test_getter_and_setter_name_work_correct(self):
        result = self.library.name
        self.assertEqual(self.NAME, result)
        result = self.library.name = "TestName"
        self.assertEqual("TestName", result)

    def test_setter_with_empty_value_raises(self):
        with self.assertRaises(ValueError) as error:
            self.library.name = ""
        self.assertEqual("Name cannot be empty string!", str(error.exception))

    def test_add_book_with_non_existing_author_and_non_existing_title(self):
        self.library.add_book(self.AUTHOR, self.TITLE)
        self.assertEqual({'TestAuthor': ['TestBookTitle']}, self.library.books_by_authors)

    def test_add_book_with_non_existing_author(self):
        self.library.books_by_authors["TestAuthor"] = []
        self.library.add_book(self.AUTHOR, self.TITLE)
        self.assertEqual({'TestAuthor': ['TestBookTitle']}, self.library.books_by_authors)

    def test_add_book_with_existing_author_and_existing_title(self):
        self.library.books_by_authors = {'TestAuthor': ['TestBookTitle']}
        self.library.add_book(self.AUTHOR, self.TITLE)
        self.assertEqual({'TestAuthor': ['TestBookTitle']}, self.library.books_by_authors)

    def test_add_reader_with_non_registred_reader(self):
        self.library.add_reader("TestReader")
        expected_result = {"TestReader": []}
        self.assertEqual(expected_result, self.library.readers)

    def test_add_reader_with_already_registred_reader(self):
        self.library.readers = {"TestReader": []}
        result = self.library.add_reader("TestReader")
        expected_result = f"TestReader is already registered in the {self.NAME} library."
        self.assertEqual(expected_result, result)
        self.assertEqual({"TestReader": []}, self.library.readers)

    def test_rent_book_with_non_existing_reader_name(self):
        reader_name = "TestReader"
        result = self.library.rent_book(reader_name, self.AUTHOR, self.TITLE)
        expected_result = f"{reader_name} is not registered in the {self.library.name} Library."
        self.assertEqual(expected_result, result)

    def test_rent_book_with_non_existing_author(self):
        self.library.books_by_authors = {"Non existing author": ["Title"]}
        self.library.readers = {"TestReader": [{"TestAuthor": ["TestBookTitle"]}]}
        result = self.library.rent_book("TestReader", self.AUTHOR, self.TITLE)
        expected_result = f"{self.library.name} Library does not have any {self.AUTHOR}'s books."
        self.assertEqual(expected_result, result)
        # care

    def test_rent_book_with_non_existing_book_title(self):
        self.library.readers = {"TestReader": [{"TestAuthor": ["TestBookTitle"]}]}
        self.library.books_by_authors = {"Author": ["TestTitle"]}
        result = self.library.rent_book("TestReader", "Author", "NonExistingTitle")
        expected_result = f"""{self.library.name} Library does not have Author's "NonExistingTitle"."""
        self.assertEqual(expected_result, result)

    def test_rent_book_work_correct(self):
        # self.readers[reader_name].append({book_author: book_title})
        # book_title_index = self.books_by_authors[book_author].index(book_title)
        # del self.books_by_authors[book_author][book_title_index]
        self.library.books_by_authors = {"TestAuthor": ["TestBookTitle"]}
        self.library.readers = {"TestReader": []}
        self.library.rent_book("TestReader", "TestAuthor", "TestBookTitle")
        expected_result = {"TestReader": [{"TestAuthor": "TestBookTitle"}]}
        self.assertEqual(expected_result, self.library.readers)
        self.assertEqual({"TestAuthor": []},self.library.books_by_authors)