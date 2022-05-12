KOLORY = {}


def rejestruj_kolor(nazwa):
    print(1 << len(KOLORY))
    return KOLORY.setdefault(nazwa, 1 << len(KOLORY))


def ma_kolor(opcje, nazwa):
    """porownoje binarne wartosci i zwraca binarna operacje AND"""
    return bool(opcje & nazwa)


CZARNY = rejestruj_kolor("CZARNY")
ZIELONY = rejestruj_kolor("ZIELONY")
ŻÓŁTY = rejestruj_kolor("ŻÓŁTY")
NIEBIESKI = rejestruj_kolor("NIEBIESKI")
moje = ZIELONY | ŻÓŁTY  # 0010 | 0100 = 0110
print(ma_kolor(moje, CZARNY))  # 0110 & 0001 = False
print(ma_kolor(moje, ZIELONY))  # 0110 & 0010 = True

print(1 & 2)
print(1 & 6)
print(2 & 6)
