from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Tytuł')

# showinfo, showwarning, showerror, askquestion, askokcancel, askyesno


def popup():
    # wyświetla po prostu okienko z naszą wiadomością
    response = messagebox.askyesno("This is my Popup!", "Hello World") # tytuł i treść wiadomości
    # Label(root, text=response).pack() # tekstem jest response, nasza odpowiedz, Yes - 1, No - 0
    if response == 1:
        Label(root, text="You clicked YES").pack()
    else:
        Label(root, text="You clicked NO").pack()
    # askokcancel, ok - 1, cancel - 0
    # askquestion, yes - "yes", no - "no" czyli zwraca string
    # showerror zwraca "ok" ???
    # showwarning zwraca "ok"
    # showinfo zwraca "ok"


Button(root, text="Popup", command=popup).pack()

mainloop()
