# java way data ENCAPSULATION
class P:

    def __init__(self, x):
        self.__x = x

    def get_x(self):
        return self.__x

    def set_x(self, x):
        if x >= 0:
            self.__x = x
        else:
            print('input positive number')


# python way without data ENCAPSULATION
class Q:

    def __init__(self, x):
        self.x = x


# class with default data
class Default:
    def __init__(self, name='Goga', age=100):
        self.name = name
        self.age = age


'''
Для создания приватного атрибута в начале его наименования ставится двойной прочерк: self.__name. 
К такому атрибуту мы сможем обратиться только из того же класса. Но не сможем обратиться вне этого класса.

Геттеры-сеттеры
Во-первых, стоит обратить внимание, что свойство-сеттер определяется после свойства-геттера.
Во-вторых, и сеттер, и геттер называются одинаково - age. И поскольку геттер называется age, то над сеттером устанавливается аннотация @age.setter.
После этого, что к геттеру, что к сеттеру, мы обращаемся через выражение tom.age

**Инкапсуляция - предоставляет интерфейсы взаимодействия с полями**
'''


class Person:
    def __init__(self, name):
        self.__name = name  # устанавливаем имя
        self.__age = 1  # устанавливаем возраст

    def set_age(self, age):
        if age in range(1, 100):
            self.__age = age
        else:
            print("Недопустимый возраст")

    def get_age(self):
        return self.__age

    def get_name(self):
        return self.__name

    def display_info(self):
        print("Имя:", self.__name, "\tВозраст:", self.__age)


tom = Person("Tom")

tom.display_info()  # Имя: Tom  Возраст: 1
tom.set_age(-3486)  # Недопустимый возраст
tom.set_age(25)
tom.display_info()  # Имя: Tom  Возраст: 25

"""
ООП - примеры
Дерево
Аттр: ствол, лист, ветки
Методы: качаться,расти, очищать воздух
Лиственное(Дерево)      Хвойное(Дерево)
Д.ствол = 100           Д.ствол = 1005
Д.очищатьВ = 10         Д.очищатьВ = 105
"""


class Derevo:
    def __init__(self, stvol=0, list=0):
        self.__stvol = stvol
        self.__list = list

    @property
    def stvol(self):
        return self.__stvol

    @property
    def get_list(self):
        return self.__list

    @stvol.setter
    def stvol(self, stvol):
        if stvol in range(1, 100):
            self.__stvol = stvol
        else:
            print('range: 1-100')


class Listvennoe(Derevo):
    def clean_air(self):
        pass


derevo1 = Derevo(15, True)
print(derevo1.__init__(22, True))
derevo2 = Listvennoe(20, False)
print(derevo2)
derevo3 = Derevo()
derevo3.stvol = 99  # derevo3.stvol() так с () нельзя задавать сеттер
print(derevo3.stvol)

class check_static:
    def __init__(self):
        self.__name = 'Vasia' #self.__name = 'Vasia' - can't print a = check_static(); print(a.name)
    @staticmethod
    def smth():
        print('Hello bot')
a = check_static()
a.smth()
check_static.smth() # Without object creation!!!!!

# дз - массив геометр фигур с разным расчетом площади/периметра для каждого, квадрат/круг... Вывести название Круг площадью 5 имеет периметр 45
# в разных файлах
"""
Класс фигура:
Класс Shape с абстрактными длиной, шириной и радиусом
Геттеры и сеттеры для создания объектов
Метод для вывода всех параметров объекта
Методы расчета периметра, площади, площади круга

Создадим классы квадрата,прямоугольника, треугольника, круга с методами вывода и задания св-в
В файле мэйн(или как-то так):
Создадим несколько значений в словаре:
3 квадрата
3 прямоугольника
3 треугольника
4 круга

"""

