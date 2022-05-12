t = "to jest test"
lista = list(t)
lista[0] = "TXX"
lista.reverse()
t = "1".join(lista)
print(t)
