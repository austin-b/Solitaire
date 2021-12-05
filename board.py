from deck import *

class Board:

    # to determine win condition
    amount_hidden_in_rows = 0

    # top row of finished cards
    diamonds_completed = []
    spades_completed = []
    hearts_completed = []
    clubs_completed = []

    # spare deck
    spare_shown = []
    spare_hidden = []

    # rows
    rows = []

    def __init__(self):
        deck = Deck()

        deck.shuffle()

        for i in range(7):
            temp_list = []
            for j in range(i+1):
                card = deck.draw()
                card.location = i
                temp_list.append(card)
            self.rows.append(temp_list)

        for r in self.rows:
            r[-1].hidden = False

        for c in deck.cards:
            c.location = "spare_hidden"
            self.spare_hidden.append(c)

    def check_rows_for_reveal(self):
        for row in self.rows:
            if len(row) > 0:
                row[-1].hidden = False

    def validate_playing_row_move(self, moving_card, dest_card):
        if moving_card.color != dest_card.color:
            if dest_card.value == (moving_card.value + 1):
                return True
            else: return False
        else: return False

    def validate_move(self, moving_card, dest_card):
        # playing row to playing row
        if 0 <= moving_card.location <= 6:
            return self.validate_playing_row_move(moving_card, dest_card)

        # playing row to completed

        # spare_hidden to spare_shown


    # change location of moved card
    def move_card(self, card, dest):
        if self.validate_move(card, dest[-1]):
            dest.append(card)
            self.check_rows_for_reveal()

    # TODO
    def check_win(self):
        pass

    def print_single_show_row(self, row):
        if len(row) > 0:
            return str(row[-1])
        else:
            return "Empty"

    def print_play_row(self, row):
        hidden = 0
        temp_string = ""
        for c in row:
            if c.hidden:
                hidden += 1
            else:
                temp_string += str(c) + " "
        return "Hidden: " + str(hidden) + " Revealed: " + temp_string

    def show_board(self):
        print("Diamonds: " + self.print_single_show_row(self.diamonds_completed))
        print("Spades: " + self.print_single_show_row(self.spades_completed))
        print("Hearts: " + self.print_single_show_row(self.hearts_completed))
        print("Clubs: " + self.print_single_show_row(self.clubs_completed))

        print()
        print("Spares:")
        print("Shown: " + self.print_single_show_row(self.spare_shown))
        print("Hidden: length " + str(len(self.spare_hidden)))

        print()
        print("Row 1 -- " + self.print_play_row(self.rows[0]))
        print("Row 2 -- " + self.print_play_row(self.rows[1]))
        print("Row 3 -- " + self.print_play_row(self.rows[2]))
        print("Row 4 -- " + self.print_play_row(self.rows[3]))
        print("Row 5 -- " + self.print_play_row(self.rows[4]))
        print("Row 6 -- " + self.print_play_row(self.rows[5]))
        print("Row 7 -- " + self.print_play_row(self.rows[6]))

    
def board_test():
    board = Board()

    board.show_board()
        
def test():
    deck = Deck()

    print(len(deck.cards))

    deck.shuffle()

    for c in deck.cards:
        print(c)

    print(len(deck.cards))

if __name__ == "__main__":
    board_test()