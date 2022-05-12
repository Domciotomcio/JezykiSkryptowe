from tkinter import *

root = Tk()  # root, nasz główny widget


def when_button_pressed():  # nazwa funkcji dowolna, ale ta jest spoko
    my_label = Label(root, text="Kliknięto przycisk")
    my_label.pack()
    

myButton1 = Button(root, text="Naciśnik mnie")
myButton2 = Button(root, text="Naciśnik mnie", state=DISABLED)  # nieaktywny
myButton3 = Button(root, text="Naciśnik mnie", padx=30, pady=20)  # wymiary przycisku
myButton4 = Button(root, text="Naciśnik mnie", command=when_button_pressed)  # akcja, UWAGA nazwa funkcji bez nawiasu
myButton5 = Button(root, text="Naciśnik mnie", fg="blue", bg="#BCD6FF")  # zmiana koloru, czcionka, tło, moża hex

myButton1.pack()
myButton2.pack()
myButton3.pack()
myButton4.pack()
myButton5.pack()

root.mainloop()  # nasz program musi działać w pętli
