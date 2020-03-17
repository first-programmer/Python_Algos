"""
Задание 4. Написать программу, которая генерирует в указанных пользователем границах:
    случайное целое число;
    случайное вещественное число;
    случайный символ.
Для каждого из трех случаев пользователь задает свои границы диапазона.
Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы.
Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.

Подсказка:
Нужно обойтись без ф-ций randint() и uniform()
Использование этих ф-ций = задание не засчитывается

Функцию random() использовать можно
Опирайтесь на пример к уроку
"""

import random
from re import sub

while 1:
    VAR = sub(r"[\s]", "", input(
        """
        Диапазон каких символов вы хотите получить?
        Если челых чисел, введи 1 а затем два числа поочереди.
        Если вещественных чисел, введи 2 а затем два вещественных числа поочереди.
        Если символьных, введите 3 а заетем два одиночных символа поочереди.
        Для выхода из программы введите q
        """
    ))

    if VAR.lower() == "q":
        break

    while 1:
        if VAR == "1":
            try:
                S1 = int(input("Введите число начала диапазона:"))
                S2 = int(input("Введите число конца диапазона:"))
            except ValueError:
                print("Вы ввели не верное значение одного из чисел")
                continue

            RAND_NUMBER = round(random.random() * (S2 - S1)) + S1
            print(RAND_NUMBER)
            break
        elif VAR == "2":
            try:
                S1 = float(input("Введите вещественное число начала диапазона:"))
                S2 = float(input("Введите вещественное число конца диапазона:"))
            except ValueError:
                print("Вы ввели не верное значение одного из чисел")
                continue

            RAND_NUMBER = round(random.random() * (S2 - S1), 5) + S1
            print(RAND_NUMBER)
            break
        elif VAR == "3":
            try:
                S1 = ord(input("Введите букву английского алфавита для начала диапазона:")) -96
                S2 = ord(input("Введите букву английского алфавита для конца диапазона:")) - 96
            except TypeError:
                print("Вы ввели недопустимое значение одного из символов")
                break

            RAND_SYMBOL = chr(round(random.random() * (S2 - S1)) + S1 +96)
            print(RAND_SYMBOL)
            break
        else:
            print("Вы ввели не допустимый вариант действия, попробуйте снова")
            break
