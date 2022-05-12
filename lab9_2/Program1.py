from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo
from Logic import ProgramLogic

COVID_PATH = r"C:\Users\Dominik\PycharmProjects\JezykiSkryptowe\lab9\Covid.txt"

MONTHS = {'January': 1,
          'February': 2,
          'March': 3,
          'April': 4,
          'May': 5,
          'June': 6,
          'July': 7,
          'August': 8,
          'September': 9,
          'October': 10,
          'November': 11,
          'December': 12}

CONTINENTS = {'Asia', 'Europe', 'America', 'Africa'}


class FirstProgram:
    def __init__(self):
        self.logic = ProgramLogic()
        self.end_program = False
        self.is_ev_ok = True
        self.start_menu()

    def start_menu(self):
        print("Witaj w programie do wczytywania danych o Covid")

        while not self.end_program:
            print("Wpisz polecenie")
            self.get_input()

    def get_input(self):
        line = input()
        # line = "show cases in Afghanistan in Asia on November 25"  # tylko do TESTOW !!!
        # line = "show cases in Poland in June"  # tylko do TESTOW !!!
        # line = "show from May 10 till June 20"  # tylko do TESTOW !!!
        # line = "show cases in Afghanistan in Asia on November 25"  # tylko do TESTOW !!!

        line_splitted = line.split()

        checked_el = -1

        while checked_el < len(line_splitted) - 1:
            self.is_ev_ok = True
            checked_el += 1
            match line_splitted[checked_el]:
                case 'set':
                    match line_splitted[checked_el + 1]:
                        case 'total':
                            if line_splitted[checked_el + 2] == 'on':
                                self.logic.total_flag = True
                            elif line_splitted[checked_el + 2] == 'off':
                                self.logic.total_flag = False
                            else:
                                print("nieprawidlowa podana wartosc dla total")
                    checked_el += 2
                    self.is_ev_ok = False
                case 'show':
                    self.logic.show_flag = True
                case 'cases':
                    self.logic.cases_flag = True
                    self.logic.deaths_flag = False
                case 'deaths':
                    self.logic.deaths_flag = True
                    self.logic.cases_flag = False
                case 'in':
                    if line_splitted[checked_el + 1] in MONTHS:
                        self.logic.month_start = MONTHS[line_splitted[checked_el + 1]]
                        self.logic.day_start = 1
                        self.logic.month_end = MONTHS[line_splitted[checked_el + 1]]
                        self.logic.day_end = 31
                        checked_el += 1
                    elif line_splitted[checked_el + 1] in CONTINENTS:
                        self.logic.continent = line_splitted[checked_el + 1]
                        checked_el += 1
                    else:
                        self.logic.country = line_splitted[checked_el + 1]
                        checked_el += 1
                case 'on':
                    self.logic.month_start = MONTHS[line_splitted[checked_el + 1]]
                    self.logic.day_start = int(line_splitted[checked_el + 2])
                    self.logic.month_end = MONTHS[line_splitted[checked_el + 1]]
                    self.logic.day_end = int(line_splitted[checked_el + 2])
                    checked_el += 2
                case 'from':
                    self.logic.month_start = MONTHS[line_splitted[checked_el + 1]]
                    self.logic.day_start = int(line_splitted[checked_el + 2])
                    self.logic.month_end = MONTHS[line_splitted[checked_el + 4]]
                    self.logic.day_end = int(line_splitted[checked_el + 5])
                    checked_el += 4
                case 'exit':
                    self.end_program = True
                    self.is_ev_ok = False
                    break

                case _:
                    print('podano niepoprawne zdanie, sproboj jeszcze raz')
                    self.is_ev_ok = False
                    break

        if self.is_ev_ok:
            self.logic.set_conditions_tuple()
            self.logic.create_result()
            self.logic.prepare_result()
            self.print_result()

    def progres_file(self):
        pass

    def print_result(self):
        if self.logic.cases_flag:
            index = 4
        else:
            index = 5

        print(self.logic.total_flag)

        if self.logic.total_flag:
            sum = 0
            for el in self.logic.covid_list:
                sum += el[index]
            print("Suma przypadków:", sum)

        else:
            for el in self.logic.covid_list:
                print("{day}.{month}, {number}".format(day=el[0], month=el[1], number=el[index]))


if __name__ == "__main__":
    first_program = FirstProgram()
