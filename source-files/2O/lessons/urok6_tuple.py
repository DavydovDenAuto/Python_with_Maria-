# кортеж (иногда в переводах пишут tuple)
# Гугл дает звук "тапл", оксфордский словарь транскрипцию "тьюп(э)л"
# как список, только нельзя изменять
# объявляется в круглых скобках или вообще без скобок
user = ("Tom", 23)
print(user)
user = "Jim", 45
print(user)
# кортеж из одного элемента требует запятую после него
user = ("Tom",)
# создание кортежа из списка
users_list = ["Tom", "Bob", "Kate"]
users_tuple = tuple(users_list)
print(users_tuple)
#
users = ("Tom", "Bob", "Sam", "Kate")
print(users[0])  # Tom
print(users[2])  # Sam
print(users[-1])  # Kate
# часть кортежа с индексами с 1 по 4-1=3
print(users[1:4])  # ("Bob", "Sam", "Kate")
# разложить кортеж на отдельные переменные
# для списка user = ["Tom", 22, False] тоже так можно
user = ("Tom", 22, False)
name, age, isMarried = user
print(name)  # Tom
print(age)  # 22
print(isMarried)  # False


# когда функция возвращает несколько значений,
# фактически она возвращает в кортеж:
def get_user():
    name = "Tom"
    age = 22
    is_married = False
    return name, age, is_married


user = get_user()
print(' ' * 10 + 'user = get_user()')
print(user[0])  # Tom
print(user[1])  # 22
print(user[2])  # False
# длина кортежа
print(len(user))  # 3
# циклы
print(' ' * 10 + 'for')
for item in user:
    print(item)
#
i = 0
print(' ' * 10 + 'while')
while i < len(user):
    print(user[i])
    i += 1
# наличие элемента в кортеже
if "Tom" in user:
    print("Пользователя зовут Tom")
else:
    print("Пользователь имеет другое имя")
# вложенные кортежи
countries = (
    ("Germany", 80.2, (("Berlin", 3.326), ("Hamburg", 1.718))),
    ("France", 66, (("Paris", 2.2), ("Marsel", 1.6)))
)
for country in countries:
    countryName, countryPopulation, cities = country
    print("\nCountry: {}  population: {}".format(countryName, countryPopulation))
    for city in cities:
        cityName, cityPopulation = city
        print("City: {}  population: {}".format(cityName, cityPopulation))
#
# set - множество объявляется в фигурных скобках {}
# множество содержит только уникальные значения
#
users = {"Tom", "Tom", "Bob", "Tom", "Alice", "Tom"}
print(users)  # {"Tom","Bob","Alice"}
# функция set(), в которую передается список или кортеж элементов
users3 = set(["Mike", "Bill", "Ted"])
# длина множества
print(len(users3))
# пустое множество
users = set()
print(len(users))
users.add("Sam")
print(users)
# удаление одного элемента
users = {"Tom", "Bob", "Alice"}
if "Tom" in users:
    users.remove("Tom")
print(users)  # {"Bob", "Alice"}
# discard() не будет генерировать исключения
# при отсутствии элемента
users.discard("Tom")
# удаление всех элементов
users.clear()
# циклы
for user in users:
    print(user)
# копия
users = {"Tom", "Bob", "Alice"}
users3 = users.copy()
# union() объединяет два множества и возвращает новое множество
# уникальные значения
users = {"Tom", "Bob", "Alice"}
users2 = {"Sam", "Kate", "Bob"}
users3 = users.union(users2)
print(users3)  # {"Bob", "Alice", "Sam", "Kate", "Tom"}
# intersection() производит операцию пересечения множеств
# и возвращает новое множество -
# элементы, которые есть в каждом
users3 = users.intersection(users2)
print(users3)  # {"Bob"}
# то же дает операция логического умножения
print(users & users2)  # {"Bob"}
# difference или операция вычитания
# возвращает те элементы, которые есть в первом множестве,
# но отсутствуют во втором
users3 = users.difference(users2)
print(users3)  # {"Tom", "Alice"}
print(users - users2)  # {"Tom", "Alice"}
# является ли множество подмножеством (т.е. частью) другого множества
# set.issubset(other) или set <= other - все элементы set принадлежат other
users = {"Tom", "Bob", "Alice"}
superusers = {"Sam", "Tom", "Bob", "Alice", "Greg"}
print(users.issubset(superusers))  # True
print(superusers.issubset(users))  # False
# текущее множество является надмножеством другого множества
# set.issuperset(other) или set >= other - все элементы other принадлежат set
print(users.issuperset(superusers))  # False
print(superusers.issuperset(users))  # True
# set == other - все элементы set принадлежат other и все элементы other принадлежат set
print("проверка users == superusers ", users == superusers)  # False
# вид множеств, которое не может быть изменено
# как tuple, но с уникальными элементами и др. особенностями set
f = frozenset({"Tom", "Bob", "Tom", "Bob", "Alice"})
print(f)
print(type(f))
print("проверка users == f ", users == f)  # True
# f[0] = "Dan" #TypeError: 'tuple' object does not support item assignment
list_users = list(users)  # ["Tom", "Bob", "Alice"]
print("проверка users == list_users ", users == list_users)  # False
