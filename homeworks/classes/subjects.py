"""
Створити клас Предмети, a тоді застосувати оператор pass.
Створити клас під назвою Неживі й кажемо, що його батьківський клас - Предмети.
Створити клас під назвою Живі й кажемо, що його батьківський клас - теж Предмети.
Створіть три класи Тварини, Ссавці, Жирафи.
Створити об'єкт у класі Жирафи й присвоїти його як значення змінній реджинальд.
"""

class Subjects:
    pass

class NonLiving(Subjects):
    pass

class Alive(Subjects):
    pass

class Mammals:
    pass
class Animals:
    pass
class Giraffs:

    def __init__(self, name):
        self.reginald = name

    def print_name(self):
        print(f'name is {self.reginald}')

my_giraff = Giraffs('Karol')
my_giraff.print_name()