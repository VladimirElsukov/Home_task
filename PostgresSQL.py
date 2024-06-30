'''
Методы объекта соединения
close() - закрыть соединение
cursor() - создает объект для запросов
commit() - подтверждение транзакции, любого изменения
rollback() - принудительно завершить транзакцию

'''


import psycopg2
connection = None
cursor = None
try:
    connection = psycopg2.connect(
        dbname="student_grades",
        host="127.0.0.1",
        port=5433,
        user="postgres",
        password="postgres",
        options='-c client_encoding=utf-8'
    )
except psycopg2.Error as e:
    print(e)
else:
    print("Соединение установлено")
    # Запросы в БД
    cursor = connection.cursor()
    query = ('''SELECT * FROM student_grades''')
    cursor.execute(query)
    data = cursor.fetchall()
    print(data)
finally:
    if connection:
        cursor.close()
        # Если были изменения обязательно commit
        connection.commit()
        connection.close()


