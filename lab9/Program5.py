from tkinter import *

root = Tk()
frame = Frame(root)
frame.pack()
sam_dol = StringVar()
zmianaVideo = IntVar()


# musi być wcześniej, w klasie jest to zbyteczne
def zmiana():
    print(zmianaMuster.get())
    sam_dol.set(zmianaMuster.get())
    zmianaVideo.set(zmianaMuster.get())


zmianaMuster = IntVar()
c1 = Checkbutton(frame, text="Muster", variable=zmianaMuster, onvalue=11, offvalue=12, height=7, width=20,
                 command=zmiana)
c2 = Checkbutton(frame, text="Slave", variable=zmianaVideo, onvalue=12, offvalue=11, height=1, width=20)
pokazDol = Label(frame, textvar=sam_dol, relief=SUNKEN)
c1.pack()
c2.pack()
pokazDol.pack()
root.mainloop()
