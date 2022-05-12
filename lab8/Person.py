from First_name import First_name
from Last_name import Last_name
from Ident_number import Ident_number
from my_exceptions import PersonException
import re


class Person:
    def __init__(self, param1=None, param2=None, param3=None):
        self.first_name = param1
        self.last_name = param2
        self.ident_number = param3

    def fromString(self, text):
        pattern = re.compile(r'[A-Za-z0-9\-ąćęłńóśźżĄĘŁŃÓŚŹŻ]+')
        list = pattern.findall(text)

        if len(list) != 3:
            raise PersonException("zla ilosc pol danych")

        self.first_name = First_name(list[0])
        self.last_name = Last_name(list[1])
        self.ident_number = Ident_number(list[2])

    def __str__(self):
        return str(self.last_name) + " " + str(self.first_name) + ", " + str(self.ident_number)




if __name__ == "__main__":
    print("Hello world")
    pattern = re.compile(r'[A-Za-z0-9]+')
    print(pattern.findall('ala ma_kota;123'))

    osoba1 = Person(First_name("Kacper"), Last_name("Tomałek"), Ident_number("1234567"))
    osoba2 = Person()
    osoba2.fromString("Adam Polak-Kapar 123456930 ")
    osoba3 = Person()
    osoba3.fromString("Dawid;Młecz/193456937")
    osoba4 = Person()
    osoba4 = osoba4.fromString("")
    #osoba4 = Person("Adam", "Polak", "123456930", "costam")
    print(osoba1)
    print(osoba2)
    print(osoba3)

