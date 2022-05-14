from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Tytuł')
root.geometry("400x400")  # rozmiar okienka

# var = IntVar() # tylko liczba, więc zwróci w checkbutton 0 lub 1
var = StringVar() # może zwrócić jakieś stringi

c = Checkbutton(root, text="Check this box :)", variable=var, onvalue="Pizza", offvalue="Hamburger")
# zmienną którą zmieniamy, vartość jak zaznaczone i jak odznaczone
# np dla IntVar nie trzeba pisać wartości, on to 1, off to 0
c.deselect() # domyślnie odchacza
c.pack()


myLabel = Label(root, text=var.get()).pack()


def show():
    myLabel = Label(root, text=var.get()).pack()


myButton = Button(root, text="Show Selection", command=show).pack()

root.mainloop()
