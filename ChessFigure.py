'''
Задание 1
Создайте базовый абстрактный класс ChessFigure. Опишите следующие
методы:
 Определить бьет ли она другую фигуру на поле
 Сделать ход на поле
 Определить возможность хода по правилам
 Определить текущие координаты
  - наследника, класса ChessFigure и сделайте ход
на поле по правилам.
'''

from abc import ABC, abstractmethod
class ChessFigure(ABC):
    def __init__(self, x, y):
        self.x = x
        self.y = y


    @abstractmethod
    def check_strike(self, x, y):
        ...


    @abstractmethod
    def make_move_field(self, new_x, new_y):
        ...

    @abstractmethod
    def check_move_rules(self, new_x, new_y):
        ...

    @abstractmethod
    def determine_current_coordinates(self):
        return self.x, self.y

class HorseFigure(ChessFigure):
    def __init__(self, x, y):
        super().__init__(x, y)

    # Определем бьет ли лошадь другую фигуру на поле
    def check_strike(self, x, y):
        dx = x - self.x
        dy = y - self.y
        if (dx == 1 and dy == 2) or (dx == 2 and dy == 1) or (dx == -1 and dy == 2) or (dx == -2 and dy == 1) or (
                dx == 1 and dy == -2) or (dx == 2 and dy == -1) or (dx == -1 and dy == -2) or (dx == -2 and dy == -1):
            return True
        else:
            return False

    def make_move_field(self, new_x, new_y):
        if self.check_move_rules(new_x, new_y):
            self.x = new_x
            self.y = new_y
            print(f"Фигура сделала ход на ({new_x}, {new_y})")
        else:
            print("Недопустимый ход")

    def check_move_rules(self, new_x, new_y):
        # Проверяем, соответствуют ли новые координаты возможным ходам лошади
        dx = abs(new_x - self.x)
        dy = abs(new_y - self.y)
        return (dx == 1 and dy == 2) or (dx == 2 and dy == 1)

    def determine_current_coordinates(self):
        return self.x, self.y


horse_figure = HorseFigure(3, 3)
print(horse_figure.check_strike(5, 4))
horse_figure.make_move_field(4, 5)
print(horse_figure.determine_current_coordinates())




