# Zadanie 3
from kol_licz_pier import kol_licz_pier

akt_liczba = int(input("podaj wartosc startowa: "))
k = int(input("podaj liczbe kolejnych liczb pierwszych k: "))

print("Liczby pierwsze po", akt_liczba, ":")

for i in range(0, k):
    akt_liczba = kol_licz_pier(akt_liczba)
    print(akt_liczba, " ")
