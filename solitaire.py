from board import Board
from deck import Value

if __name__ == '__main__':
    board = Board()

    board.show_board()

    # hacky but it works for the moment -- only playing rows
    def find_card(txt):
        suit = ""
        if txt[0] == "D":
            suit = "Diamonds"
        elif txt[0] == "H":
            suit = "Hearts"
        elif txt[0] == "S":
            suit = "Spades"
        elif txt[0] == "C":
            suit = "Clubs"
        value = Value(txt[1])
        for r in board.rows:
            for c in r:
                if c.suit == suit and c.value == value and c.hidden == False:
                    return c

    chosen_card = find_card(input("Which card do you want to move (EX: DQ for Queen of Diamonds): "))

    to_row = eval(input("Move card to (1-7):"))

    board.move_card(chosen_card, board.rows[to_row-1])

    board.show_board()