from my_exceptions import ControlledTextException


class Controlled_text:
    def __init__(self, text='a'):
        if self.is_text_ok(text):
            self.__text = text

    def get_text(self):
        return self.__text

    def set_text(self, text):
        if self.is_text_ok(text):
            self.__text = text

    @staticmethod
    def is_text_ok(text):
        if not text.isprintable() or text.isspace():
            raise ControlledTextException("zle dane")
        else:
            return True

    def __lt__(self, other):
        return self.__text > other.get_text()

    def __gt__(self, other):
        return self.__text < other.get_text()

    def __str__(self):
        return self.get_text()


if __name__ == "__main__":
    ctext = Controlled_text()
    ctext.set_text("kot")
    print(ctext)
    # ctext2 = Controlled_text(" ")
    # ctext3 = Controlled_text("\n")
    # ctext2 = Controlled_text("abc")
    # ctext3 = Controlled_text("abd")
    # print(ctext2>ctext3)
