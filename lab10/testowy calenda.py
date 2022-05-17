from tkinter import *
from tkcalendar import *
from datetime import date, timedelta

root = Tk()
root.title('Tytuł')
root.geometry("600x400")

cal = Calendar(root, selectmode="day", date_pattern='dd.mm.y', year=2020, month=5, day=22)
cal.pack()

def grab_date():
    print(type(cal.get_date()))
    my_label.config(text="Today Date Is " + cal.get_date())

b1 = Button(root, text="Get Date", command=grab_date)
b1.pack()

my_label = Label(root, text="")
my_label.pack(pady=20)



root.mainloop()