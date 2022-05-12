from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Tytuł')

r = IntVar()  # zmienna r, ale trochę inna tkinterowa, będzie na bieżąco aktualizowana
r.get()  # sposób na branie wartości tej zmiennej
r.set(2)  # sposób na przypisywanie wartości


def button_clicked(value):
    myLabel = Label(root, text=value)
    myLabel.pack()


# Radiobutton(root, text="Option 1", variable=r, value=1, command=lambda: clicked(r.get())).pack()
# Radiobutton(root, text="Option 2", variable=r, value=2, command=lambda: clicked(r.get())).pack()
# tutaj variable (czyli rodzaj np taki IntVar czyli jak int) musi się zgadzać z rodzajem value, czyli np liczby
# kliknięcie ustawia naszą zmienną r na wartość value i wywołuje funkcję w command, czyli naszą customową lambda
# która nie przyjmuje żadnych argumentów i wywołuje funkcję clicked z wartością r (za pomocą r.get())

MODES = [
    ("Pepperoni", "Pepperoni"),
    ("Cheese", "Cheese"),
    ("Mushroom", "Mushroom"),
    ("Onion", "Onion"),
]

pizza = StringVar()  # tkinterowa zmienna string
pizza.set("Pepperoni")

# sposób na zrobienie radiobattonów w pętli
for text, mode in MODES:
    Radiobutton(root, text=text, variable=pizza, value=mode).pack(anchor=W)
    # przycisk radiowy o tekscie tym pierwszym z pary, zmienia wartość zmiennej pizza na wartość mode
    # anchor przykleiło do lewej


myButton = Button(root, text="Kliknij Mnie!", command=lambda: button_clicked(pizza.get()))
# po kliknięciu wywoła funkcję clicked z wartością zmiennej pizza, czyli jakimś stringiem aktualnej pizzy
myButton.pack()

mainloop()
