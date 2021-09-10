# Найдите площадь треугольника по трем сторонам (формула Герона)
# S= p(p−a)(p−b)(p−c)

# 1
import math


def count_square_Heron_1(a, b, c):
    p = 1 / 2 * (a + b + c)
    S = math.sqrt(p * (p - a) * (p - b) * (p - c))
    return S


# square = count_square_Heron_1(3,4,5)
# print(square)

# 2
"""
inputs = [3,4,8], [7,8,9], [5,3,2]
for n in inputs:
    S = geron(n[0], n[1], n[2])
    print ('Площадь =',S, '\n')
"""


def count_square_Heron_2(a, b, c):
    p = 1 / 2 * (a + b + c)
    S = math.sqrt(p * (p - a) * (p - b) * (p - c))
    return S


inputs = [3, 4, 5], [6, 7, 8], [9, 10, 11]
squares = []
for i in inputs:
    S = count_square_Heron_2(i[0], i[1], i[2])
    squares.append(S)
print(*squares, '\n', end='')  # пытался вывести их через запятую / рачитывал получить список из трех площадей
print(round(squares[2], 2))
