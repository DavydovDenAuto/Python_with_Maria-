# словарь dict (в других языках ассоциативный массив)
# состоит из пар ключ: значение, где ключи уникальные, а значения - любые
# присвоение по новому ключу расширяет словарь,
# присвоение по существующему ключу перезаписывает значение,
# попытка извлечения несуществующего ключа порождает исключение
users = {1: "Tom", 2: "Bob", 3: "Bill"}
new_dict = list(users)
print(users[new_dict[1]])
elements = {"Au": "Золото", "Fe": "Железо", "H": "Водород", "O": "Кислород"}
objects = {1: "Tom", "2": True, 3: 100.6}
# пустой словарь
objects1 = {}
objects2 = dict()
# преобразование списка или кортежа в словарь возможно при условиях
# 1)список должен хранить набор вложенных списков
# 2)каждый вложенный список должен состоять из двух элементов
# первый элемент станет ключом, а второй - значением
users_list = [
    ["+111123455", "Tom"],
    ["+384767557", "Bob"],
    ["+958758767", "Alice"]
]
users_dict = dict(users_list)
print(users_dict)  # {"+111123455": "Tom", "+384767557": "Bob", "+958758767": "Alice"}
#
users_tuple = (
    ("+111123455", "Tom"),
    ("+384767557", "Bob"),
    ("+958758767", "Alice")
)
users_dict = dict(users_tuple)
print(users_dict)
# генератор словаря
d = {k: v for k, v in [('key1', 'value1',), ('key2', 'value2',)]}
print("d = ", d)
print()
# добавление нового ключа автоматически
users["+33333333"] = "Bob Smith"
print(users["+33333333"])
# проверка наличия ключа
key = "+4444444"
if key in users:
    user = users[key]
    print(user)
else:
    print("Элемент не найден")
key = "+55555555"
# get(key)
# Если элемента с таким ключом нет, то возвращает значение None
user = users.get(key)
# get(key, default)
# Если элемента с таким ключом нет, то возвращает "Unknown user"
user = users.get(key, "Unknown user")
# удаление элемента по ключу
del users["+33333333"]
print(users)
#
key = "+55555555"
if key in users:
    user = users[key]
    del users[key]
    print(user, "удален")
else:
    print("Элемент не найден")
# pop(key): удаляет элемент по ключу key и возвращает
# удаленный элемент. Если элемент с данным ключом отсутствует,
# то генерируется исключение KeyError
# pop(key, default): удаляет элемент по ключу key
# и возвращает удаленный элемент. Если элемент с данным ключом
# отсутствует, то возвращается значение default
users = {
    "+11111111": "Tom",
    "+33333333": "Bob",
    "+55555555": "Alice"
}
key = "+55555555"
user = users.pop(key)
print(user)

user = users.pop("+4444444", "Unknown user")
print(user)
# удалить все элементы
users.clear()
# копия в новый словарь
users = {"+1111111": "Tom", "+3333333": "Bob", "+5555555": "Alice"}
users2 = users.copy()
# добавить из другого словаря
users = {"+1111111": "Tom", "+3333333": "Bob", "+5555555": "Alice"}
users2 = {"+2222222": "Sam", "+6666666": "Kate"}
users.update(users2)
print(users)  # {"+1111111": "Tom", "+3333333": "Bob", "+5555555": "Alice", "+2222222": "Sam", "+6666666": "Kate"}
print(users2)  # {"+2222222": "Sam", "+6666666": "Kate"}
# циклы
users = {"+1111111": "Tom", "+3333333": "Bob", "+5555555": "Alice"}
print("for key in users:")
for key in users:
    print(key, " - ", users[key])
# Метод items() возвращает набор кортежей
print("for key, value in users.items():")
for key, value in users.items():
    print(key, " - ", value)
#
print("for key in users.keys():")
for key in users.keys():
    print(key)
#
print("for value in users.values():")
for value in users.values():
    print(value)

