from tkinter import *
from PIL import ImageTk, Image  # do obrazów

root = Tk()
root.title('Tytuł')
root.iconphoto(False, PhotoImage(file="icons8-batman-logo-30.png"))  # False, czyli nie standardowe, a potem fota


def open():
    global my_img # bez tego python jakos dziwnie uwaza my_img za smiec i go czysci
    top = Toplevel()  # tworzy nowe okno na wierzchu
    top.title('PodTytuł')
    top.iconphoto(False, PhotoImage(file="icons8-batman-logo-30.png"))  # False, czyli nie standardowe, a potem fota
    my_img = ImageTk.PhotoImage(Image.open("batman3.jpg"))
    lbl = Label(top, text="Hello World", image=my_img).pack()  # wrzucamy w topa, czyli nasze nowe okno
    # co ciekawe, nie wyświetliło teraz tekstu

    btn2 = Button(top, text="close window", command=top.destroy).pack() #destroy niszczy tylko to otwarte okno


btn = Button(root, text="Open Second Window", command=open).pack()

mainloop()
