# Zadanie 1
import numpy as np


def lev_sim(str1, str2):
    m = len(str1)
    n = len(str2)

    tab = np.zeros((m + 1, n + 1))

    for i in range(len(str1) + 1):
        tab[i][0] = i

    for i in range(len(str2) + 1):
        tab[0][i] = i
    # print(tab)
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                cost = 0
            else:
                cost = 1
            tab[i, j] = min(tab[i-1, j] + 1,
                            tab[i, j-1] + 1,
                            tab[i-1, j-1] + cost)
    # print(tab)
    return tab[m, n]


if __name__ == '__main__':
    text1 = "hello"
    text2 = "keml"
    lev_sim("wyraz", "werez")
    print("Podobienstwo ciagow = ", lev_sim(text1, text2))
