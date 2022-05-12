from tkinter import *
from PIL import ImageTk, Image # do obrazów


root = Tk()

root.title("Obrazkowa aplikacja")  # tytuł okienka
root.iconphoto(False, PhotoImage(file="icons8-batman-logo-30.png"))  # False, czyli nie standardowe, a potem fota

my_img = ImageTk.PhotoImage(Image.open("batman_photo.jpg"))  # obrazek klasy PhotoImage
my_label = Label(image=my_img)  # bierze obrazek klasy ImageTk.PhotoImage
my_label.pack()

button_quit = Button(root, text="Wyjdź", bg="red", command=root.quit)  # przycisk do wyłączania, np dodałem czerwony kolor
button_quit.pack()

root.mainloop()