#### 1
class CardDeck:
    def __init__(self):
        self.length = 52
        self.index = 0
        self.__SUITS = ["пикей", "бубен", "червей", "крест"]
        self.__RANKS = [*range(2, 11), "J", "Q", "K", "ace"]

    def __next__(self):
        if self.index >= self.length:
            raise StopIteration
        else:
            s = self.__SUITS[self.index // len(self.__RANKS)]
            r = self.__RANKS[self.index % len(self.__RANKS)]
            self.index += 1
            if r == "ace" and s == "пикей":  # это должно было случиться
                return f"\nyou know its gonna be\nthe ACE OF SPADES\n"
            else:
                return f"{r} {s}"

    def __iter__(self):
        return self


deck = CardDeck()
for card in deck:
    print(card)
####### 2
