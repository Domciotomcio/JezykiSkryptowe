import Controlled_text
from my_exceptions import LastNameException

class Last_name(Controlled_text.Controlled_text):
    def __init__(self, lname):
        super().__init__()
        if self.check_lname(lname):
            self.__lname = lname

    def check_lname(self, lname):
        if '-' not in lname:
            # 1. Ciąg liter zaczynający się od dużej litery a potem same małe : Kowalski
            return self.check_conditions(lname)
        else:
            # 2. Dwa liter zaczynające się od dużej litery a potem same małe rozdzielone przez znak '-'
            temp_names = lname.split('-')
            return self.check_conditions(temp_names[0]) and self.check_conditions(temp_names[1])

    def check_conditions(self, lname):
        """Ciąg liter zaczynający się od dużej litery a potem same małe"""

        is_name_ok = True
        temp_name = list(lname)

        if not self.is_text_ok(lname):
            is_name_ok = False

        if not temp_name:
            raise LastNameException("zle nazwisko")

        if not temp_name[0].isupper():
            is_name_ok = False

        temp_name[0] = temp_name[0].casefold()

        if "".join(temp_name) != "".join(temp_name).casefold():
            is_name_ok = False

        if is_name_ok:
            return True
        else:
            raise LastNameException("zle nazwisko")

    def set_name(self, lname):
        self.__lname = self.check_lname(lname)

    def get_name(self):
        return self.__lname

    def __str__(self):
        return self.get_name()


if __name__ == "__main__":
    last_name1 = Last_name("Kowalski")
    last_name2 = Last_name("Nowak-Grodzinski")
    last_name3 = Last_name("-")
    # last_name4 = Last_name("AMAdek-Bodzinski")

    print(last_name1)
    print(last_name2)
    print(last_name3)
