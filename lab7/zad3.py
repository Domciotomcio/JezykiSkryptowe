from timeit import default_timer as timer
import sys
from zad1 import create_tuple_all_cases, \
                 create_dic_by_country, \
                 create_dic_by_date


def for_country_a(country, cases_list):
    sum_deaths, sum_cases = 0, 0

    start = timer()

    for act_tuple in cases_list:
        if act_tuple[0] == country:
            sum_deaths += act_tuple[4]
            sum_cases += act_tuple[5]

    end = timer()

    time = "{:.4f}".format((end - start) * 1000)
    print(f"czas wykonania (w ms): {time}")

    return sum_deaths, sum_cases


def for_country_d(country, dic):
    sum_deaths, sum_cases = 0, 0

    start = timer()

    for key in dic:
        for val in dic[key]:
            if val[0] == country:
                sum_deaths += val[1]
                sum_cases += val[2]

    end = timer()

    time = "{:.4f}".format((end - start) * 1000)
    print(f"czas wykonania (w ms): {time}")

    return sum_deaths, sum_cases


def for_country_c(country, dic):
    sum_deaths, sum_cases = 0, 0

    start = timer()

    for key in dic:
        if key == country:
            for val in dic[key]:
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

    input_country = sys.argv[1]

    print("Sumaryczna liczba zgonów i przypadków dla danego kraju:")

    print("Funkcja for_country_a:")
    deaths, cases = for_country_a(input_country, list_all_cases)
    print(f"cases = {cases}, deaths = {deaths}")

    print("Funkcja for_country_d:")
    deaths, cases = for_country_d(input_country, dic_by_date)
    print(f"cases = {cases}, deaths = {deaths}")

    print("Funkcja for_country_c:")
    deaths, cases = for_country_c(input_country, dic_by_country)
    print(f"cases = {cases}, deaths = {deaths}")
