# Zadanie 1
def czy_palindrom(ciag):
    for i in range(0, int(len(ciag) / 2)):
        if ciag[i] != ciag[len(ciag) - i - 1]:
            return False
    return True


def czy_palindrom2(ciag):
    return ciag == ciag[::-1]


ciagPal = str(input("podaj ciag: "))

if czy_palindrom(ciagPal):
    print("ciag", ciagPal, "jest palindromem")
else:
    print("ciag", ciagPal, "nie jest palindromem")
