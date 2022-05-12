class Punkt:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):  # odpowiednik toString
        return "%02d:%02d" % (self.x, self.y)


class Pusta:
    pass  # konieczne, pusta linia to błąd


if __name__ == "__main__":
    p1 = Punkt(1, 2)
    p2 = Punkt(4, 10)
    print(p1, p2)
