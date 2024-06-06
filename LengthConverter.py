'''
Задание 2
Создайте класс для перевода мер длины из метрической в имперскую
(английскую) систему. У класса должно быть несколько статических методов.

'''
class MetricToImperialConverter:
    @staticmethod
    def millimeter_to_inch(millimeter):
        return millimeter / 25.4

    @staticmethod
    def centimetre_to_inch(centimetre):
        return centimetre / 2.54

    @staticmethod
    def metre_to_inch(metre):
        return metre * 39.37

    @staticmethod
    def millimeter_to_foot(millimeter):
        return millimeter / 304.8

    @staticmethod
    def centimetre_to_foot(centimetre):
        return centimetre / 30.48

    @staticmethod
    def metre_to_foot(metre):
        return metre * 3.28084
    @staticmethod
    def metre_to_yard(metre):
        return metre / 0.9144

    @staticmethod
    def kilometer_to_yard(kilometer):
        return kilometer * 1.093613298

    @staticmethod
    def kilometer_to_mile(kilometer):
        return kilometer * 0.621371

    @staticmethod
    def centimetre_to_hand(centimetre):
        return centimetre / 10.16


centimetre = 735
inch = MetricToImperialConverter.centimetre_to_inch(centimetre)
foot = MetricToImperialConverter.centimetre_to_foot(centimetre)
hand = MetricToImperialConverter.centimetre_to_hand(centimetre)
print(f"{centimetre} сантиметров равно:\n{inch} дюймов, \n{foot} футов, \n{hand} хэнд")
print("*"*30)
kilometer = 325
mile = MetricToImperialConverter.kilometer_to_mile(kilometer)
print(f"{kilometer} киллометров равно: \n{mile} миль")