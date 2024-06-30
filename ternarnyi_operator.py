'''
1.Перебираем элементы списока my_list и если они четные добавляем в новый список result
'''
'''
my_list = [1, 45, 23, 2, 34, 43, 76, 77, 3, 3, 2, 7, 9, 8, 10, 23]
result = []
for item in my_list:
    if item % 2 == 0:
        result.append(item)
print(f"Cписок четных чисел: {result}")

'''







'''
Тернарный оператор 
'''
'''
number = 15
result = f"Число положительное {number * 2}" if number > 0 else "Число отрицательное"
print(result)
'''

'''
3.Добавляем в список result элемент списка, если он соответсвует условию справа и * 100
'''
'''
my_list = [1, 45, 23, 2, 34, 43, 76, 77, 3, 3, 2, 7, 9, 8, 10, 23]
result = [item * 100 for item in my_list if item % 3 == 0]
print(result)
'''

'''
my_list = [1, 45, 23, 2, 34, 43, 76, 77, 3, 3, 2, 7, 9, 8, 10, 23]
result2 = [item * 100 for item in my_list if item % 3 == 0]
print(result)
'''


'''
4)Выводим:
a)обычный список,
b)"set comprehension" (генератор множества) с уникальными значениями c помощью тернарного оператора
c)"dict comprehension"
'''

my_list = [45, 23, 2, 34, 43, 76, 1, 1, 3, 4, 5, 3, 9, 4, 9, 4, 77, 3, 3, 1, 1, 3, 4, 5, 3, 9, 4, 9, 4, 2, 7, 9, 8, 10, 23]
result = [item for item in my_list if item % 3 == 0]
result2 = {item for item in my_list if item % 3 == 0}
result3 = {item * 5: item for item in my_list if item % 3 == 0}
print(f"Вывод-списка: {result}")
print(f"Вывод списка с уникальными значениями- set comprehension:{result2}")
print(f"Вывод словаря- dict comprehension: {result3}")


'''
Решаем задачу. Проверяем Среди min значения и max. значения проверяем делятся ли числа на: 
3-5, 
на 3, 
на 5 
или не делятся. 
'''
'''
min_number = 1
max_number = 150
divided = []
for item in range(min_number, max_number + 1):
    if item % 15 == 0:
        divided.append("divided_3_5")
    elif item % 5 == 0:
        divided.append("divided_5")
    elif item % 3 == 0:
        divided.append("divided_3")
    else:
        divided.append(item)

print(divided)
'''




