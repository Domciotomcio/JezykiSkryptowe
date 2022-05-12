COVID_PATH = r"C:\Users\Dominik\PycharmProjects\JezykiSkryptowe\lab9\CovidShort.txt"

MONTHS = {'Janauary': 1,
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


class FileOperation:  # do operacji na plikach odczytu z covid i zapisu logow
    def __init__(self):
        pass

    def read_from_file_covid(self, path, conditions_tuple):
        self.conditions_tuple = conditions_tuple
        covid_list = []

        with open(path, encoding='utf8') as f:
            next(f)
            for line in f:
                line_list = line.split()

                act_tuple = (int(line_list[1]), int(line_list[2]), line_list[6],
                             line_list[10], int(line_list[4]), int(line_list[5]))

                if self.tuple_meets_conditions(act_tuple):
                    covid_list.append(act_tuple)

        return covid_list

    def tuple_meets_conditions(self, checked_tuple):
        meets_conditions = True

        start_day = self.conditions_tuple[0] + self.conditions_tuple[1] * 100
        end_day = self.conditions_tuple[2] + self.conditions_tuple[3] * 100

        checked_day = checked_tuple[0] + checked_tuple[1] * 100

        return start_day <= checked_day <= end_day and \
               checked_tuple[2] == self.conditions_tuple[4] and \
               checked_tuple[3] == self.conditions_tuple[5]

    def write_log_file(self, path):
        print("zapisuje logi")


class ProgramLogic:
    def __init__(self):
        self.file_path = ""
        self.day_start = -1
        self.day_end = -1
        self.month_start = -1
        self.month_end = -1
        self.country = ""
        self.continent = ""
        self.cases_or_deaths = True  # True - cases, False deaths
        self.sort_by = True  # True - date, False cases/deaths
        self.sort_order = True  # True - ascending, False descending
        self.sum = True  # True - sum, False - all lines alone
        self.continents_list = ['Asia', 'Europe', 'Africa', 'America']
        self.covid_list = []

        self.set_default_param()

    def set_default_param(self):
        # ustawianie podstawowych parametrow (z pliku konfiguracyjnego?)
        self.file_path = COVID_PATH
        self.day_start = 1
        self.day_end = 30
        self.month_start = 1
        self.month_end = 12
        self.country = "Poland"
        self.continent = "Europe"
        self.cases_or_deaths = True  # True - cases, False deaths
        self.sort_by = True  # True - date, False cases/deaths
        self.sort_order = True  # True - ascending, False descending
        self.sum = True  # True - sum, False - all lines alone
        self.continents_list = ['Asia', 'Europe', 'Africa', 'America']
        self.covid_list = []

    def set_cases_or_deaths(self, value):
        self.cases_or_deaths = value

    def set_sort_order(self, value):
        self.sort_order = value

    def set_sum(self, value):
        self.sum = value

    def get_continents(self):
        return self.continents_list

    def get_acc_tuple(self):
        return self.day_start,  self.month_start, self.day_end, self.month_end, self.country, self.continent

    def set_covid_list(self, list):
        self.covid_list = list

    def sort_prepared_values(self):
        if self.sort_by:
            self.covid_list.sort()
        else:
            self.covid_list.sort()


class FirstProgram:
    def __init__(self):
        self.file_operation = FileOperation()
        self.program_logic = ProgramLogic()

        self.start_menu()

    def start_menu(self):
        print("Witaj w programie do wczytywania danych o Covid")
        print("Zaladowano podstawowa konfiguracje: ")
        # wyswietl podstawowa konfiguracja
        print("Wpisz polecenie")
        self.get_input()

    def get_input(self):
        # line = input()
        line = "show cases in Afghanistan in Asia on November 25"  # tylko do TESTOW !!!

        line_splitted = line.split()

        # można potem ogarnoc te konsolowe lepsze
        match line_splitted[0]:
            case 'set':
                self.set_scenario(line_splitted)
                print("Pomyslnie ustawiono")
            case 'show':
                self.show_scenario(line_splitted)
                self.program_logic.covid_list = \
                    self.file_operation.read_from_file_covid(COVID_PATH, self.program_logic.get_acc_tuple())

                self.print_results()

            case 'exit':
                pass


    def set_scenario(self, line_splitted):
        match line_splitted[1]:
            case 'total':
                if line_splitted[2] == 'on':
                    self.program_logic.set_sum(True)
                else:
                    self.program_logic.set_sum(False)

            case 'order':
                if line_splitted[2] == 'on':
                    self.program_logic.set_sort_order(True)
                else:
                    self.program_logic.set_sort_order(False)

            case 'cases':
                self.program_logic.set_cases_or_deaths(True)

            case 'deaths':
                self.program_logic.set_cases_or_deaths(False)

    def show_scenario(self, line_splitted):
        act_checked_el = 0

        while act_checked_el < len(line_splitted):
            act_checked_el += 1
            match line_splitted[act_checked_el]:
                case 'deaths':
                    self.program_logic.set_cases_or_deaths(True)
                case 'cases':
                    self.program_logic.set_cases_or_deaths(False)
                case 'from':
                    self.program_logic.month_start = MONTHS[line_splitted[act_checked_el + 1]]
                    self.program_logic.day_start = int(line_splitted[act_checked_el + 2])
                    self.program_logic.month_end = MONTHS[line_splitted[act_checked_el + 4]]
                    self.program_logic.day_end = int(line_splitted[act_checked_el + 5])

                    act_checked_el += 4
                case 'on':
                    self.program_logic.month_start = MONTHS[line_splitted[act_checked_el + 1]]
                    self.program_logic.day_start =  int(line_splitted[act_checked_el + 2])
                    self.program_logic.month_end = MONTHS[line_splitted[act_checked_el + 1]]
                    self.program_logic.day_end =  int(line_splitted[act_checked_el + 2])

                    act_checked_el += 4
                case 'in':
                    if line_splitted[act_checked_el + 1] in self.program_logic.continents_list:
                        self.program_logic.continent = line_splitted[act_checked_el + 1]
                    else:
                        self.program_logic.country = line_splitted[act_checked_el + 1]
                    act_checked_el += 1

    def print_results(self):
        print("Wyniki wyszukiwania:")

        if self.program_logic.sum and self.program_logic.cases_or_deaths:
            sum = 0
            for el in self.program_logic.covid_list:
                sum += el[4]
            print(sum)
        elif self.program_logic.sum and not self.program_logic.cases_or_deaths:
            sum = 0
            for el in self.program_logic.covid_list:
                sum += el[5]
            print(sum)

        else:
            for el in self.program_logic.covid_list:
                if self.program_logic.cases_or_deaths:
                    print(el[4])
                else:
                    print(el[5])


if __name__ == "__main__":
    program1 = FirstProgram()

