from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Tytuł')
root.geometry("400x400")  # rozmiar okienka

# UWAGA slider nazywa się Scale
vertical = Scale(root, from_=0, to=200)  # zakres wartości od do
vertical.pack()  # ważne żeby pack() w osobnej linii


def slide(event):  # jak jest funkcją od slidera to musi być tu jakiś parametr
    my_label = Label(root, text=horizontal.get()).pack()
    root.geometry(str(horizontal.get()) + "x400")


horizontal = Scale(root, from_=0, to=400, orient=HORIZONTAL, command=slide)  # poziomy slider
horizontal.pack()

my_label = Label(root, text=horizontal.get()).pack()  # przyjmuje wartość slidera

my_btn = Button(root, text="Kliknij", command=slide).pack()

root.mainloop()
