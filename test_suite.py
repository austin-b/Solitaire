import unittest
from deck import *
from board import Board

class TestValue(unittest.TestCase):

    def setUp(self):
        self.test_value = Value(5)

    def test_value_error(self):
        with self.assertRaises(ValueError):
            Value(98)
        with self.assertRaises(ValueError):
            Value('a')

    def test_string_representation(self):
        self.assertEqual(str(self.test_value),'5')
        self.assertEqual(str(Value('K')), 'K')

    def test_add(self):
        self.assertEqual(self.test_value+1, Value(6))
        with self.assertRaises(IndexError):
            self.test_value+19

    def test_subtract(self):
        self.assertEqual(self.test_value-1, Value(4))
        with self.assertRaises(IndexError):
            self.test_value - 19

    def test_equal(self):
        self.assertTrue(self.test_value == 5)
        self.assertTrue(self.test_value == "5")
        self.assertTrue(self.test_value == Value(5))
        self.assertTrue(Value('K') == 'K')
        self.assertFalse(self.test_value == 4)
        self.assertFalse(Value('K') == 'k')
        self.assertFalse(self.test_value == Value(7))

class TestValueContinuous(unittest.TestCase):

    def setUp(self):
        self.test_value = ValueContinuous(5)

    def test_add(self):
        self.assertEqual(self.test_value+14, ValueContinuous(6))
        self.assertEqual(self.test_value+34, ValueContinuous('K'))

    def test_subtract(self):
        self.assertEqual(self.test_value-14, ValueContinuous(4))

class TestCard(unittest.TestCase):

    def setUp(self):
        self.test_card = Card("black", "Spades", 'Q')

    def test_card_string(self):
        self.assertEqual(str(self.test_card), "Card(black, Spades, Q, location: None)")

    def test_invalid_color(self):
        with self.assertRaises(ValueError):
            Card("green", "Spades", 'Q')
    
    def test_invalid_suit(self):
        with self.assertRaises(ValueError):
            Card("black", "apple", 'Q')

    def test_invalid_value(self):
        with self.assertRaises(ValueError):
            Card("black", "Spades", 17)

    def test_equality(self):
        self.assertTrue(self.test_card == Card("black", "Spades", 'Q'))

class TestDeck(unittest.TestCase):

    def setUp(self):
        self.test_deck = Deck()

    def test_card_counts(self):
        self.assertEqual(len(self.test_deck.cards), 52) 
        self.assertEqual(len([1 for c in self.test_deck.cards if c.suit == "Diamonds"]), 13)
        self.assertEqual(len([1 for c in self.test_deck.cards if c.suit == "Spades"]), 13)
        self.assertEqual(len([1 for c in self.test_deck.cards if c.suit == "Hearts"]), 13)
        self.assertEqual(len([1 for c in self.test_deck.cards if c.suit == "Clubs"]), 13)

        self.assertEqual(len([1 for c in self.test_deck.cards if c.value == 'A']), 4)
        self.assertEqual(len([1 for c in self.test_deck.cards if c.value == 2]), 4)
        self.assertEqual(len([1 for c in self.test_deck.cards if c.value == 3]), 4)
        self.assertEqual(len([1 for c in self.test_deck.cards if c.value == 4]), 4)
        self.assertEqual(len([1 for c in self.test_deck.cards if c.value == 5]), 4)
        self.assertEqual(len([1 for c in self.test_deck.cards if c.value == 6]), 4)
        self.assertEqual(len([1 for c in self.test_deck.cards if c.value == 7]), 4)
        self.assertEqual(len([1 for c in self.test_deck.cards if c.value == 8]), 4)
        self.assertEqual(len([1 for c in self.test_deck.cards if c.value == 9]), 4)
        self.assertEqual(len([1 for c in self.test_deck.cards if c.value == 10]), 4)
        self.assertEqual(len([1 for c in self.test_deck.cards if c.value == 'J']), 4)
        self.assertEqual(len([1 for c in self.test_deck.cards if c.value == 'Q']), 4)
        self.assertEqual(len([1 for c in self.test_deck.cards if c.value == 'K']), 4)
        
    def test_deck_draw(self):
        test_pop = self.test_deck.draw()
        self.assertFalse(test_pop in self.test_deck.cards)

class TestBoard(unittest.TestCase):

    def setUp(self):
        self.board = Board()

    def test_initial_board_layout(self):
        self.assertEqual(len(self.board.rows[0]), 1)
        self.assertEqual(len(self.board.rows[1]), 2)
        self.assertEqual(len(self.board.rows[2]), 3)
        self.assertEqual(len(self.board.rows[3]), 4)
        self.assertEqual(len(self.board.rows[4]), 5)
        self.assertEqual(len(self.board.rows[5]), 6)
        self.assertEqual(len(self.board.rows[6]), 7)

        self.assertEqual(len(self.board.spare_hidden), 24)

        # ensure only last card in row is unhidden
        for r in self.board.rows:
            for c in r:
                if c == r[-1]:
                    self.assertFalse(c.hidden)
                else:
                    self.assertTrue(c.hidden)

    # TODO: will need to know the 'mock' sublibrary
    def test_move_card_from_playing_row_to_playing_row(self):
        pass

    def test_move_card_from_playing_row_to_completed_row(self):
        pass

    def test_move_bundle_of_cards(self):
        pass

    def test_move_spare_hidden_to_shown(self):
        pass

    def test_move_spare_shown_to_playing_row(self):
        pass

    def test_move_spare_shown_to_completed_row(self):
        pass

    def test_validate_win_condition(self):
        pass

if __name__ == '__main__':
    unittest.main(verbosity=3)