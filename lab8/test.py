class Punkt:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "%02d:%02d"%(self.x, self.y)

    def metoda_z_x(self, x):
        print("x = ", x)
        x += 1
        print("x = ", x)


class Pusta:
    pass


if __name__ == "__main__":
    str1 = "123"
    print(type(str1[0]))
