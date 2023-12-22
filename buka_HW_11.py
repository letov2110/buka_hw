###############  zadanie 1
class Publication:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def display(self):
        return f"Title: {self.title}\nAuthor: {self.author}\nYear: {self.year}"


class Book(Publication):
    def __init__(self, title, author, year, isbn):
        super().__init__(title, author, year)
        self.isbn = isbn

    def display(self):
        return print(f"{super().display()}\nISBN: {self.isbn}")


class Magazin(Publication):
    def __init__(self, title, author, year, issue_number):
        self.issue_number = issue_number
        super().__init__(title, author, year)

    def display(self):
        return print(f"{super().display()}\nissue number: {self.issue_number}")


best_book = Book("The end of a beautiful era", "J.A.Brodskiy", "1977", "1-111-111-111")
magazin = Magazin("gippo price", "gippo", "2023", "№3")
best_book.display()
magazin.display()

####### zadanie 2
