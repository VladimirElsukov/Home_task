'''
1.Перебираем элементы списока my_list и если они четные добавляем в новый список result
'''
'''
my_list = [1, 45, 23, 2, 34, 43, 76, 77, 3, 3, 2, 7, 9, 8, 10, 23]
result = []
for item in my_list:
    if item % 2 == 0:
        result.append(item)
print(result)
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
Выводим:
1)обычный список,
2)"set comprehension" (генератор множества) с уникальными значениями c помощью тернарного оператора
3)"dict comprehension"
'''

my_list = [1, 1, 3, 4, 5, 3, 9, 4, 9, 4, 45, 23, 2, 34, 43, 76, 77, 3, 3, 2, 7, 9, 8, 10, 23]
result = [item for item in my_list if item % 3 == 0]
result2 = {item for item in my_list if item % 3 == 0}
result3 = {item * 5: item for item in my_list if item % 3 == 0}
print(result)
print(result2)
print(result3)