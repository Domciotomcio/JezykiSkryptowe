from tkinter import *
from PIL import ImageTk, Image  # do obrazów

root = Tk()

root.title("Obrazkowa aplikacja")  # tytuł okienka
root.iconphoto(False, PhotoImage(file="icons8-batman-logo-30.png"))  # False, czyli nie standardowe, a potem fota

my_img1 = ImageTk.PhotoImage(Image.open("batman_photo.jpg"))
my_img2 = ImageTk.PhotoImage(Image.open("batman2.jpg"))
my_img3 = ImageTk.PhotoImage(Image.open("batman3.jpg"))

image_list = [my_img1, my_img2, my_img3]

my_label = Label(image=my_img1)  # bierze obrazek klasy ImageTk.PhotoImage
my_label.grid(row=0, column=0, columnspan=3)


def forward(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()  # my_label wylatuje z siatki
    my_label = Label(image=image_list[image_number - 1])
    my_label.grid(row=0, column=0, columnspan=3)  # przywracam z powrotem

    # trzeba jeszcze zmienić w guzikach aktualne numery obrazka
    # samemu zrobię sprytniej jedną zmienną
    button_forward = Button(root, text=">>", bg="yellow", command=lambda: forward(image_number + 1))
    button_back = Button(root, text="<<", bg="blue", command=lambda: forward(image_number - 1))

    if image_number == len(image_list):
        button_forward = Button(root, text=">>", bg="white", state=DISABLED)

    if image_number == 0:
        button_back = Button(root, text="<<", bg="white", state=DISABLED)

    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)

    status = Label(root, text="Image " + str(image_number) +
                              " of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W + E)
    # bd to szerokość ramki, relief to wygląd pola 3D, sunken to taki wklęsły, a
    # anchor to pozycja tekstu w widgecie, kierunki W i E to do lewej i prawej
    # sticky przykleja, do stron świata N, S, W, E, a że tu ma miejsce to rozciągnął


def back():
    return


button_back = Button(root, text="<<", bg="blue", command=lambda: back())
button_quit = Button(root, text="Wyjdź", bg="red", command=root.quit)
button_forward = Button(root, text=">>", bg="yellow", command=lambda: forward(2))

button_back.grid(row=1, column=0)
button_quit.grid(row=1, column=1)
button_forward.grid(row=1, column=2, pady=10)
# pady dodaje 10 px odległości, dzieki czemu ten wiersz jest oddzielony od etykiety na dole

status = Label(root, text="Image 1 of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
status.grid(row=2, column=0, columnspan=3, sticky=W + E)


root.mainloop()
