# Заданы координаты точек на плоскости. Найдите расстояние между ними
# AB = √(xb - xa)2 + (yb - ya)2
import math


def countCoordinates(x1, x2, y1, y2):
    dist = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return dist


distance = countCoordinates(4, 2, 6, 2)

print(distance)
