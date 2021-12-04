from board import Board

if __name__ == '__main__':
    board = Board()

    board.show_board()

    from_row = eval(input("Move card from (1-7):"))

    to_row = eval(input("Move card to (1-7):"))

    board.move_card(board.rows[from_row-1], board.rows[to_row-1])

    board.show_board()