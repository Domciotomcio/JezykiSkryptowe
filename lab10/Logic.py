import os
from os.path import exists
from datetime import datetime

COVID_PATH = r"C:\Users\Dominik\PycharmProjects\JezykiSkryptowe\lab9\Covid.txt"


class FileOperation:  # do operacji na plikach odczytu z covid i zapisu logow
    def __init__(self, conditions_tuple):
        self.conditions_tuple = conditions_tuple

    def read_from_file_covid(self, path):
        covid_list = []

        if not os.path.exists(path):
            print("nie znaleziono pliku o podanej ścieżce")
            return []

        with open(path, encoding='utf8') as f:
            next(f)
            for line in f:
                line_list = line.split()

                if len(line_list) > 9:
                    act_tuple = (int(line_list[1]), int(line_list[2]), line_list[6],
                                 line_list[10], int(line_list[4]), int(line_list[5]))

                    a = self.tuple_meets_conditions(act_tuple)

                    if self.tuple_meets_conditions(act_tuple):
                        covid_list.append(act_tuple)

        return covid_list

    def tuple_meets_conditions(self, checked_tuple):
        meets_conditions = True

        start_day = self.conditions_tuple[0] + self.conditions_tuple[1] * 100
        end_day = self.conditions_tuple[2] + self.conditions_tuple[3] * 100

        checked_day = checked_tuple[0] + checked_tuple[1] * 100

        meets_conditions = (start_day <= checked_day <= end_day) and \
                           checked_tuple[2] == self.conditions_tuple[4] and \
                           checked_tuple[3] == self.conditions_tuple[5]

        return meets_conditions

    def set_conditions_tuple(self, new_con_tup):
        self.conditions_tuple = new_con_tup

    def write_log_file(self, name, path, covid_list, sum_flag, cases_flag):
        print("zapisano logi w pliku")

        if os.path.exists(path):
            print("znaleziono juz plik o podanej sciezce, zostanie on nadpisany")

        f = open("logi.txt", "w")

        if cases_flag:
            index = 4
        else:
            index = 5

        f.write("Logi z Covid\n")
        f.write("------------------\n")

        now = datetime.now()

        current_time = now.strftime("%H:%M:%S")
        f.write("Czas = " + str(current_time))
        f.write("\nkryteria:\n")
        f.write("data poczatkowa: {0}.{1}\n".format(self.conditions_tuple[0], self.conditions_tuple[1]))
        f.write("data koncowa: {0}.{1}\n".format(self.conditions_tuple[2], self.conditions_tuple[3]))
        f.write("kraj: {0}, kontynent: {1}\n".format(self.conditions_tuple[4], self.conditions_tuple[5]))
        f.write("Data  Liczba Przypadkow")
        f.write("\n------------------\n")

        if sum_flag:
            sum = 0
            for el in covid_list:
                sum += el[index]
            f.write("Suma przypadkow: " + str(sum))
        else:
            for el in covid_list:
                f.write("{day}.{month}, {number}\n".format(day=el[0], month=el[1], number=el[index]))
        f.write("\n------------------")
        f.close()


class ProgramLogic:
    def __init__(self):
        self.day_start = -1
        self.day_end = -1
        self.month_start = -1
        self.month_end = -1
        self.country = ""
        self.continent = ""
        self.show_flag = False
        self.set_flag = False
        self.cases_flag = False
        self.deaths_flag = False
        self.total_flag = False
        self.covid_list = []

        self.file_operation = FileOperation([])

        self.set_default_param()

    def set_default_param(self):
        self.day_start = 1
        self.day_end = 30
        self.month_start = 1
        self.month_end = 12
        self.country = "Poland"
        self.continent = "Europe"
        self.show_flag = False
        self.set_flag = False
        self.cases_flag = False
        self.deaths_flag = False
        self.total_flag = False

        self.file_operation.set_conditions_tuple(
            [self.day_start, self.month_start, self.day_end, self.month_end, self.country, self.continent])

    def create_result(self):
        self.covid_list = self.file_operation.read_from_file_covid(COVID_PATH)

    def prepare_result(self):
        # jakies sortowanie
        self.file_operation.write_log_file("logs.txt", "logs.txt", self.covid_list, self.total_flag, self.cases_flag)

    def default_operations(self):
        self.create_result()
        self.prepare_result()

    def set_param(self, params):
        self.day_start = params[0]
        self.day_end = params[1]
        self.month_start = params[2]
        self.month_end = params[3]
        self.country = params[4]
        self.continent = params[5]

        self.set_conditions_tuple()

    def set_conditions_tuple(self):
        self.file_operation.set_conditions_tuple(
            [self.day_start, self.month_start, self.day_end, self.month_end, self.country, self.continent])

