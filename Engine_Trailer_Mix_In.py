'''
Используя механизм множественного наследования разработайте класс
«Легковой автомобиль». Создайте несколько классов-наследников согласно
примерной классификации(

леговые автомобили-MotorCar
грузовые автомобили,Truck
автобусы-Bus
троллейбусы-Trolleybus)

. Создайте классы миксины «EngineMixIn»
(двигатель) и «TrailerMixIn» (прицеп). Используя классы-миксины
«примешайте» к классам наследникам несколько методов:
1. Метод класса TrailerMixIn, который добавляет груз в прицеп,
учитывая максимальную вместимость прицепа.
2. Метод класса EngineMixin, который заводит двигатель, учитывая
состояние двигателя «заведен» / «не заведен».
'''

class Car:
    ...

class EngineMixIn:
    def __init__(self):
        self.engine_started = False
    def start_engine(self):
        if not self.engine_started:
            self.engine_started = True
            print("Двигатель успешно заведен")
        else:
            print("Двигатель уже заведен")

    def stop_engine(self):
        if self.engine_started:
            self.engine_started = False
            print("Двигатель успешно выключен")
        else:
            print("Двигатель уже выключен")


class TrailerMixIn:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current_capacity = 0

    def add_cargo_trailer(self, cargo):
        if self.current_capacity + cargo <= self.capacity:
            self.current_capacity += cargo
            print(f"Груз добавлен. Текущий объем груза: {self.current_capacity} из {self.capacity}")
        else:
            print("Прицеп переполнен, нельзя добавить больше груза")



class MotorCar(Car, EngineMixIn):
    ...

class Truck(Car, EngineMixIn, TrailerMixIn):
    def __init__(self, capacity):
        super().__init__()
        TrailerMixIn.__init__(self, capacity)
        self.current_capacity = 0


class Bus(Car, EngineMixIn):
    ...

class Trolleybus(Car, EngineMixIn):
    ...

motorcar = MotorCar()
motorcar.start_engine()
motorcar.stop_engine()
truck = Truck(1000)
truck.start_engine()
truck.stop_engine()
truck.add_cargo_trailer(800)
truck.start_engine()
truck.add_cargo_trailer(150)
truck.add_cargo_trailer(300)
truck.stop_engine()




