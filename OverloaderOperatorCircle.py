'''
Задание 1
Создайте класс Circle (окружность). Для данного класса реализуйте
ряд перегруженных операторов: проверка на равенство площадей двух
окружностей (операция ==, !=), проверка сравнения площадей двух
окружностей (операции >, <,<=,>=).
'''

import math
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi*self.radius**2

    '''
    экземпляр первого класса сравниваем с экземпляром 2 класса(=> он и будет other), 
    для него вызываем метод other.area()
    '''

    def __eq__(self, other):
        return self.area() == other.area()

    def __ne__(self, other):
        return self.area() != other.area()

    def __lt__(self, other):
        return self.area() < other.area()

    def __le__(self, other):
        return self.area() <= other.area()

    def __gt__(self, other):
        return self.area() > other.area()

    def __ge__(self, other):
        return self.area() >= other.area()

c1 = Circle(7)
c2 = Circle(15)

print(c1 == c2)
print(c1 != c2)
print(c1 < c2)
print(c1 > c2)
print(c1 <= c2)
print(c1 >= c2)