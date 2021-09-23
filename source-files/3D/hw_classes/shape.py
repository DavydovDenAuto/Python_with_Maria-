"""
Пусть нам необходимо работать с геометрическими фигурами, например, с квадратами, прямоугольниками,
треугольниками и так далее. Пусть каждая фигура будет описываться своим классом, при этом мы хотим
сделать так, чтобы каждый класс имел метод для вычисления площади и метод для вычисления периметра фигуры.
Давайте сделаем для этого абстрактный класс Figure с двумя абстрактными методами getSquare и getPerimeter.
Почему класс Figure абстрактный: потому что он не описывает реально существующую геометрическую фигуру
и, соответственно, объект этого класса мы не будем создавать.
http://code.mu/ru/php/book/oop/abstract-classes/
"""
class Shape:
    def get_perim(self):
        pass
    def get_area(self):
        pass

class Square(Shape):
    def __init__(self,a):
        self.a = a

    def get_area(self):
        return self.a**2

    def get_perim(self):
        return self.a*4


class Triangle(Square):

    def get_perim(self,a,b,c):
        self.__a = a
        self.__b = b
        self.__c = c

square = Square(5)
square_perim = square.get_perim()
square_area = square.get_area()
print(square_area,square_perim)








