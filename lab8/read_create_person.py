from Person import Person
from my_exceptions import ControlledTextException, FirstNameException, LastNameException, \
                          IdentNumberException, PersonException

PERSONS_PATH = r"/lab8/Persons.txt"


def read_and_create_person_list(path):
    person_list = []

    with open(path, encoding='utf8') as f:
        next(f)  # pomin tytulowy wiersz
        next(f)  # pomin opis kolumn

        for line in f:
            except_tail_text = "i nie udalo sie wczytac osoby: " + line
            try:
                person = Person()
                person.fromString(line)

                person_list.append(person)
            except ControlledTextException:
                print("Wystapil blad z zapisem tekstu", except_tail_text)
            except FirstNameException:
                print("Wystapil blad z imieniem", except_tail_text)
            except LastNameException:
                print("Wystapil blad z nazwiskiem", except_tail_text)
            except IdentNumberException:
                print("Wystapil blad z numerem identyfikujacym", except_tail_text)
            except PersonException:
                print("Wystapil blad z tworzeniem osoby", except_tail_text)

    return person_list


def print_person_list(person_list):
    print("Lista poprawnie odczytanych osób:")
    for person in person_list:
        print(person)


if __name__ == "__main__":
    person_list = read_and_create_person_list(PERSONS_PATH)
    print_person_list(person_list)
