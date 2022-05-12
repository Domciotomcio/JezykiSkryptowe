from First_name import First_name

def testowa1(arg1):
    print(arg1)
    arg1 = arg1 + " dodatek"
    print(arg1)


def testowa2(arg1):
    print(arg1)
    arg1.append("dodatek")
    print(arg1)
    return "OK"


class Test:
    def __init__(self, war):
        self.war = war

    def fun1(self):
        print("COSTAM")

    def __str__(self):
        return str(self.war)


test1 = Test(1).fun1()
