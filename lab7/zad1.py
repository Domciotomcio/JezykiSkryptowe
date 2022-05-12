from timeit import default_timer as timer
COVID_PATH = r"C:\Users\Dominik\PycharmProjects\JezykiSkryptowe\lab7\Covid.txt"


def create_tuple_all_cases():
    all_cases = []

    with open(COVID_PATH, encoding='utf8') as f:
        next(f)
        for line in f:
            line_list = line.split()
            # Krotka (nazwa pełna, rok, miesiąc, dzień, liczba zgonów, liczba przypadków)
            act_tuple = (line_list[6], int(line_list[3]), int(line_list[2]),
                         int(line_list[1]), int(line_list[5]), int(line_list[4]))

            all_cases.append(act_tuple)

    return all_cases


def create_dic_by_date():
    by_date = {}

    with open(COVID_PATH, encoding='utf8') as f:
        next(f)
        for line in f:
            line_list = line.split()

            # (rok, miesiąc, dzień) - lista krotek (nazwa pełna, liczba zgonów, liczba przypadków)
            key_tuple = (int(line_list[3]), int(line_list[2]), int(line_list[1]))
            value_tuple = (line_list[6], int(line_list[5]), int(line_list[4]))

            if key_tuple in by_date:
                by_date[key_tuple].append(value_tuple)
            else:
                by_date[key_tuple] = [value_tuple]

    return by_date


def create_dic_by_country():
    by_country = {}

    with open(COVID_PATH, encoding='utf8') as f:
        next(f)
        for line in f:
            line_list = line.split()

            # nazwa kraju - (rok, miesiąc, dzień, liczba zgonów, liczba przypadków)
            value_tuple = (int(line_list[3]), int(line_list[2]), int(line_list[1]),
                           int(line_list[5]), int(line_list[4]))

            if line_list[6] in by_country:
                by_country[line_list[6]].append(value_tuple)
            else:
                by_country[line_list[6]] = [value_tuple]

    return by_country


if __name__ == '__main__':
    start = timer()
    cases_tuple = create_tuple_all_cases()
    print("czas tworzenia listy krotek all_cases = ", (timer()-start)*1000)
    # for i in cases_tuple:
    #   print(i)
    start = timer()
    by_date_dic = create_dic_by_date()
    print("czas tworzenia słownika by_date = ", (timer() - start) * 1000)
    # for i in by_date_dic:
    #    print(i, by_date_dic[i])
    start = timer()
    by_country_dic = create_dic_by_country()
    print("czas tworzenia słownika by_country = ", (timer() - start) * 1000)
    # for i in by_country_dic:
    #    print(i, by_country_dic[i])
