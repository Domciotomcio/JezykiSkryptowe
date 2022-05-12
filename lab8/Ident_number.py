import Controlled_text
import re
from my_exceptions import IdentNumberException


class Ident_number(Controlled_text.Controlled_text):

    def __init__(self, number):
        super().__init__()
        if self.check_number(number):  # 7 liczb
            self.__number = self.set_control_numbers(number)
        else:  # 9 liczb
            self.__number = number

    def check_number(self, number):
        """True gdy 7 cyfr, False gdy 9 cyfr, w innym wypadku wyjatek."""

        if len(number) == 7:
            pattern = re.compile(r'^\d{7}$')
            if pattern.findall(number):
                return True
            else:
                raise IdentNumberException("zle wprowadzone dane liczbowe")

        elif len(number) == 9:
            pattern = re.compile(r'^\d{9}$')
            if not pattern.findall(number):
                raise IdentNumberException("zle wprowadzone dane liczbowe")

            sum = 0
            for i in range(0, 7):
                sum += int(number[i])

            if sum % 97 == (int(number[7]) * 10 + int(number[8])):
                return False
            else:
                raise IdentNumberException("bledne cyfry kontrolne")

        else:
            raise IdentNumberException("zle podane dane")

    @staticmethod
    def set_control_numbers(number):
        num_list = [int(i) for i in list(number)]
        last_digits = sum(num_list) % 97
        return number+(str(last_digits))

    def get_ident_number(self):
        return self.__number

    def __str__(self):
        return self.get_ident_number()


if __name__ == "__main__":
    # print("Hello world")
    # pattern = re.compile(r'^\d{7}$')  # ^zaczyna sie od, \d liczby, {7}ich ilosc, $konczy sie
    # print(pattern.findall('1234567'))
    # print(pattern.findall('123456a'))
    # print(pattern.findall('123'))
    # print(pattern.findall('12345678'))

    id_num1 = Ident_number('1234567')
    id_num2 = Ident_number('123456728')
    # id_num3 = Ident_number('123')
    # id_num4 = Ident_number('1234932035043')
    # id_num5 = Ident_number('1dso234id4')

    print(id_num1)
