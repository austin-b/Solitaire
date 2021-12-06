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

# Variation on Value that can be used in a game where the card
# values are continuous -- an Ace can be put on a King
class ValueContinuous(Value):

    def __add__(self, value):
        remainder = value % len(self.value_range)
        return super().__add__(remainder)

    def __sub__(self, value):
        remainder = value % len(self.value_range)
        return super().__sub__(remainder)

class Card:

    def __init__(self, color, suit, value, image="", hidden=True, location=None):
        self.color = self.sanitize_color(color)
        self.suit = self.sanitize_suit(suit)
        self.value = Value(value)
        self.image = image
        self.hidden = hidden
        self.location = location

    def sanitize_color(self, color):
        if color.lower() == "black" or color.lower() == "red":
            return color.lower()
        else: raise ValueError("Invalid color: black or red only")
    
    def sanitize_suit(self, suit):
        if suit.capitalize() == "Diamonds" or suit.capitalize() == "Hearts" and self.color == "red":
            return suit.capitalize()
        elif suit.capitalize() == "Spades" or suit.capitalize() == "Clubs" and self.color == "black":
            return suit.capitalize()
        else: raise ValueError("Suit can only be Diamonds, Hearts, Spades, or Clubs.")

    def __repr__(self):
        return "Card(" + self.color + ", " + self.suit + ", " + str(self.value) + ", location: " + str(self.location) + ")"

    def __eq__(self, other):
        if self.value == other.value and self.suit == other.suit:
            return True
        else: return False

    def __lt__(self, other):
        if self.value < other.value:
            return True
        else: return False

    def __gt__(self, other):
        if self.value > other.value:
            return True
        else: return False

class Deck:

    def __init__(self, continuous=False):
        self.cards = []
        for s in ["Diamonds", "Spades", "Hearts", "Clubs"]:
            for v in ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']:
                if s in ["Diamonds", "Hearts"]:
                    color = "red"
                elif s in ["Spades", "Clubs"]:
                    color = "black"

                if continuous:
                    self.cards.append(Card(color,s,ValueContinuous(v)))
                else: 
                    self.cards.append(Card(color,s,Value(v)))

    def shuffle(self):
        shuffle(self.cards)

    def draw(self):
        return self.cards.pop(0)

if __name__ == '__main__':                
    from test_suite import TestValue, TestValueContinuous, TestCard, TestDeck
    import unittest

    unittest.main(verbosity=3)
