###############  zadanie 1
class Publication:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def display(self):
        return f"{'Title:'.ljust(15)} {self.title}\n{'Author:'.ljust(15)} {self.author}\n{'Year:'.ljust(15)} {self.year}"


class Book(Publication):
    def __init__(self, title, author, year, isbn):
        super().__init__(title, author, year)
        self.isbn = isbn

    def display(self):
        return print(f"{super().display()}\n{'ISBN:'.ljust(15)} {self.isbn}")


class Magazin(Publication):
    def __init__(self, title, author, year, issue_number):
        self.issue_number = issue_number
        super().__init__(title, author, year)

    def display(self):
        return print(
            f"{super().display()}\n{'issue number:'.ljust(15)} {self.issue_number}"
        )


best_book = Book("The end of a beautiful era", "J.A.Brodskiy", "1977", "1-111-111-111")
magazin = Magazin("gippo sale!!!", "gippo", "2023", "№3")

best_book.display()
print()
magazin.display()
print("*" * 50)


####### zadanie 2
class Bankaccount:
    def __init__(self, __balance, __interest_rate, __transactions=None):
        self.__balance = __balance
        self.__interest_rate = __interest_rate
        self.__transactions = []

    def deposit(self, add_money):
        self.__balance += add_money
        self.__transactions.append(f"added to balance {add_money}$")

    def withdraw(self, withdraw_money):
        self.__balance -= withdraw_money
        self.__transactions.append(f"withdraw from balance{withdraw_money}$")

    def add_interest(self):
        self.__balance += self.__balance * (self.__interest_rate / 100)
        self.__transactions.append(
            f"added {self.__interest_rate} %"
            f"of the amount {self.__balance * (self.__interest_rate / 100)}$")

    def history(self):
        return print(*self.__transactions, sep="\n")


account = Bankaccount(15000, 20)
print(account._Bankaccount__balance)
account.add_interest()
account.deposit(1500)
account.deposit(5500)
account.withdraw(2000)
account.deposit(500)
account.deposit(4500)
account.history()  ## 15k+20%(3k)+7k-2k+05k-4.5k//28k
print(account._Bankaccount__balance)
