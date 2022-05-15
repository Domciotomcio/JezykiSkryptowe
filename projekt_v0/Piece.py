DIC_FIGURES_NAMES = {
    0: 'wh_pawn',
    1: 'wh_knight',
    2: 'wh_bishop',
    3: 'wh_rook',
    4: 'wh_queen',
    5: 'wh_king',
    10: 'bl_pawn',
    11: 'bl_knight',
    12: 'bl_bishop',
    13: 'bl_rook',
    14: 'bl_queen',
    15: 'bl_king',

}

DIC_FIGURES_VALUES = {
    'pawn': 1,
    'knight': 3,
    'bishop': 3,
    'rook': 5,
    'queen': 9,
    'king': 100
}


class Piece:
    name = ""
    value = -1

    def __init__(self, color):
        self.color = color  # True - white, False - black
        self.short_name = "--"

    def __str__(self):
        return self.name

    def move(self, pos):
        return -1


class King(Piece):
    name = "King"
    value = 100

    def __init__(self, color):
        super().__init__(color)
        if color:
            self.short_name = "w" + King.name[0]
        else:
            self.short_name = "b" + King.name[0]

    def get_pot_moves(self, pos):
        legit_moves = [pos-9, pos-8, pos-7,
                       pos-1,        pos+1,
                       pos+7, pos+8, pos+9]

        return legit_moves


class Pawn(Piece):
    name = "Pawn"
    value = 1

    def __init__(self, color):
        super().__init__(color)
        if color:
            self.short_name = "w" + Pawn.name[0]
        else:
            self.short_name = "b" + Pawn.name[0]

    def get_pot_moves(self, pos):
        if self.color:  # white pawn
            if 8 <= pos <= 15:
                legit_moves = [pos + 8, pos + 16]
            else:
                legit_moves = [pos + 8]
        else:  # black pawn
            if 8 <= pos <= 15:
                legit_moves = [pos - 8, pos - 16]
            else:
                legit_moves = [pos + 8]
        return legit_moves

class Rook(Piece):
    name = "Rook"
    value = 1

    def __init__(self, color):
        super().__init__(color)
        if color:
            self.short_name = "w" + Rook.name[0]
        else:
            self.short_name = "b" + Rook.name[0]

    def get_pot_moves(self, pos):
        if self.color:  # white pawn
            if 8 <= pos <= 15:
                legit_moves = [pos + 8, pos + 16]
            else:
                legit_moves = [pos + 8]
        else:  # black pawn
            if 8 <= pos <= 15:
                legit_moves = [pos - 8, pos - 16]
            else:
                legit_moves = [pos + 8]
        return legit_moves
