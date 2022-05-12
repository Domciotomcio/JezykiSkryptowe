from tkinter import *

root = Tk()

root.title("Prosty kalkulator")  # tytuł okienka

e = Entry(root, width=35, borderwidth=4)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


# columnspan oznacza, że zajmie 3 pola kolumny (od wartosci column), pad to wymiary
# with i pad ładnie zrobiły białe pole do wpisywania o szerokości width, a cale e zajmuje wymiary padow



def button_click(number):
    current = e.get()  # pobiera aktualną wartość e
    e.delete(0, END)  # usuwa wszystko, od indexu 0 do końca
    e.insert(0, str(current) + str(number))  # dodaje na początku (indeksie 0) stringa z current i naszej number
    return


def button_add():
    first_number = e.get()
    global f_num
    f_num = int(first_number)
    e.delete(0, END)

def button_equal():
    second_number = e.get()
    e.delete(0, END)
    e.insert(0, f_num + int(second_number))

def button_clear():
    e.delete(0, END)


# stworzenie przycisków cyfr
button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))

# lambda jako funkcja,       lambda arguments : expression
# np x = lambda a, b : a * b
# u nas lambda nie dostaje argumentów, a realizuje funkcję button_click()
# wszystko dlatego, że nie możemy podawać funkcji z tymi normalnymi nawiasami

# przyciski operacji
button_add = Button(root, text="+", padx=39, pady=20, command=button_add)
button_equal = Button(root, text="=", padx=91, pady=20, command=button_equal)
button_clear = Button(root, text="Clear", padx=79, pady=20, command=button_clear)

# dodanie przycisków cyfr do naszej siatki
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)

# to samo dla przycisków operacji
button_clear.grid(row=4, column=1, columnspan=2)
button_add.grid(row=5, column=0)
button_equal.grid(row=5, column=1, columnspan=2)

root.mainloop()
