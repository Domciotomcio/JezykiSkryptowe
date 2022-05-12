from tkinter import *
from PIL import ImageTk, Image  # do obrazów
from tkinter import filedialog

root = Tk()
root.title('Tytuł')
root.iconphoto(False, PhotoImage(file="icons8-batman-logo-30.png"))  # False, czyli nie standardowe, a potem fota


def open():
    global my_image # pamiętaj, python wywala zawartość ImageTk.PhotoImage jeśli nie jest global
    root.filename = filedialog.askopenfilename(initialdir="", title="Select a File",
                                               filetypes=(("png files", "*.png"), ("all files", "*.*")))
    # po włączeniu od razu otwiera okno do wybrania pliku
    # initialdir to domyślna lokalizacja do otwarcia
    # filetypes to to co wybierasz na dole w okienku rodzaj pliku,
    # pierwsza część krotki to nazwa, a druga to co faktycznie komp pozwoli otworzyć
    # zwraca ścieżkę pliku

    myLabel = Label(root, text=root.filename).pack()  # etykieta z ścieżką pliku

    # wyświetlenie obrazka o otrzymanej ścieżce
    my_image = ImageTk.PhotoImage(Image.open(root.filename))
    my_image_label = Label(root, image=my_image).pack()


my_btn = Button(root, text="Open File", command=open).pack()

mainloop()
