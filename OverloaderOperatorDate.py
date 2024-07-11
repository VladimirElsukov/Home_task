'''
Задание 2
Создайте класс Date, который будет содержать информацию о текущей
дате (день, месяц, год). Для данного класса реализуйте ряд перегруженных
операторов: проверка на равенство двух дат (операция ==, !=), проверка
сравнения двух дат (операции >, <,<=,>=).
'''

class Date:
    def __init__(self, day:int, month:int, year:int):
        self.day = day
        self.month = month
        self.year = year

    def __eq__(self, other):
        return (self.year, self.month, self.day) == (other.year, other.month, other.day)

    def __ne__(self, other):
        return not self == other

    def __lt__(self, other):
        return (self.year, self.month, self.day) < (other.year, other.month, other.day)

    def __le__(self, other):
        return self < other or self == other

    def __gt__(self, other):
        return not (self <= other)

    def __ge__(self, other):
        return not (self < other)


data1 = Date(25, 5, 2005)
data2 = Date(15, 12, 1990)
print(data1 == data2)
print(data1 != data2)
print(data1 > data2)
print(data1 < data2)
print(data1 <= data2)
print(data1 >= data2)