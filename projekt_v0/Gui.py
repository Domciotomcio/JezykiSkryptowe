from tkinter import *
from PIL import ImageTk, Image

dic_letters = {
  0: 'a',
  1: 'b',
  2: 'c',
  3: 'd',
  4: 'e',
  5: 'f',
  6: 'g',
  7: 'h',
}

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


class GUI:
    def __init__(self):
        # basic root frame configuration
        self.root = Tk()
        self.root.title('ChessGo')
        self.root.geometry("800x800")

        # chessboard
        self.chb_frame = LabelFrame(self.root, text="Chess Board", labelanchor=N, borderwidth=10)  # chessboard frame

        self.chessboard_size = 8
        self.poles_list = []
        my_img = ImageTk.PhotoImage(Image.open("figures/batman.png"))  # obrazek klasy PhotoImage

        for i in range(0, 8):  # rows
            for j in range(0, 8):  # columns
                # self.poles_list.append(Label(self.chb_frame, text=j + i * 8, width=5, height=2, bg="yellow"))
                if i % 2 == j % 2:
                    self.poles_list.append(Label(self.chb_frame, text=j + i * 8, width=5, height=2, bg="brown"))
                else:
                    self.poles_list.append(Label(self.chb_frame, text=j + i * 8, width=5, height=2, bg="yellow"))
                self.poles_list[j + i*8].grid(row=7 - i, column=j)

        self.chb_frame.grid(row=0, column=0, padx=10, pady=10)
        # end chessboard

        # figures on chessboard
        self.figure1 = Button(self.chb_frame, text=DIC_FIGURES_NAMES[0], width=5, height=2, bg="blue", bd=0)
        self.figure1.grid(row=0, column=0)



        # right side buttons
        self.panel_frame = LabelFrame(self.root, text="Menu")
        self.button1 = Button(self.panel_frame, text="button1").pack()
        self.button2 = Button(self.panel_frame, text="button2").pack()
        self.button3 = Button(self.panel_frame, text="button3").pack()

        # my_img = ImageTk.PhotoImage(Image.open("figures/batman.png"))  # obrazek klasy PhotoImage
        my_label = Label(self.panel_frame, image=my_img)  # bierze obrazek klasy ImageTk.PhotoImage
        my_label.pack()

        self.panel_frame.grid(row=0, column=1, padx=10, pady=10)
        # end right side buttons

        self.root.mainloop()

    def create_chessboard(self):
        pass

    def funkcja1(self):
        print("cos")





if __name__ == "__main__":
    gui = GUI()

