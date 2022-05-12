from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Tytuł')
root.iconphoto(False, PhotoImage(file="icons8-batman-logo-30.png"))

frame = LabelFrame(root, text="This is my Frame...", padx=30, pady=30)
frame = LabelFrame(root, padx=30, pady=30)  # ramka bez nazwy
frame.pack(padx=10, pady=10)
# pierwszy pady dotyczą samej ramki w środku, drugie miejsca na zewnątrz niej

# przykład, że frame jest pack() w roocie, ale już przyciski są w grid() w ramce
b1 = Button(frame, text="Nie ruszaj tego")  # ten przycisk jest w ramce frame
b2 = Button(frame, text="przycisk 2")
b1.grid(row=0, column=0)
b2.grid(row=1, column=1)

root.mainloop()
