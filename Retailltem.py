'''
Задание 1.
Реализуйте класс Retailltem (товарная единица), который содержит
данные о товаре в магазине. Этот класс должен хранить данные в атрибутах:
описание товара, количество единиц на складе и цена. После написания
этого класса напишите программу, которая создает три объекта Retailitem.

Создайте класс CashRegister (Кассовый аппарат), который может
использоваться вместе с классом Retailltem. Класс CashRegister должен иметь
внутренний список объектов Retailltem, а также приведенные ниже методы:
Метод purchase_item() (приобрести товар) в качестве аргумента
принимает объект Retailltem. При каждом вызове метода purchase_item()
объект Retailltem, передан­ный в качестве аргумента, должен быть добавлен в
список.
Метод get_total () (получить сумму покупки) возвращает общую
стоимость всех объектов Retailltem, хранящихся во внутреннем списке
объекта CashRegister.

Метод show_iterns () (показать товары) выводит данные об объектах
Retailltem, хранящихся во внутреннем списке объекта CashRegister.

Метод clear () (очистить) должен очистить внутренний список объекта
CashRegister.
Продемонстрируйте класс CashRegister в программе, которая
позволяет пользователю выбрать несколько товаров для покупки. Когда
пользователь готов рассчитаться за покупку, программа должна вывести
список всех товаров, которые он выбрал для покупки, а также их общую
стоимость.
'''

class RetailItem:
    def __init__(self, product_description: str, product_quantity: int, price: float):
        self.__product_description = product_description
        self.__product_quantity = product_quantity
        self.__price = price

class CashRegister:
    def __init__(self):
        self.__list_objects = []

    # приобрести товар, в качестве аргумента принимает объект Retailltem   item
    def purchase_item(self, item):
        self.__list_objects.append(item)
        return self.__list_objects

    # получить сумму покупки. возвращает общую
    # стоимость всех объектов Retailltem, хранящихся во внутреннем списке
    # объекта CashRegister.
    def get_total(self):
        total = 0
        for item in self.__list_objects:
            total += item._RetailItem__price * item._RetailItem__product_quantity
        return total

    # выводит данные об объектах товары Retailltem
    def show_items(self):
        item_info = ""
        for item in self._CashRegister__list_objects:  # Accessing the private attribute using the mangled name
            item_info += f"Описание товара: {item._RetailItem__product_description}\nКоличество товара: {item._RetailItem__product_quantity}\nЦена товара: {item._RetailItem__price}\n\n"
        return item_info

    # очистить внутренний список объекта CashRegister
    def clear(self):
        self.__list_objects = []


# Демонстрация работы

item1 = RetailItem("Рюкзак школьный SkyName для мальчика", 2, 4690.00)
item2 = RetailItem("Рюкзак школьный GRIZZLY для девочки", 1, 1990.00)
item3 = RetailItem("Пенал для мальчика", 2, 450.00)
item4 = RetailItem("Пенал для девочки", 1, 750.00)

register = CashRegister()

# Покупаем товар
register.purchase_item(item1)
register.purchase_item(item2)
register.purchase_item(item3)
register.purchase_item(item4)

print(register.show_items())

# Получение общей суммы
total = register.get_total()
print(f"Общая сумма покупки: {total}")

# Очистка кассового аппарата
register.clear()

