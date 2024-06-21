'''
Задание 1
Создайте базовый абстрактный класс Shape для хранения методов
плоских фигур: area, perimeter, save, load. Определите следующие производные
классы:
Square — квадрат, который характеризуется координатами левого
верхнего угла и длиной стороны;
Rectangle — прямоугольник с заданными координатами верхнего
левого угла и размерами;
Circle — окружность с заданными координатами центра и радиусом;
Ellipse — эллипс с заданными координатами верхнего угла описанного
вокруг него прямоугольника со сторонами, параллельными осям координат,и
размерами этого прямоугольника.
Создайте список фигур. Напишите функцию, которая сохраняет
каждую фигуру в отдельный файл, загружает фигуру из файла и отображает
информацию о каждой из фигур, включая площадь и периметр.
'''

from abc import ABC, abstractmethod
import json

class Shape(ABC):
    def __init__(self, name, index):
        self.name = name
        self.index = index

    @abstractmethod
    def area(self):
        ...

    @abstractmethod
    def perimeter(self):
        ...

    @abstractmethod
    def save(self, filename):
        ...

    @classmethod
    @abstractmethod
    def load(cls, filename):
        ...

class Square(Shape):
    def __init__(self, name, index, x, y, side_length):
        super().__init__(name, index)
        self.x = x
        self.y = y
        self.side_length = side_length

    def area(self):
        return self.side_length ** 2

    def perimeter(self):
        return 4 * self.side_length

    def save(self, filename):
        data = {
            "type": "square",
            "name": self.name,
            "index": self.index,
            "x": self.x,
            "y": self.y,
            "side_length": self.side_length
        }
        with open(filename, 'w') as file:
            json.dump(data, file)

    @classmethod
    def load(cls, filename):
        with open(filename, 'r') as file:
            data = json.load(file)
            return cls(data["name"], data["index"], data["x"], data["y"], data["side_length"])

class Rectangle(Shape):
    def __init__(self, name, index,  x, y, width, height):
        super().__init__(name, index)
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def save(self, filename):
        data = {
            "type": "rectangle",
            "name": self.name,
            "index": self.index,
            "x": self.x,
            "y": self.y,
            "width": self.width,
            "height": self.height
        }
        with open(filename, 'w') as file:
            json.dump(data, file)

    @classmethod
    def load(cls, filename):
        with open(filename, 'r') as file:
            data = json.load(file)
            return cls(data["name"], data["index"], data["x"], data["y"], data["width"], data["height"])



# Создание списка фигур
shapes = [Square("Квадрат",0, 0, 5, 5), Rectangle("Прямоугольник", 0, 3, 4, 3, 4)]  # Добавьте сюда создание экземпляров других фигур

# Сохранем каждую фигуру в отдельный файл
for idx, shape in enumerate(shapes):
    shape.save(f'shape{idx}.json')

# Загрузка фигур из файлов и вывод информации о каждой из них
for idx in range(len(shapes)):
    if isinstance(shapes[idx], Square):
        loaded_shape = Square.load(f'shape{idx}.json')
    elif isinstance(shapes[idx], Rectangle):
        loaded_shape = Rectangle.load(f'shape{idx}.json')
    print(f"Фигура-> {idx+1}){loaded_shape.name}: Площадь - {loaded_shape.area()}, Периметр - {loaded_shape.perimeter()}")