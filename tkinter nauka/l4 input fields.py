from tkinter import *

root = Tk()

# pole do wpisywania o szerokości 50, kolor tła cyjan, kolor czcionki biały i obwódka tekstu na 5 px
e = Entry(root, width=50, bg="cyan", fg='white', borderwidth=5)
e.pack()
e.get() # zwraca zawartość e, czyli stringa
e.insert(0, "Podaj imie")


def when_button_pressed():  # nazwa funkcji dowolna, ale ta jest spoko
    my_label = Label(root, text="Hello " + e.get())  # tworzy etykietę w roocie z tekstem np "Hello John"
    my_label.pack()


myButton = Button(root, text="Podaj imie", command=when_button_pressed)
myButton.pack()

root.mainloop()