'''
Задание 1
Создайте класс «Число», которое хранит его значение и информацию о
системе счисления. Создайте несколько экземпляров данного класса.
Задание 2
Создайте класс «Калькулятор СС». В классе должна быть реализована
следующая функциональность:
– Перевод числа в восьмеричную систему счисления.
– Перевод числа в шестнадцатеричную систему счисления.
– Перевод числа в двоичную систему счисления.
– Перевод числа в десятичную систему счисления.
–Сложение двух чисел в разных системах счисления через обычный
арифметический оператор и составное присваивание. Результат сложения
записать в СС левого операнда.
'''

class Number:
    def __init__(self, value, base):
        self.value = value
        self.base = base

class NumberSystemCalculator:
    # Реализация перевода числа в двоичную систему счисления
    def to_binary(self, number):
        return bin(number.value).replace("0b", "")

    # Реализация перевода числа в восьмеричную систему счисления
    def to_octal(self, number):
        return oct(number.value).replace("0o", "")

    # Реализация перевода числа в шестнадцатеричную систему счисления
    def to_hexadecimal(self, number):
        return hex(number.value).replace("0x", "")

    # Реализация перевода числа из указанной системы счисления в десятичную
    def to_decimal(self, number, base):
        return int(str(number.value), number.base)

    # Реализация сложения чисел в разных системах счисления и запись результата в СС левого операнда
    def add_numbers(self, num1, num2):
        decimal_num1 = int(str(num1.value), num1.base)
        decimal_num2 = int(str(num2.value), num2.base)
        sum_decimal = decimal_num1 + decimal_num2
        return Number(sum_decimal, 10)

# Задание 1 => Создаем экземпляры класса "Число"
# Десятичная система счисления
num1 = Number(32, 10)
# Двоичная система счисления
num2 = Number(1010, 2)
# Шестнадцатеричная система счисления
num3 = Number('2A', 16)



# Задание2 => Пример использования:
num1 = Number(42, 10)
calculator = NumberSystemCalculator()


# Перевод числа в двоичную систему
binary_num = calculator.to_binary(num1)

# Перевод числа в восьмеричную систему
octal_num = calculator.to_octal(num1)

# Перевод числа в шестнадцатеричную систему
hex_num = calculator.to_hexadecimal(num1)

print(binary_num)
print(octal_num)
print(hex_num)
print('*'*30)
num2 = Number(101, 2)

# Сложение чисел в разных системах счисления

sum_result = calculator.add_numbers(num1, num2)
print(sum_result.value)










