'''
Задание 1
Создайте класс Flat (квартира). Для данного класса реализуйте ряд
перегруженных операторов: проверка на равенство площадей квартир
(операция == и !=), сравнение двух квартир по площади (операции >, <,
<=, >=).
Создайте класс контейнер ApartmentHouse (многоквартирный дом).
Атрибутом данного класса должен быть список объектов класса Flat.
Реализуйте в классе необходимые методы для работы с
последовательностями. Каждый новый дом по умолчанию имеет 10 этажей.
Продемонстрируйте работу с классом на примере.
'''

class Flat:
    def __init__(self, area:float):
        self.area = area

    def __eq__(self, other):
        return self.area == other.area

    def __ne__(self, other):
        return self.area != other.area

    def __lt__(self, other):
        return self.area < other.area

    def __gt__(self, other):
        return self.area > other.area

    def __le__(self, other):
        return self.area <= other.area

    def __ge__(self, other):
        return self.area >= other.area

class ApartmentHouse():
    def __init__(self):
        self.flats = []
        self.num_floors = 10

    def add_flat(self, flat):
        self.flats.append(flat)

# Создаем несколько квартир
flat1 = Flat(80.5)
flat2 = Flat(90.7)
flat3 = Flat(70.3)

# Проверяем перегруженные операторы
print(flat1 == flat2)
print(flat1 != flat2)
print(flat1 < flat2)
print(flat1 > flat2)
print(flat1 <= flat2)
print(flat1 >= flat2)

# Создаем многоквартирный дом и добавляем квартиры в список дома
house = ApartmentHouse()
print(f"В доме {house.num_floors} этажей.")
house.add_flat(flat1)
house.add_flat(flat2)
house.add_flat(flat3)

# Выводим список квартир в доме
for index, flat in enumerate(house.flats, start=1):
    print(f"Квартира{index}: площадь {flat.area} кв.м.")