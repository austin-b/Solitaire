import unittest
from deck import *

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

class TestCard(unittest.TestCase):
    def setUp(self):
        self.test_card = Card("black", "Spades", 'Q')

    def test_card_string(self):
        self.assertEqual(str(self.test_card), "Card(black, Spades, Q, location: None)")

    

if __name__ == '__main__':
    unittest.main(verbosity=3)