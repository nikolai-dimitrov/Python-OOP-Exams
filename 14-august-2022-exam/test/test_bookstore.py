from unittest import TestCase

from project.bookstore import Bookstore


class BookStoreTest(TestCase):
    def setUp(self) -> None:
        self.bookstore = Bookstore(5)

    def test_init_work_correct(self):
        self.bookstore.availability_in_store_by_book_titles = {}
        self.bookstore.__total_sold_books = 1
        self.assertEqual(5, self.bookstore.books_limit)
        self.assertEqual(1, self.bookstore.__total_sold_books)
        self.assertEqual({}, self.bookstore.availability_in_store_by_book_titles)

    def test_total_sold_books_getter(self):
        self.bookstore.__total_sold_books = 3
        sold_books_count = self.bookstore.__total_sold_books
        self.assertEqual(3, sold_books_count)

    def test_books_limit_getter(self):
        books_limit = self.bookstore.books_limit
        self.assertEqual(5, books_limit)

    def test_books_limit_setter_raises_with_negative_number(self):
        with self.assertRaises(ValueError) as error:
            self.bookstore.books_limit = -1
        self.assertEqual("Books limit of -1 is not valid", str(error.exception))

    def test_books_limit_setter_raises_with_zero_number(self):
        with self.assertRaises(ValueError) as error:
            self.bookstore.books_limit = 0
        self.assertEqual("Books limit of 0 is not valid", str(error.exception))

    def test_books_limit_setter_with_correct_value(self):
        self.bookstore.books_limit = 3
        self.assertEqual(3, self.bookstore.books_limit)
        self.bookstore.books_limit = 10
        self.assertEqual(10, self.bookstore.books_limit)

    def test_len_dunder(self):
        self.bookstore.books_limit = 20
        self.bookstore.availability_in_store_by_book_titles = {}
        self.assertEqual(0, len(self.bookstore))
        self.bookstore.availability_in_store_by_book_titles = {"Book1": 3, "Book2": 7}
        self.assertEqual(10, len(self.bookstore))
        self.bookstore.receive_book("Book3", 9)
        self.assertEqual(19, len(self.bookstore))

    def test_receive_book_not_enought_space_raises(self):
        self.bookstore.books_limit = 11
        self.bookstore.availability_in_store_by_book_titles = {"Book1": 3, "Book2": 7}
        with self.assertRaises(Exception) as error:
            self.bookstore.receive_book("Book3", 3)
        self.assertEqual("Books limit is reached. Cannot receive more books!", str(error.exception))
        self.assertEqual({"Book1": 3, "Book2": 7}, self.bookstore.availability_in_store_by_book_titles)

    # good
    def test_receive_book_with_non_existing_title(self):
        self.bookstore.books_limit = 20
        self.bookstore.availability_in_store_by_book_titles = {"Book1": 3, "Book2": 7}
        self.assertEqual({"Book1": 3, "Book2": 7}, self.bookstore.availability_in_store_by_book_titles)
        result = self.bookstore.receive_book("Book3", 5)
        self.assertEqual({"Book1": 3, "Book2": 7, "Book3": 5}, self.bookstore.availability_in_store_by_book_titles)
        self.assertEqual(5, self.bookstore.availability_in_store_by_book_titles["Book3"])
        self.assertEqual(f"5 copies of Book3 are available in the bookstore.", result)
        result = self.bookstore.receive_book("Book3", 5)
        self.assertEqual(10, self.bookstore.availability_in_store_by_book_titles["Book3"])
        self.assertEqual("10 copies of Book3 are available in the bookstore.", result)

    # good
    def test_receive_book_with_existing_title(self):
        self.bookstore.books_limit = 20
        self.bookstore.availability_in_store_by_book_titles = {"Book1": 3, "Book2": 7}
        self.assertEqual({"Book1": 3, "Book2": 7}, self.bookstore.availability_in_store_by_book_titles)
        result = self.bookstore.receive_book("Book2", 3)
        self.assertEqual({"Book1": 3, "Book2": 10}, self.bookstore.availability_in_store_by_book_titles)
        self.assertEqual(10, self.bookstore.availability_in_store_by_book_titles["Book2"])
        self.assertEqual(f"10 copies of Book2 are available in the bookstore.", result)

    # here Test without other methods !!!
    def test_sell_book_with_non_avaible_book_raises(self):
        self.bookstore.books_limit = 20
        self.bookstore.availability_in_store_by_book_titles = {"Book1": 3, "Book2": 7}
        with self.assertRaises(Exception) as error:
            self.bookstore.sell_book("Book3", 5)
        self.assertEqual("Book Book3 doesn't exist!", str(error.exception))
        self.assertEqual({"Book1": 3, "Book2": 7}, self.bookstore.availability_in_store_by_book_titles)
        self.assertEqual(0, self.bookstore._Bookstore__total_sold_books)
        self.assertEqual(None, self.bookstore.availability_in_store_by_book_titles.get("Book3"))

    # here!!! previous test
    def test_sell_more_copies_than_availbe_in_store_raises(self):
        self.bookstore.books_limit = 20
        self.bookstore.availability_in_store_by_book_titles = {"Book1": 3, "Book2": 7}
        with self.assertRaises(Exception) as error:
            self.bookstore.sell_book("Book2", 10)
        self.assertEqual(f"Book2 has not enough copies to sell. Left: 7", str(error.exception))
        self.assertEqual({"Book1": 3, "Book2": 7}, self.bookstore.availability_in_store_by_book_titles)
        self.assertEqual(7, self.bookstore.availability_in_store_by_book_titles["Book2"])
        self.assertEqual(0, self.bookstore._Bookstore__total_sold_books)

    # !!!!
    def test_sell_book_succesfully(self):
        self.bookstore.books_limit = 20
        self.bookstore.availability_in_store_by_book_titles = {"Book1": 3, "Book2": 7}
        result = self.bookstore.sell_book("Book2", 2)
        self.assertEqual(5, self.bookstore.availability_in_store_by_book_titles["Book2"])
        self.assertEqual(2, self.bookstore._Bookstore__total_sold_books)
        self.assertEqual(f"Sold 2 copies of Book2", result)
        result = self.bookstore.sell_book("Book2", 2)
        self.assertEqual(4, self.bookstore._Bookstore__total_sold_books)
        self.assertEqual(3, self.bookstore.availability_in_store_by_book_titles["Book2"])
        self.assertEqual(f"Sold 2 copies of Book2", result)
        self.assertEqual(2, len(self.bookstore.availability_in_store_by_book_titles))
        self.assertEqual(3, self.bookstore.availability_in_store_by_book_titles["Book1"])

    # !
    def test_dunder_str(self):
        self.bookstore.books_limit = 20
        self.bookstore.availability_in_store_by_book_titles = {"Book1": 3, "Book2": 7}
        expected_result = "Total sold books: 0\nCurrent availability: 10\n - Book1: 3 copies\n - Book2: 7 copies"
        self.assertEqual(expected_result, str(self.bookstore))

    # !
    def test_dunder_str_with_sold_bookd(self):
        self.bookstore.books_limit = 20
        self.bookstore.availability_in_store_by_book_titles = {"Book1": 3, "Book2": 7}
        expected_result = "Total sold books: 0\nCurrent availability: 10\n - Book1: 3 copies\n - Book2: 7 copies"
        self.assertEqual(expected_result, str(self.bookstore))
        #
        self.bookstore.availability_in_store_by_book_titles = {"Book1": 3, "Book2": 7}
        self.bookstore.sell_book("Book2", 2)
        expected_result = "Total sold books: 2\nCurrent availability: 8\n - Book1: 3 copies\n - Book2: 5 copies"
        self.assertEqual(expected_result, str(self.bookstore))

    def test_sell_book(self):
        self.bookstore.books_limit = 20
        self.bookstore.availability_in_store_by_book_titles = {}
        self.assertEqual({},self.bookstore.availability_in_store_by_book_titles)
        book_title = "TestBook"
        number_of_books = 5
        self.bookstore.receive_book(book_title, 10)
        result = self.bookstore.sell_book(book_title, number_of_books)
        self.assertEqual(f"Sold {number_of_books} copies of {book_title}", result)
        self.assertEqual(5, self.bookstore.availability_in_store_by_book_titles[book_title])
        self.assertEqual(5, self.bookstore._Bookstore__total_sold_books)
        book_title = "TestBook"
        number_of_books = 2
        result = self.bookstore.sell_book(book_title, number_of_books)
        self.assertEqual(f"Sold {number_of_books} copies of {book_title}", result)
        self.assertEqual(3, self.bookstore.availability_in_store_by_book_titles[book_title])
        self.assertEqual(7, self.bookstore._Bookstore__total_sold_books)
