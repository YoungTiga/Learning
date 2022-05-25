class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.page = 0

    def turn_page(self, page):
        self.page = page

class Library:
    def __init__(self):
        self.books = []
    def find_book(self, title):
        try:
            return [x for x in self.books if x.title == title][0]
        except IndexError:
            return "There is no such book here"

    def add_book(self,book:Book):
        if book not in self.books:
            self.books.append(book)

library = Library()
book = Book("Hooks", "J.K. Rolings")
book2 = Book("Hooks2", "J.K. Rolings")
book3 = Book("Hooks3", "J.K. Rolings")
library.add_book(book)
