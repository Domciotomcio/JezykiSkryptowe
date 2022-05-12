# zadanie 4

def lista_srednich_krocz(list_in):
    if not list_in:
        return []

    krok = list_in[0]
    lista_res = []

    for i in range(1, len(list_in) - krok + 1):
        suma = 0
        for ii in range(0, krok):
            suma += list_in[i + ii]
        srednia = float(suma / krok)
        lista_res.append(srednia)

    return lista_res


lista1 = [2, 1, 5, 7.7, 12]
lista2 = [3, 1, 5, 6, 7]
lista3 = [2, 1, 1]
lista4 = []

print(lista_srednich_krocz(lista1))
print(lista_srednich_krocz(lista2))
print(lista_srednich_krocz(lista3))
print(lista_srednich_krocz(lista4))
