from project.library import Library
from unittest import TestCase,main

class TestLibrary(TestCase):
    def setUp(self) -> None:
        self.library = Library("Lib")
        self.library.books_by_authors["Stephen Hawking"] = []
        self.library.readers["Ivan"] = []
    def test_init(self):
        name = "Lib"
        library = Library(name)
        self.assertEqual(name,library.name)
        self.assertEqual({},library.books_by_authors)
        self.assertEqual({},library.readers)

    def test_name_setter_exception(self):
        name = ""
        with self.assertRaises(ValueError) as ex:
            library = Library(name)
        self.assertEqual("Name cannot be empty string!",str(ex.exception))

    def test_add_book_with_non_existing_author(self):
        author = "J.K Roling"
        book = "Harry Potter 2"
        self.library.add_book(author,book)
        self.assertEqual({"J.K Roling":["Harry Potter 2"],"Stephen Hawking":[]},self.library.books_by_authors)

    def test_add_book_with_existing_author(self):
        author = "Stephen Hawking"
        book = "Brief History of time"
        self.library.add_book(author,book)
        self.assertEqual({'Stephen Hawking': ["Brief History of time"]},self.library.books_by_authors)

    def test_add_reader_existing_reader(self):
        name = "Ivan"
        res = self.library.add_reader(name)
        self.assertEqual({"Ivan":[]},self.library.readers)
        self.assertEqual("Ivan is already registered in the Lib library.",res)

    def test_add_reader_non_existing_reader(self):
        name = "Gosho"
        self.library.add_reader(name)
        self.assertEqual({"Ivan":[],"Gosho":[]},self.library.readers)

    def test_rent_book_non_existing_reader_error(self):
        self.library.books_by_authors["Stephen Hawking"] = ["Brief History of Time"]
        name = "Gosho"
        res = self.library.rent_book(name,"Stephen Hawking","Brief History of Time")
        self.assertTrue(name not  in self.library.readers)
        self.assertEqual("Gosho is not registered in the Lib Library.",res)


    def test_rent_book_non_existing_author_error(self):
        name = "Ivan"
        author = "J.K. Rolings"
        book = "Harry Potter"
        res = self.library.rent_book(name,author,book)
        self.assertEqual({"Ivan":[]},self.library.readers)
        self.library.rent_book(name,author,book)
        self.assertEqual({"Ivan": []}, self.library.readers)
        self.assertEqual("Lib Library does not have any J.K. Rolings's books.",res)

    def test_rent_book_non_existing_author_book_error(self):
        name = "Ivan"
        author = "Stephen Hawking"
        book = "Biref History of time"
        res = self.library.rent_book(name,author,book)
        self.assertEqual({'Ivan':[]},self.library.readers)
        self.assertTrue(author in self.library.books_by_authors)
        self.assertEqual('Lib Library does not have Stephen Hawking\'s "Biref History of time".',res)

    def test_if_rent_book_works_correctly_with_valid_inputs(self):
        self.library.books_by_authors["Stephen Hawking"] = ["Biref History of time"]
        name = "Ivan"
        author = "Stephen Hawking"
        book = "Biref History of time"
        self.library.rent_book(name,author,book)
        self.assertEqual({'Stephen Hawking': []},self.library.books_by_authors)
        self.assertTrue(author in self.library.books_by_authors)
        self.assertTrue(name in self.library.readers)
        self.assertEqual({"Ivan":[{'Stephen Hawking': "Biref History of time"}]},self.library.readers)

if __name__ == "__main__":
    main()