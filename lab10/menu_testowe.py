from tkinter import *


def donothing():
    filewin = Toplevel(root)  # tworzy nowe okno na wierzchu
    button = Button(filewin, text="Do nothing button")
    button.pack()


root = Tk()

menubar = Menu(root)  # stwórz menubar

# pierwsza rozwijana lista File
filemenu = Menu(menubar, tearoff=0)  # to są kolejne pozycje listy
filemenu.add_command(label="New", command=donothing)
filemenu.add_command(label="Open", command=donothing)
filemenu.add_command(label="Save", command=donothing)
filemenu.add_command(label="Save as...", command=donothing)
filemenu.add_command(label="Close", command=donothing)
filemenu.add_separator()  # linia rozdzielająca kolejne pozycje
filemenu.add_command(label="Exit", command=root.quit)  # exit wychodzi z aplikacji
menubar.add_cascade(label="File", menu=filemenu)  # dopiero ta linia dodaje filemenu do paska menu

# pierwsza rozwijana lista Edit, itd
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Undo", command=donothing)
editmenu.add_separator()
editmenu.add_command(label="Cut", command=donothing)
editmenu.add_command(label="Copy", command=donothing)
editmenu.add_command(label="Paste", command=donothing)
editmenu.add_command(label="Delete", command=donothing)
editmenu.add_command(label="Select All", command=donothing)
menubar.add_cascade(label="Edit", menu=editmenu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index", command=donothing)
helpmenu.add_command(label="About...", command=donothing)
menubar.add_cascade(label="Help", menu=helpmenu)
root.config(menu=menubar)  # Ważna Linia!!! w roocie trzeba ustawic menu=menubar, czyli obiekt klasy Menu
root.mainloop()
