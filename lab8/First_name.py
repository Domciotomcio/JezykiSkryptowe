import Controlled_text
from my_exceptions import FirstNameException

NAMES_PATH = r"/lab8/PopularneImiona.txt"


class First_name(Controlled_text.Controlled_text):
    female_names = []
    male_names = []

    def __init__(self, name):
        super().__init__()
        # tylko za pierwszym razem
        if not First_name.female_names or not First_name.male_names:
            self.set_male_female_names(NAMES_PATH)

        if self.check_name(name):
            self.__name = name.casefold().capitalize()

    def check_name(self, name):
        # sprawdzanie czy tekst jest poprawny
        if self.is_text_ok(name):
            name = name.casefold().capitalize()  # przygotuj imie do szukania w liscie imion
        if name in First_name.male_names or name in First_name.female_names:
            return True
        else:
            raise FirstNameException("zle imie")

    @classmethod
    def set_male_female_names(cls, path):
        First_name.female_names, First_name.male_names = prepare_name_lists(path)

    def set_name(self, name):
        name = name.casefold().capitalize()  # przygotuj imie
        if self.check_name(name):
            self.__name = name

    def get_name(self):
        return self.__name

    def is_female(self):
        return self.female_name(self.__name)

    def is_male(self):
        return self.male_name(self.__name)

    @staticmethod
    def male_name(name):
        return True if name in First_name.male_names else False

    @staticmethod
    def female_name(name):
        return True if name in First_name.female_names else False

    def __str__(self):
        return self.get_name()


def prepare_name_lists(path):
    male_names = []
    female_names = []
    is_female_name = True

    with open(path, encoding='utf8') as f:
        next(f)  # pomin "Kobiety"
        # zczyta wszystkie imiona kobiet az do pustej linii
        for line in f:
            line = line.strip()

            if not line:
                break
            else:
                female_names.append(line)

        # zczyta wszystkie imiona mezczyzn
        next(f)  # pomin "Mezczyzni"
        for line in f:
            line = line.strip()
            male_names.append(line)

    return female_names, male_names


if __name__ == "__main__":
    first_name1 = First_name("adam")
    first_name2 = First_name("Anna")
    first_name3 = First_name("jAGoDA")
    first_name4 = First_name("Mikołaj")
    # first_name4 = First_name("\n")
    # first_name5 = First_name("Awsd")

    first_name1.set_name("SZYMON")
    print(first_name1.is_male())
    print(not first_name1.is_female())
    print(First_name.male_name("Adam"))

    print(first_name1)
    print(first_name2)
    print(first_name3)
    print(first_name4)
