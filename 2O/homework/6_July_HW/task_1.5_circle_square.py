# Вычислите длину окружности и площадь круга заданного радиуса
# длина окружности C = 2*p*R; площадь круга S = p*R*R
import math


def countCircumferenceAndSquare():
    radius = float(input('Enter radius: '))
    C = round(2 * math.pi * radius, 2)
    S = round(math.pi * radius ** 2, 2)
    print(f'Длина окружности равна: {C},площадь круга равна: {S}')


countCircumferenceAndSquare()
