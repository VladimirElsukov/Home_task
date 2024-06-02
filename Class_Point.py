'''
Задание 2
Реализуйте класс «Точка в пространстве». Необходимо хранить в полях
класса: координату по оси X, координату по оси Y, координату по оси Z.
Реализуйте конструктор по умолчанию и метод для вывода данных объекта.
Реализуйте методы валидации данных для атрибутов объекта. Реализуйте
доступ к отдельным атрибутам класса через методы объекта (геттеры и
сеттеры), используя декоратор @property и @атрибут.setter.

'''

class Point:

    def __init__(self, coor_x: int, coor_y: int, coor_z: int):
        self._x: int = coor_x
        self._y: int = coor_y
        self._z: int = coor_z

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = self.validation_coor(value, 'x')

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = self.validation_coor(value, 'y')

    @property
    def z(self):
        return self._z

    @z.setter
    def z(self, value):
        self._z = self.validation_coor(value, 'z')

    def validation_coor(self, value: int, parameter: int):
        if not isinstance(value, int):
            raise TypeError(f"Координата {parameter} должна быть целым числом.")
        return value

    def __str__(self):
        return f"(x: {self._x}; y: {self._y}; z: {self._z})"


p1 = Point(15, 76, 17)
p2 = Point(23, 13, 53)


if p1.x == 0 and p2.x == 0:
    print("Лежат на оси Х")
else:
    print("Не лежат на оси Х")
print(p1, p2)
print("*"*30)
p1.x = 44
p1.y = 54
p1.z = 0
p2.x = 44
p2.y = 23
p2.z = 17
print(p1, p2)