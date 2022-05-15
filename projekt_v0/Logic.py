from Piece import *

DIC_LETTERS = {
    0: 'a',
    1: 'b',
    2: 'c',
    3: 'd',
    4: 'e',
    5: 'f',
    6: 'g',
    7: 'h',
}

class Square:
    def __init__(self, number):
        self.number = number  # number of square
        self.piece = None  # the piece on the square
        self.border_squares = []
        pass

    def __str__(self):
        return "Pole nr: {0}, figura: {1}".format(self.number, self.piece)

    def short_str(self):
        if self.piece is None:
            return "{:02d}".format(self.number)
        else:
            return self.piece.short_name


class Chessboard:
    def __init__(self):
        self.chessboard = []

    def create_chessboard(self):
        for i in range(0, 8):
            for j in range(0, 8):
                self.chessboard.append(Square(j + i * 8))

    def print_chessboard_num(self):
        for i in range(0, 8):
            for j in range(0, 8):
                print("{:02d}".format(self.chessboard[j + i * 8].number), end=" ")
            print()

    def print_chessboard_pieces(self):
        print("----------------------------")
        for i in range(0, 8):
            print("|", end=" ")
            for j in range(0, 8):
                print(self.chessboard[j + i * 8].short_str(), end=" ")
            print("|")
        print("----------------------------")

    def add_piece(self, piece, square):  # square in chess names, a6, b4, c7
        # translate square name to number
        a = ord(square[0]) - 97

        # square[1] starts from 1, so -1, and is a column, so * 8
        square_num = a + (int(square[1]) - 1) * 8
        print("squqre_num = ", square_num)

        self.chessboard[square_num].piece = piece

        print(f"dodano {piece} na pole {square}")

    def default_set_pieces(self):
        self.add_piece(King(True), 'e1')
        self.add_piece(King(False), 'e8')

        # set pawns
        for i in range(0, 8):
            self.add_piece(Pawn(True), chr(97 + i) + str(2))  # white pawns
            self.add_piece(Pawn(False), chr(97 + i) + str(7))  # black pawns

    def move(self, act_pos, pot_pos):
        # you cannot move figure from empty square
        if self.chessboard[act_pos].piece is None:
            print("No piece on act_pos = ", act_pos)
            return False

        # get list of possible moves
        pot_moves = self.chessboard[act_pos].piece.get_pot_moves(act_pos)
        is_move_legit = True

        # check if pot_pos is available
        # check if on pot_pos is not your piece
        if self.chessboard[pot_pos].piece is not None and \
                self.chessboard[pot_pos].piece.color == self.chessboard[act_pos].piece.color:
            is_move_legit = False

        # check if in pot_moves
        if pot_pos not in pot_moves:
            is_move_legit = False

        # move
        if is_move_legit:
            self.chessboard[pot_pos].piece = self.chessboard[act_pos].piece
            self.chessboard[act_pos].piece = None
            return True
        else:
            print(f"Illegal Move from {act_pos} to {pot_pos}")
            return False

    def create_border_squares_lists(self):
        # corner squares
        self.chessboard[0].border_squares = [1, 8, 9]
        self.chessboard[7].border_squares = [6, 14, 15]
        self.chessboard[56].border_squares = [48, 49, 57]
        self.chessboard[63].border_squares = [54, 55, 62]

        # border squares
        for i in range(1, 7):  # first row
            self.chessboard[i].border_squares = [i + 7, i + 8, i + 9]

        for i in range(1, 7):  # last row
            self.chessboard[i + 56].border_squares = [i - 9, i - 8, i - 7]

        for i in range(1, 7):  # first column
            self.chessboard[i * 8].border_squares = [i - 7, i + 1, i + 9]

        for i in range(1, 7):  # last row
            self.chessboard[i * 8 + 7].border_squares = [i - 9, i - 1, i + 7]

        # all squares inside border with other squares arround
        for i in range(1, 7):
            for j in range(1, 7):
                pos = j + i * 8
                self.chessboard[pos].border_squares = [pos-9, pos-8, pos-7,
                                                       pos-1,        pos+1,
                                                       pos+7, pos+8, pos+9]

    def pot_rook_moves(self, act_pos):
        legit_moves = []

        # find legit moves to the right
        can_search = True
        while can_search:
            if

        return legit_moves

    

    def testowe(self):
        self.chessboard[0].piece = King(True)


if __name__ == "__main__":
    chessboard = Chessboard()
    chessboard.create_chessboard()
    chessboard.create_border_squares_lists()

    chessboard.default_set_pieces()
    chessboard.print_chessboard_pieces()
    chessboard.move(5, 6)
    print()
    chessboard.print_chessboard_pieces()
    chessboard.print_chessboard_num()
