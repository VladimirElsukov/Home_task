class SafeCalculator:
    def safe_add(self, x, y):
        return x + y

    def safe_subtract(self, x, y):
        return x - y

    def safe_multiply(self, x, y):
        return x * y

    def safe_divide(self, x, y):
        return x / y if y != 0 else "Деление на ноль"

if __name__ == "__main__":
    safe_calc = SafeCalculator()

    while True:
        try:
            x = float(input("Введите первое число: "))
            operation = input("Выберите операцию (+, -, *, /): ")
            y = float(input("Введите второе число: "))

            if operation not in ['+', '-', '*', '/']:
                raise ValueError("Неподдерживаемая операция")

            if operation == "+":
                result = safe_calc.safe_add(x, y)
            elif operation == "-":
                result = safe_calc.safe_subtract(x, y)
            elif operation == "*":
                result = safe_calc.safe_multiply(x, y)
            elif operation == "/":
                result = safe_calc.safe_divide(x, y)
            else:
                raise ValueError("Неподдерживаемая операция")

            print("Результат:", result)

            redo = input("Желаете продолжить? (да/нет): ")
            if redo.lower() != "да":
                break

        except ValueError as e:
            print(str(e))
        except Exception as e:
            print("Произошла ошибка:", str(e))