print()
# словари могут хранить и более сложные объекты
# в т.ч. другие словари
users = {
    "Tom": {
        "phone": "+971478745",
        "email": "tom12@gmail.com"
    },
    "Bob": {
        "phone": "+876390444",
        "email": "bob@gmail.com",
        "skype": "bob123"
    }
}
old_email = users["Tom"]["email"]
users["Tom"]["email"] = "supertom@gmail.com"
# проверка наличия ключа
key = "skype"
if key in users["Tom"]:
    print(users["Tom"]["skype"])
else:
    print("skype is not found")


# функция получает и возвращает словари
def info(params):
    print()
    mydict = {}
    for key in params:
        mydict[key + "_info"] = params[key] + "_info"
        params[key] += "_test"  # изменяет значения users
    params["новый ключ"] = "новое значение"  # изменяет значения users
    return mydict;


# вызов функции
users = {"+1111111": "Tom", "+3333333": "Bob", "+5555555": "Alice"}
rez = info(users)
print("for key in rez:")
for key in rez:
    print(key, " - ", rez[key])
print()
print("for key in users:")
for key in users:
    print(key, " - ", users[key])


# аргументы преобразуются в словарь с именем data
# количество пар произвольное
def intro(**data):
    print()
    print("\nData type of argument:", type(data))
    for key, value in data.items():
        print("{} is {}".format(key, value))


intro(Firstname="Петя", Lastname="Петров", Age=22, Phone=456)
intro(Firstname="Ваня", Lastname="Иванов", Email="d@nomail.com", Country="Wakanda", Age=25, Phone=123)
# а послать целый словарь intro(users) нельзя

# изменить значение ключа
books = {}
books['book'] = 3  # добавление ключа
books  # {'book': 3}
books['book'] -= 1
books  # {'book': 2}

# порядок элементов словаря не важен
# но можно отсортировать список
# функция sorted(mydict) == вернет list ключей а не dict
mydict = {'carl': 40,
          'alan': 2,
          'bob': 1,
          'danny': 3}
print("функция sorted(mydict) == вернет list ключей а не dict")
print(sorted(mydict))
print()
mylist = sorted(mydict)
for key in mylist:  # ключ достаем из списка и по ключу достаем значение
    print("%s: %s" % (key, mydict[key]))

# сортировка по значению
x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
print("x.items() =")
print(x.items())  # x.items() возвращает список кортежей(k,v)
x_sorted_by_value = {k: v for k, v in sorted(x.items(),
                                             key=lambda item: item[1])}
# {0: 0, 2: 1, 1: 2, 4: 3, 3: 4}
print(x_sorted_by_value)

# reverse обратная сортировка двумерного словаря сортируем по y
x = {1: {"y": 3, 2: 1}, 3: {2: 1, "y": 0}, 4: {"y": 2, 3: 4}, 2: {"y": 1, 0: 0}}
print("x.items() =")
print(x.items())
x_sorted_by_value = {k: v for k, v in sorted(x.items(),
                                             key=lambda item: item[1]["y"],
                                             # item[1] - ({'y': 3, 2: 1})элемент кортежа с индексом 1 (1, {'y': 3, 2: 1})
                                             reverse=True)}
# {1: {'y': 3, 2: 1}, 4: {'y': 2, 3: 4}, 2: {'y': 1, 0: 0}, 3: {2: 1, 'y': 0}}
print(x_sorted_by_value)

"""
5.5. На заводе 5 цехов. Известны план и факт за каждый месяц. 
Определите перевыполнение плана каждого цеха 
за каждый месяц и за весь год. 
Выведите таблицу выполнения плана цехами за год. 
Выведите номера цехов по порядку в зависимости от выполнения плана.
"""

factory = {'Цех_1': [155, 3, 8], 'Цех_2': [34, 3, 22], 'Цех_3': [220, 6, 17]}
#общая выработка
for key in factory:
    s=0
    for i in factory[key]:
        s+=i
# добавим выработку в массив
    factory[key].append(s)
print(factory)
# отсортируем в порядке плана
x_sorted_by_value = {k: v for k, v in sorted(factory.items(),
                                             key=lambda item: item[1][3],
                                             # item[1] - ({'y': 3, 2: 1})элемент кортежа с индексом 1 (1, {'y': 3, 2: 1})
                                             reverse=False)}
print(x_sorted_by_value)