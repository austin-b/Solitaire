from random import shuffle

class Value:

    value_range = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']

    def __init__(self, value):
        if value in self.value_range:
            self.value = value
        else:
            raise ValueError

    def __repr__(self):
        return str(self.value)

    def __str__(self):
        return str(self.value)

    def __add__(self, number):
        return Value(self.value_range[self.value_range.index(self.value) + number])

    def __sub__(self, number):
        return Value(self.value_range[self.value_range.index(self.value) - number])

    def __eq__(self, other):
        if type(other) == str:
            return str(self.value) == other
        if type(other) == int:
            return self.value == other
        else:
            return self.value == other.value
        
class Card:

    def __init__(self, color, suit, value, image="", hidden=True, screen_location=None):
        self.color = color
        self.suit = suit
        self.value = Value(value)
        self.image = image
        self.hidden = hidden
        self.screen_location = screen_location

    def __repr__(self):
        return "Card(" + self.color + ", " + self.suit + ", " + str(self.value) + ")"

class Deck:

    cards = []

    def __init__(self):
        for s in ["Diamonds", "Spades", "Hearts", "Clubs"]:
            for v in ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']:
                if s in ["Diamonds", "Hearts"]:
                    color = "red"
                elif s in ["Spades", "Clubs"]:
                    color = "black"
                self.cards.append(Card(color,s,Value(v)))

    def shuffle(self):
        shuffle(self.cards)

    def draw(self):
        return self.cards.pop(0)

if __name__ == '__main__':                
    deck = Deck()

    deck.shuffle()

    for c in deck.cards:
        print(c)
