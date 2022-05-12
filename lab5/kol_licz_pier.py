# kolejna liczba pierwsza
import math


def kol_licz_pier(pocz):
    podejrzana = pocz
    czy_pierwsza = False

    while not czy_pierwsza:
        czy_pierwsza = True
        podejrzana = podejrzana + 1
        zasieg = int(math.sqrt(podejrzana)) + 1

        for i in range(2, zasieg):
            if podejrzana % i == 0:
                czy_pierwsza = False
                break

    return podejrzana
