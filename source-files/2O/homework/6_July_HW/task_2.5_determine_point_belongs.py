# Определите, принадлежит ли точка с заданными координатами треугольнику,
# ограниченному осями координат и прямой 2х+3у=6

import math
def rasstoyanie(a_1, a_2, a_3, b_1, b_2, b_3):
    A=math.sqrt((a_2-a_1)**2+(b_2-b_1)**2)
    B=math.sqrt((a_3-a_2)**2+(b_3-b_2)**2)
    C=math.sqrt((a_1-a_3)**2+(b_1-b_3)**2)
    p=(A+B+C)/2
    s = math.sqrt((p*(p-A)*(p-B)*(p-C))/2)
    return s
print('Введите координаты:')
print('Х первой вершины ')
x_1=float(input())
print('Y первой вершины ')
y_1=float(input())
print('X второй вершины ')
x_2=float(input())
print('Y второй вершины ')
y_2=float(input())
print('Х третьей вершины ')
x_3=float(input())
print('Y третьей вершины ')
y_3=float(input())
s=rasstoyanie(x_1, x_2, x_3, y_1, y_2, y_3)
print(s)
input()

