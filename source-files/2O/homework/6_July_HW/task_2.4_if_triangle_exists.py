# Существует ли треугольник с 3 введенными сторонами (в т.ч. ввести могут отрицательное число)
"""
У треугольника сумма любых двух сторон должна быть больше третьей.
Иначе две стороны просто "лягут" на третью и треугольника не получится.
необходимо сравнить суммы всех пар сторон с оставшейся третьей стороной. Чтобы треугольник существовал,
сумма всегда должна быть больше отдельной стороны или, по крайней мере, не меньше,
если учитывать так называемый вырожденный треугольник.
"""
n = 3
triangle = []
while n > 0:
    side = int(input('Enter triangle side: '))
    triangle.append(side)
    n -= 1
if triangle[0] + triangle[1] > triangle[2] and triangle[0] + triangle[2] > triangle[1] and triangle[1] + triangle[2] > \
        triangle[0]:
    print(' triangle with sides', *triangle, 'exists')
else:
    print(' triangle with sides', *triangle, "doesn't exists")
