'''
Задание 1
Создайте класс для конвертирования температуры из градусов
Цельсия в градусы Фаренгейта, Кельвина и наоборот. У класса должно быть
несколько статических методов.
'''
class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return celsius * 9/5 + 32

    @staticmethod
    def celsius_to_kelvin(celsius):
        return celsius + 273.15

    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        return (fahrenheit - 32) * 5/9

    @staticmethod
    def fahrenheit_to_kelvin(fahrenheit):
        return (fahrenheit - 32) * 5/9 + 273.15

    @staticmethod
    def kelvin_to_celsius(kelvin):
        return kelvin - 273.15

    @staticmethod
    def kelvin_to_fahrenheit(kelvin):
        return (kelvin - 273.15) * 9/5 + 32

# Пример использования:
celsius = 25
fahrenheit = TemperatureConverter.celsius_to_fahrenheit(celsius)
kelvin = TemperatureConverter.celsius_to_kelvin(celsius)
print(f"{celsius} градусов Цельсия равно {fahrenheit} градусам Фаренгейта и {kelvin} Кельвинам.")

fahrenheit = 50
celsius = TemperatureConverter.fahrenheit_to_celsius(fahrenheit)
kelvin = TemperatureConverter.fahrenheit_to_kelvin(fahrenheit)
print(f"{fahrenheit} градусов Фаренгейта равно {celsius} градусам Цельсия  и {kelvin} Кельвинам.")

kelvin = 150
celsius = TemperatureConverter.kelvin_to_celsius(kelvin)
fahrenheit = TemperatureConverter.kelvin_to_fahrenheit(kelvin)
print(f"{kelvin} градусов Келвина равно {celsius} градусам Цельсия  и {fahrenheit} Фаренгейта.")
