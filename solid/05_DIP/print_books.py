class Book:
    def __init__(self, author, title,content: str):
        self.author = author
        self.title = title
        self.content = content


class Formatter:
    def format(self, book: Book) -> str:
        return book.content
class PrintFlayer:
    def format(self, book: Book) -> str:
        return f"---------\n{book.author}\n---------\n{book.title}---------"

class Printer:
    # def __init__(self,formatter):
    #     self.formatter = formatter

    def get_book(self, book: Book,formatter):

        formatted_book = formatter.format(book)
        return formatted_book


book1  = Book("Author1","Title1","Content1")
