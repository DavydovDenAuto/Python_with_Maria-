"""
Попросите ввести действительное число. Выведите квадратный корень от модуля его синуса
"""
import math

number = float(input('Введите действительное число: '))
res = math.sqrt(abs(math.sin(number)))
print(res)
