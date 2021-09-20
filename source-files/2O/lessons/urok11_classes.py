# Классы и объекты
class Person:
    # атрибуты (общедоступные поля)
    name = "Tom"
    age = 18

    # методы
    # каждый метод должен принимать в качестве первого параметра
    # ссылку на текущий объект, который называется self
    def display_info(self):
        print("Привет, меня зовут", self.name)
    def function_1(self):
        self.address = 'Hello_street'
        address = 'Hi'
    def function_2(self):
        print(self.address)

object_1 = Person()
object_1.display_info()
print('----------------------------------------------------')





# при вызове метода в основной программе self не пишут
person1 = Person()  # конструктор по умолчанию, () - так вызывается конструктор/метод класса
print(type(person1))
val = 5
print(type(2))
if type(2)==type(val):
    print(2,'=целое число')
person1.display_info()  # Привет, меня зовут Tom
person2 = Person()
person2.name = "Sam"
person2.display_info()  # Привет, меня зовут Sam


#
class Person2:
    # конструктор, он сам добавит атрибут self.name
    def __init__(self, name):
        self.name = name  # устанавливаем имя, __спереди и сзади - это показатель что эти методы есть в Object,
        # _-protected,__-private
        #protected - доступен классу и его наследникам
        # self.name будет существовать пока существует объект
        # def __init__(self, name) name будет существовать до конца функции
    # деструктор
    def __del__(self):
        print(self.name, "удален из памяти") #может закрыть файл или соединение с базой

    def display_info(self):
        print("Привет, меня зовут", self.name)


person1 = Person2("Tom")
person1.display_info()  # Привет, меня зовут Tom
person2 = Person2("Sam")
person2.display_info()  # Привет, меня зовут Sam
del person1  # удаление из памяти


# если классы определены в другом модуле, он подключается как обычно
# from classes import Person, Auto
# или
# import classes
#
# свойства (локальные переменные) начинаются с __
# свойство-сеттер определяется после свойства-геттера
# и сеттер, и геттер называются одинаково - age.
# к геттеру и сеттеру, мы обращаемся через выражение tom.age
# как к атрибуту
class Person3:
    def __init__(self, name):
        self.__name = name  # свойство
        self.__age = 1  # свойство

    # геттер
    @property
    def age(self): # при вызове можно указывать x = person1.age  - без круглых скобок
        return self.__age

    # сеттер
    @age.setter
    def age(self, age): # при вызове можно указывать person1.age = 5  - без круглых скобок
        if age in range(1, 100):
            self.__age = age
        else:
            print("Недопустимый возраст")

    # геттер без сеттера
    @property
    def name(self):
        return self.__name

    # метод
    def display_info(self):
        print("Имя:", self.__name, "\tВозраст:", self.__age)


#
tom = Person3("Tom")
tom.display_info()  # Имя: Tom  Возраст: 1
tom.age = -3486  # Недопустимый возраст
print(tom.age)  # 1
tom.age = 36
tom.display_info()  # Имя: Tom  Возраст: 36


# подкласс и суперкласс
# суперкласс = базовый (base class) = родительский (parent class)
# подкласс = производный (derived class) = дочерний (child class)
#
class Person4:
    def __init__(self, name, age):
        self.__name = name  # устанавливаем имя
        self.__age = age  # устанавливаем возраст

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age in range(1, 100):
            self.__age = age
        else:
            print("Недопустимый возраст")

    @property
    def name(self):
        return self.__name

    def display_info(self):
        print("Имя:", self.__name, "\tВозраст:", self.__age)


# Employee наследует все из Person4 и добавляет свое
class Employee(Person4):
    # определение конструктора
    def __init__(self, name, age, company):
        # вызов метода базового класса - тут self нужен
        Person4.__init__(self, name, age)
        self.company = company

    # переопределение метода display_info
    def display_info(self):
        # вызов метода базового класса - тут self нужен
        Person4.display_info(self)
        print("Компания:", self.company)

    def details(self, company):
        # писать print(self.__name, "работает в компании", company)
        # нельзя, self.__name - приватный атрибут Person4
        print(self.name, "работает в компании", company)


tom = Employee("Tom", 23, "firma")
tom.details("Google")
tom.age = 33
tom.display_info()


#
class Student(Person4):
    # определение конструктора
    def __init__(self, name, age, university):
        Person4.__init__(self, name, age)
        self.university = university
        # переопределение метода display_info

    def display_info(self):
        print("Студент", self.name, "учится в университете", self.university)


#
people = [Person4("Tom", 23), Student("Bob", 19, "Harvard"), Employee("Sam", 35, "Google")]
#в массив записываются не объекты а указатели на объекты(адреса в памяти)
for person in people:
    person.display_info()
    print()
# Проверка типа объекта
for person in people:
    if isinstance(person, Student): #isinstance - метод языка, показывает что person принадлежит типу студент или его наследнику
        print('university = ', person.university)
    elif isinstance(person, Employee):
        print('company = ', person.company)
    else:
        print('name = ',person.name)
    print()
# все классы неявно имеют один общий суперкласс - object
# в т.ч. метод  __str__() - получить строковое представление объекта
tom = Person4("Tom", 23)
print("метод __str__() по умолчанию дает")
print(tom)


#
class Person5:
    def __init__(self, name, age):
        self.__name = name  # устанавливаем имя
        self.__age = age  # устанавливаем возраст

    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age in range(1, 100):
            self.__age = age
        else:
            print("Недопустимый возраст")

    def display_info(self):
        print(self.__str__())

    def __str__(self):
        return "Имя: {} \t Возраст: {}".format(self.__name, self.__age)


class Animals(Person5):
    def breathe(self):
        pass  # ничего не делает, но легко дописать потом

    def move(self):
        pass  # без 4 пробелов все равно нельзя писать

    def eat_food(self):
        pass


tom5 = Person5("Dan", 18)
print("метод __str__(), переопределенный в Person5 дает")
print(tom5)

newAnimal = Animals('sss',5)
print(newAnimal)
# дз - массив геометр фигур с разным расчетом площади/периметра для каждого, квадрат/круг... Вывести название Круг площадью 5 имеет периметр 45
# в разных файлах