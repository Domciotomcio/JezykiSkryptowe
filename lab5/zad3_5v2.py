# zadanie 5
import math


def metoda_wallisa(dokl):
    n = 1
    akt_przyb = 2 * 2 / 3

    while round(akt_przyb, dokl) != round(math.pi / 2, dokl):
        n += 1

        licznik = 2 * n
        mian1 = (2 * n - 1)
        mian2 = (2 * n + 1)
        akt_przyb *= licznik / mian1 * licznik / mian2

    return n


dokladnosc = int(input("podaj dokladnosc: "))
# print(round(math.pi, dokladnosc) / 2)
print("Wymagana liczba powtorzen n:", metoda_wallisa(dokladnosc))
