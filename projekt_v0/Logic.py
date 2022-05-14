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
            for j in range(1, 9):
                self.chessboard.append(Square(j + i * 8))

    def print_chessboard_num(self):
        for i in range(0, 8):
            for j in range(0, 8):
                print("{:02d}".format(self.chessboard[j + i * 8].number), end=" ")
            print()

    def print_chessboard_pieces(self):
        for i in range(0, 8):
            for j in range(0, 8):
                print(self.chessboard[j + i * 8].short_str(), end=" ")
            print()

    def add_piece(self, piece, square):  # square in chess names, a6, b4, c7
        # translate square name to number
        a = ord(square[0]) - 97

        # square[1] starts from 1, so -1, and is a column, so * 8
        square_num = a + (int(square[1])-1) * 8
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



    def testowe(self):
        self.chessboard[0].piece = King(True)



if __name__ == "__main__":
    chessboard = Chessboard()
    chessboard.create_chessboard()

    chessboard.print_chessboard_num()

    king = King(False)
    print(king.short_name)


    #chessboard.testowe()

    #chessboard.print_chessboard_pieces()
    chessboard.default_set_pieces()
    chessboard.print_chessboard_pieces()
