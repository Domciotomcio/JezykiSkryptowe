from tkinter import *
from Logic import ProgramLogic


CONTINENTS = {'Asia', 'Europe', 'America', 'Africa'}

class App:
    def __init__(self):
        self.logic = ProgramLogic()

        self.root = Tk()
        self.root.geometry("600x400")
        self.root.title("Program 2")

        # ustawianie etykiet
        self.label1 = Label(self.root, text="selekcja zakresu dat")
        self.label1.grid(column=0, row=0)
        self.label2 = Label(self.root, text="Początkowy dzień")
        self.label2.grid(column=0, row=1)
        self.label2 = Label(self.root, text="Ostatni dzień")
        self.label2.grid(column=2, row=1)
        self.label2 = Label(self.root, text="Początkowy miesiąc")
        self.label2.grid(column=0, row=2)
        self.label2 = Label(self.root, text="Ostatni miesiąc")
        self.label2.grid(column=2, row=2)
        self.label3 = Label(self.root, text="Podaj kraj")
        self.label3.grid(column=0, row=3)
        self.label4 = Label(self.root, text="Podaj kontynent")
        self.label4.grid(column=2, row=3)

        # ustawianie entry_text
        self.entry_text1 = StringVar()
        self.entry_text1.set("tekst1")
        self.entry_text2 = StringVar()
        self.entry_text2.set("tekst2")
        self.entry_text3 = StringVar()
        self.entry_text3.set("tekst3")
        self.entry_text4 = StringVar()
        self.entry_text4.set("tekst4")
        self.entry_text5 = StringVar()
        self.entry_text5.set("tekst5")
        self.entry_text6 = StringVar()
        self.entry_text6.set("tekst6")

        # ustawianie pol do wprowadzania
        self.start_day_entry = Entry(self.root, textvariable=self.entry_text1)
        self.start_day_entry.grid(column=1, row=1)
        self.end_day_entry = Entry(self.root, textvariable=self.entry_text2)
        self.end_day_entry.grid(column=3, row=1)
        self.start_month_entry = Entry(self.root, textvariable=self.entry_text3)
        self.start_month_entry.grid(column=1, row=2)
        self.end_month_entry = Entry(self.root, textvariable=self.entry_text4)
        self.end_month_entry.grid(column=3, row=2)
        self.country_entry = Entry(self.root, textvariable=self.entry_text5)
        self.country_entry.grid(column=1, row=3)
        self.continent_entry = Entry(self.root, textvariable=self.entry_text6)
        self.continent_entry.grid(column=3, row=3)

        # checkboxy

        self.cb1 = IntVar()
        self.cb2 = IntVar()
        self.checkbox1 = Checkbutton(self.root, variable=self.cb1, text="Czy sortować po dacie?", onvalue=1, offvalue=0,
                                     command=self.checkbox1f)
        self.checkbox1.grid(column=0, row=6)
        self.checkbox2 = Checkbutton(self.root, variable=self.cb2, text="Sortowanie odwrotne", onvalue=1, offvalue=0,
                                     command=self.checkbox2f)
        self.checkbox2.grid(column=1, row=6)

        self.var_cases_deaths = IntVar()
        self.checkbox3 = Checkbutton(self.root, variable=self.var_cases_deaths, text="Wybierz zachorowania", onvalue=1,
                                     offvalue=0,
                                     command=self.checkbox_cases_deaths)
        self.checkbox3.grid(column=2, row=6)

        # przycisk do startu
        self.start_button = Button(self.root, text="Rozpocznij", command=self.when_start_button_clicked)
        self.start_button.grid(column=0, row=8)

        # pole tekstowe z wynikami
        self.result_text = Text(self.root, height=15, width=50)
        self.result_text.grid(column=1, row=8, columnspan=4)

        self.set_def_values()

        self.root.mainloop()

    def when_start_button_clicked(self):
        self.logic.set_param([
            int(self.start_day_entry.get()),
            int(self.end_day_entry.get()),
            int(self.start_month_entry.get()),
            int(self.end_month_entry.get()),
            self.country_entry.get(),
            self.continent_entry.get(),
        ])

        self.logic.create_result()
        self.logic.prepare_result()

        self.result_text.delete(1.0, END)

        if self.logic.cases_flag:
            index = 4
        else:
            index = 5

        if self.logic.total_flag:
            sum = 0
            for el in self.logic.covid_list:
                sum += el[index]
            self.result_text.insert("Suma przypadków:" + str(sum))
        else:
            for el in self.logic.covid_list:
                self.result_text.insert(END, str(el[0]) + "." + str(el[1]) + ", " + str(el[index]))
                self.result_text.insert(END, '\n')


    def checkbox1f(self):
        if self.cb1.get() == 1:
            self.logic.s
        else:
            print("False")

    def checkbox2f(self):
        if self.cb2.get() == 1:
            print("True")
        else:
            print("False")

    def checkbox_cases_deaths(self):
        print(self.var_cases_deaths.get())
        if self.var_cases_deaths.get() == 1:
            self.logic.cases_flag = True
            self.logic.deaths_flag = False
        else:
            self.logic.cases_flag = False
            self.logic.deaths_flag = True

    def changeText(self):
        self.text.set("Text updated")

    def set_def_values(self):
        self.entry_text1.set(25)
        self.entry_text2.set(25)
        self.entry_text3.set(11)
        self.entry_text4.set(11)
        self.entry_text5.set("Afghanistan")
        self.entry_text6.set("Asia")


if __name__ == "__main__":
    mp = App()

# Na kolejne zrobić znak zapytania
# w linii statusu ma obsłuzyc blad
# sprawdzanie poprawnosci formatu pliku