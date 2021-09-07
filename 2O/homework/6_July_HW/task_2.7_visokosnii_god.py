# Определите, является ли заданный год высокосным

import datetime
import calendar

# k = datetime.date.today()
#
# l = datetime.date not in datetime.date.

# def check_year(year):
#     k = calendar.isleap(year=year)
#     if k:
#         print(f'{year} is visikosnii')
#     else:
#         print(f'{year} is NOT visikosnii')
#
# check_year(2020)

# просим ввести пока не получим высокосный
# def check_year():
#     while True:
#         check_year = int(input('Enter year for the check: '))
#         year = calendar.isleap(check_year)
#         if year:
#             print(f'{check_year} is visikosnii')
#             break
#         else:
#             print((f'{check_year} is NOT visikosnii, try the new year'))
#
#
# check_year()

"""
Високосный год кратен 4, но при этом не кратен 100, либо кратен 400. ... Иными словами, если год делится на 4 без 
остатка, но делится на 100 только с остатком, то он високосный, иначе — невисокосный, кроме случая, 
если он делится без остатка на 400 — тогда он всё равно високосный

Сделаем проверку деления по последнему символу и сделаем тест класс ассерт с календарем для проверки нашей функции
"""


def check_year(year):
    if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
        print(f'{year} is visikosnii')
    else:
        print(f'{year} is not visikosnii')

check_year(1900)

