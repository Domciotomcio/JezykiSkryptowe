from tkinter import *



class App:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        self.button = Button(
            frame, text='Zakończ', fg='red', command=frame.quit
        )

        self.button.pack(side=LEFT)
        self.hi_there = Button(frame, text="Cześć", command=self.witajcie)
        self.hi_there.pack(side=LEFT)

    def witajcie(self):
        print("Witajcie mili studenci")




if __name__ == "__main__":
    root = Tk()
    root.geometry("100x500+200+400")

    app = App(root)
    root.mainloop()
