# Zadanie 1
ciag = str(input("podaj ciag: "))

if ciag == ciag[::-1]:
    print("ciag", ciag, "jest palindromem")
else:
    print("ciag", ciag, "nie jest palindromem")
