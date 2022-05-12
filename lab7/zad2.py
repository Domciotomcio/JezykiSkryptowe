from timeit import default_timer as timer
import sys
from zad1 import create_tuple_all_cases, \
                 create_dic_by_country, \
                 create_dic_by_date


def for_date_a(year, month, day, cases_list):
    sum_deaths, sum_cases = 0, 0

    start = timer()

    for act_tuple in cases_list:
        if act_tuple[3] == day and act_tuple[2] == month and act_tuple[1] == year:
            sum_deaths += act_tuple[4]
            sum_cases += act_tuple[5]

    end = timer()

    time = "{:.4f}".format((end - start) * 1000)
    print(f"czas wykonania (w ms): {time}")

    return sum_deaths, sum_cases


def for_date_d(year, month, day, dic):
    sum_deaths, sum_cases = 0, 0
    look_date = (year, month, day)

    start = timer()

    # for key in dic:
    #     if key == look_date:
    #         for val in dic[key]:
    #             sum_deaths += val[1]
    #             sum_cases += val[2]

    if look_date in dic:
        for val in dic[look_date]:
            sum_deaths += val[1]
            sum_cases += val[2]

    end = timer()

    time = "{:.4f}".format((end - start) * 1000)
    print(f"czas wykonania (w ms): {time}")

    return sum_deaths, sum_cases


def for_date_c(year, month, day, dic):
    sum_deaths, sum_cases = 0, 0

    start = timer()

    for key in dic:
        for val in dic[key]:
            if val[0] == year and val[1] == month and val[2] == day:
                sum_deaths += val[3]
                sum_cases += val[4]

    end = timer()

    time = "{:.4f}".format((end - start) * 1000)
    print(f"czas wykonania (w ms): {time}")

    return sum_deaths, sum_cases


if __name__ == "__main__":
    list_all_cases = create_tuple_all_cases()
    dic_by_date = create_dic_by_date()
    dic_by_country = create_dic_by_country()

    input_year = int(sys.argv[1])
    input_month = int(sys.argv[2])
    input_day = int(sys.argv[3])

    print("Sumaryczna liczba zgonów i przypadków dla danej daty dla wszystkich krajów:")

    print("Funkcja  for_date_a:")
    deaths, cases = for_date_a(input_year, input_month, input_day, list_all_cases)
    print(f"cases = {cases}, deaths = {deaths}")

    print("Funkcja  for_date_d:")
    deaths, cases = for_date_d(input_year, input_month, input_day, dic_by_date)
    print(f"cases = {cases}, deaths = {deaths}")

    print("Funkcja  for_date_c:")
    deaths, cases = for_date_c(input_year, input_month, input_day, dic_by_country)
    print(f"cases = {cases}, deaths = {deaths}")
