# Найдите среднее арифметическое и среднее геометрическое трех чисел
# перемножить все числа и извлечь из них корень. Степень корня определяется количеством чисел
# print(pow(8, 1/3))
# print(8 ** (1/3))

import math

n = 3
arith_numbers = []
geom_numbers = []
while n > 0:
    k = int(input('Enter number: '))
    arith_numbers.append(k)
    geom_numbers.append(k)
    n -= 1


def count_arithmetic(a, b, c):
    res = (a + b + c) / 2
    return res


def count_geom(a, b, c):
    res = round(pow((a * b * c), 1 / 3), 2)
    return res


for i in arith_numbers, geom_numbers:
    arith_result = count_arithmetic(i[0], i[1], i[2])
    geom_result = count_geom(i[0], i[1], i[2])
print(f'Среднее арифметическое чисел {arith_numbers}  = {arith_result}')
print(f'Среднее геометрическое чисел {geom_numbers}  = {geom_result}')
