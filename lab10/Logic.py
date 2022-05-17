import os
from os.path import exists
from datetime import datetime

COVID_PATH = r"C:\Users\Dominik\PycharmProjects\JezykiSkryptowe\lab10\Covid.txt"


class FileOperation:  # do operacji na plikach odczytu z covid i zapisu logow
    conditions_tuple = []
    countries_continents = []

    def __init__(self, conditions_tuple):
        FileOperation.conditions_tuple = conditions_tuple

    @classmethod
    def read_from_file_covid(cls, path):
        covid_list = []

        if not os.path.exists(path):
            print("nie znaleziono pliku o podanej ścieżce")
            return []

        FileOperation.countries_continents = []

        with open(path, encoding='utf8') as f:
            next(f)
            for line in f:
                line_list = line.split()

                if len(line_list) > 9:
                    act_tuple = (int(line_list[1]), int(line_list[2]), line_list[6],
                                 line_list[10], int(line_list[4]), int(line_list[5]), line_list[0])

                    FileOperation.countries_continents.append((line_list[6], line_list[10]))

                    a = FileOperation.tuple_meets_conditions(act_tuple)

                    if FileOperation.tuple_meets_conditions(act_tuple):
                        covid_list.append(act_tuple)

        FileOperation.countries_continents = set(FileOperation.countries_continents)
        return covid_list

    @classmethod
    def tuple_meets_conditions(cls, checked_tuple):
        meets_conditions = True

        start_day = FileOperation.conditions_tuple[0] + FileOperation.conditions_tuple[1] * 100
        end_day = FileOperation.conditions_tuple[2] + FileOperation.conditions_tuple[3] * 100

        checked_day = checked_tuple[0] + checked_tuple[1] * 100

        meets_conditions = (start_day <= checked_day <= end_day) and \
                           checked_tuple[2] == FileOperation.conditions_tuple[4] and \
                           checked_tuple[3] == FileOperation.conditions_tuple[5]

        return meets_conditions

    @classmethod
    def set_conditions_tuple(cls, new_con_tup):
        FileOperation.conditions_tuple = new_con_tup

    @classmethod
    def write_log_file(cls, name, path, covid_list, sum_flag):
        print("zapisano logi w pliku")

        if os.path.exists(path):
            print("znaleziono juz plik o podanej sciezce, zostanie on nadpisany")

        f = open("logi.txt", "w")

        index = 4  # index czy przypadki czy zgony

        f.write("Logi z Covid\n")
        f.write("------------------\n")

        now = datetime.now()

        current_time = now.strftime("%H:%M:%S")
        f.write("Czas = " + str(current_time))
        f.write("\nkryteria:\n")
        f.write("data poczatkowa: {0}.{1}\n".format(FileOperation.conditions_tuple[0], FileOperation.conditions_tuple[1]))
        f.write("data koncowa: {0}.{1}\n".format(FileOperation.conditions_tuple[2], FileOperation.conditions_tuple[3]))
        f.write("kraj: {0}, kontynent: {1}\n".format(FileOperation.conditions_tuple[4], FileOperation.conditions_tuple[5]))
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

    @classmethod
    def load_countries_and_continents(cls, path):
        if not os.path.exists(path):
            print("nie znaleziono pliku o podanej ścieżce")
            return

        FileOperation.countries_continents = []

        with open(path, encoding='utf8') as f:
            next(f)
            for line in f:
                line_list = line.split()

                if len(line_list) > 9:
                    act_tuple = (int(line_list[1]), int(line_list[2]), line_list[6],
                                 line_list[10], int(line_list[4]), int(line_list[5]), line_list[0])

                    FileOperation.countries_continents.append((line_list[6], line_list[10]))

        FileOperation.countries_continents = set(FileOperation.countries_continents)
        print(FileOperation.countries_continents)


class ProgramLogic:
    day_start = -1
    day_end = -1
    month_start = -1
    month_end = -1
    country = ""
    continent = ""
    data_select_type = 1
    cases_type = 1
    sort_type = 1
    reverse_sort_flag = False
    total_flag = False
    covid_list = []

    def __init__(self):
        ProgramLogic.set_default_param()

    @classmethod
    def set_default_param(cls):
        ProgramLogic.day_start = 1
        ProgramLogic.day_end = 30
        ProgramLogic.month_start = 1
        ProgramLogic.month_end = 12
        ProgramLogic.country = "Poland"
        ProgramLogic.continent = "Europe"
        ProgramLogic.data_select_type = 1
        ProgramLogic.cases_type = 1
        ProgramLogic.sort_type = 1
        ProgramLogic.reverse_sort_flag = False
        ProgramLogic.total_flag = False

        ProgramLogic.set_conditions_tuple()

    @classmethod
    def create_result(cls):
        ProgramLogic.covid_list = FileOperation.read_from_file_covid(COVID_PATH)

    @classmethod
    def prepare_result(cls):
        # jakies sortowanie
        FileOperation.write_log_file("logs.txt", "logs.txt", ProgramLogic.covid_list, ProgramLogic.total_flag)

    @classmethod
    def default_steps(cls):
        ProgramLogic.create_result()
        ProgramLogic.prepare_result()
        ProgramLogic.sort_list()

    @classmethod
    def set_param(cls, params):
        ProgramLogic.day_start = params[0]
        ProgramLogic.day_end = params[1]
        ProgramLogic.month_start = params[2]
        ProgramLogic.month_end = params[3]
        ProgramLogic.country = params[4]
        ProgramLogic.continent = params[5]
        ProgramLogic.data_select_type = params[6]
        ProgramLogic.cases_type = params[7]
        ProgramLogic.sort_type = params[8]
        ProgramLogic.reverse_sort_flag = params[9]
        ProgramLogic.total_flag = params[10]
        print("Param dodany")
        print("ProgramLogic.country = ", ProgramLogic.country)

        ProgramLogic.set_conditions_tuple()

    @classmethod
    def set_conditions_tuple(cls):
        FileOperation.set_conditions_tuple([
            ProgramLogic.day_start,
            ProgramLogic.month_start,
            ProgramLogic.day_end,
            ProgramLogic.month_end,
            ProgramLogic.country,
            ProgramLogic.continent
        ])

    @classmethod
    def sort_list(cls):
        if ProgramLogic.sort_type == 1:
            ProgramLogic.covid_list.sort(key=lambda date: datetime.strptime(date[6], "%d.%m.%Y"),
                                         reverse=ProgramLogic.reverse_sort_flag)
        else:
            if ProgramLogic.cases_type == 1:
                ProgramLogic.covid_list.sort(key=lambda el: el[4], reverse=ProgramLogic.reverse_sort_flag)
            else:
                ProgramLogic.covid_list.sort(key=lambda el: el[5], reverse=ProgramLogic.reverse_sort_flag)

    @classmethod
    def check_country_and_continent(cls, country, continent):
        FileOperation.load_countries_and_continents(COVID_PATH)

        #if not (ProgramLogic.country, None) in FileOperation.countries_continents:
        #    return False

        if not (country, continent) in FileOperation.countries_continents:
            return False
        return True

if __name__ == "__main__":
    p1 = ProgramLogic()
    ProgramLogic.set_param([1, 30, 11, 11, 'Afghanistan', 'Asia', 1, 1, 1, False, False])
    ProgramLogic.default_steps()
