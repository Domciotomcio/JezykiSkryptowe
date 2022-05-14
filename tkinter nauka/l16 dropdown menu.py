from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Tytuł')
root.geometry("400x400")  # rozmiar okienka

clicked = StringVar()
clicked.set("Monday")

options = [
    "Monday",
    "Tuesday",
    "Wendesday"
]

drop = OptionMenu(root, clicked, *options) # gwiazdka oznacza, że dajemy wiele wiele takich argumentów (np w postaci listy)
drop.pack()


def show():
    myLabel = Label(root, text=clicked.get()).pack()


myButton = Button(root, text="Show Selection", command=show).pack()

root.mainloop()
