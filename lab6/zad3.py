from lev_sim import lev_sim

similarity = 3
source_name = "Poland"

# zczytanie nazw panstw
countries = []

with open(r'pliki\Covid.txt', encoding='utf8') as f:
    next(f)
    for line in f:
        line_list = line.split()
        countries.append(line_list[6])

countries_set = set(countries)

# przypisanie nazwie państwa podobienstwa
countries_dict = {}

for country in countries_set:
    countries_dict[country] = lev_sim(source_name, country)

# sortowanie wzgledem podobienstwa
sorted_dict = {}
sorted_keys = sorted(countries_dict, key=countries_dict.get)  # [1, 3, 2]

for w in sorted_keys:
    sorted_dict[w] = countries_dict[w]

# wyswietlanie podobnych
print("Kraje podobne w nazwie:")
for country, simil in countries_dict.items():
    if simil <= similarity:
        print(country)

# print(sorted_dict)

# na rano:
# zrobić sume w innych jezykach, w cmd jest praktycznie zrobione, szybka java i c++
# w 3 zrobic wszystko w funkcjach!!!
# zrobic stoper do dzialania w 2
# ogarnac, troche opisac te funkcje
