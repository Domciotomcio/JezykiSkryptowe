from tkinter import *

root = Tk()  # root, nasz główny widget

myLabel = Label(root, text="Hello World!")  # prosta etykieta w widgecie root, z tekstem Hello World!

myLabel.pack()  # spakuj, czy włóż nasz widget (myLabel) do głównego widgeta w którym jest (root)

root.mainloop()  # nasz program musi działać w pętli
