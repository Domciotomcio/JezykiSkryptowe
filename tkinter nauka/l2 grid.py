from tkinter import *

root = Tk()  # root, nasz główny widget

myLabel1 = Label(root, text="Hello World!")  # prosta etykieta w widgecie root, z tekstem Hello World!
myLabel2 = Label(root, text="Tu DomcioTomcio!")

# ustawiam w siatce, w rzędzie row i kolumnie column
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=5)  # samo się dostosuje, nawet jak jest 5 to zrobi column=1

# opcjonalnie można wrzucać tak
myLabel1 = Label(root, text="Hello World!").grid(row=0, column=0)
myLabel2 = Label(root, text="Tu DomcioTomcio!").grid(row=1, column=5)

root.mainloop()  # nasz program musi działać w pętli
