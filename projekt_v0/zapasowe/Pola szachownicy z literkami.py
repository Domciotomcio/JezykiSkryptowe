from tkinter import *
import string

letters_dic = {
  0: 'a',
  1: 'b',
  2: 'c',
  3: 'd',
  4: 'e',
  5: 'f',
  6: 'g',
  7: 'h',
}

class GUI:
    def __init__(self):
        # basic root frame configuration
        self.root = Tk()
        self.root.title('ChessGo')
        self.root.geometry("800x800")

        # ramka szachownicy
        self.frame = LabelFrame(self.root, text="Chess Board", labelanchor=N, borderwidth=10)

        self.chessboard_size = 8
        self.poles_list = []

        for i in range(0, 8):  # rows
            for j in range(0, 8):  # columns
                if i % 2 == j % 2:
                    self.poles_list.append(Label(self.frame, text=letters_dic[j] + str(8-i), width=5, height=2, bg="brown"))
                else:
                    self.poles_list.append(Label(self.frame, text=letters_dic[j] + str(8-i), width=5, height=2, bg="yellow"))
                self.poles_list[j + i*8].grid(row=i, column=j)


        self.frame.pack()

        self.root.mainloop()

    def create_chessboard(self):
        pass

    def funkcja1(self):
        print("cos")





if __name__ == "__main__":
    gui = GUI()

