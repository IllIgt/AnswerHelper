nominative_root = \
        {
            1: "первый", 2: "второй", 3: "третий", 4: "четвертый", 5: "пятый", 6: "шестой", 7: "седьмой",
            8: "восьмой", 9: "девят", 10: "десят", 11: "одиннадцатый", 12: "двенадцатый", 13: "тринадцатый",
            14: "четырнадцатый", 15: "пятнадцатый", 16: "шестнадцатый", 17: "семнадцатый", 18: "восемнадцатый",
            19: "девятнадцатый"
        }

class Builder:
    def build_hundred(self):
        raise NotImplementedError()
    def build_ten(self):
        raise NotImplementedError()
    def build_one(self):
        raise NotImplementedError()

class Numeral:
    def __init__(self,hundred,ten,one):
        self.hundred = hundred
        self.ten = ten
        self.one = one

    def __str__(self):
        return "{} {} {}".format(self.hundred, self.ten, self.one)

class NumeralBuilder


    @staticmethod
    def to_string_nominative(number):



