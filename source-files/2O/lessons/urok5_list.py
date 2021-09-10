# список (в других языках массив)
numbers = [1, 2, 3, 4, 5]
# пустой список
numbers1 = []
# пустой список
numbers2 = list()
# копия списка
numbers2 = list(numbers)
# индексы с начала начинаются с 0
# индексы с конца начинаются с -1
# т.е. у последнего элемента будет индекс -1
print(numbers[0])  # 1
print(numbers[2])  # 3
print(numbers[-3])  # 3
numbers[0] = 88
print(numbers[0])
# повтор
num5 = [5] * 6  # [5, 5, 5, 5, 5, 5]
print(num5)
# последовательность
numbers = list(range(10))
print(numbers)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
numbers = list(range(2, 10))
print(numbers)  # [2, 3, 4, 5, 6, 7, 8, 9]
numbers = list(range(10, 2, -2))
print(numbers)  # [10, 8, 6, 4]
# можно разные типы
objects = [1, 2.6, "Hello", True]
for item in objects:
    print(item)
#
i = 0
while i < len(objects):
    print(objects[i])
    i += 1
# считаются равными, если они содержат один и тот же набор элементов
numbers = [1, 2, 3, 4]
numbers2 = list(range(1, 5))
if numbers == numbers2:
    print("numbers == numbers2")
else:
    print("numbers != numbers2")

# Добавление и удаление элементов
users = ["Tom", "Bob"]
# добавляем в конец списка
users.append("Alice")  # ["Tom", "Bob", "Alice"]
# добавляем на вторую позицию
users.insert(1, "Bill")  # ["Tom", "Bill", "Bob", "Alice"]
# получаем индекс элемента
i = users.index("Tom")
# удаляем по этому индексу
removed_item = users.pop(i)  # ["Bill", "Bob", "Alice"]
last_user = users[-1]
# удаляем последний элемент
users.remove(last_user)  # ["Bill", "Bob"]
print(users)
# перед удалением обязательно проверить наличие,
# иначе ошибка ValueError: list.remove(x): x not in list
if "Bill" in users:
    users.remove("Bill")  # удалит только первый, если их несколько
print(users)
# удаляем все элементы
users.clear()

# Подсчет вхождений
users = ["Tom", "Bob", "Alice", "Tom", "Bill", "Tom"]
kolvo_kopiy = users.count("Tom")
print(kolvo_kopiy)
# Сортировка
users.sort()
print(users)
# в обратном порядке
users.reverse()
print(users)
# в качестве параметра функция, вызываемая до сортировки
users = ["Tom", "bob", "alice", "Sam", "Bill"]
users.sort()
print(users)
users.sort(key=str.lower)
print(users)
# сортировка по ключу
student_tuples = [
    ('john', 'A', 15),
    ('jane', 'B', 12),
    ('dave', 'B', 10),
]
# здесь lambda - анонимная функция, student - ее аргумент
# student[2] - последнее поле
sorted(student_tuples, key=lambda student: student[2])
print(student_tuples)
# то же проще
from operator import itemgetter, attrgetter, methodcaller

sorted(student_tuples, key=itemgetter(2))
#
print(min(numbers))
print(max(numbers))

# поверхностное копирование
users1 = ["Tom", "Bob", "Alice"]
users2 = users1
users2.append("Sam")
# users1 и users2 указывают на один и тот же список
print(users1)  # ["Tom", "Bob", "Alice", "Sam"]
print(users2)  # ["Tom", "Bob", "Alice", "Sam"]
# глубокое копирование
import copy

users1 = ["Tom", "Bob", "Alice"]
users2 = copy.deepcopy(users1)
users2.append("Sam")
# пееменные users1 и users2 указывают на разные списки
print(users1)  # ["Tom", "Bob", "Alice"]
print(users2)  # ["Tom", "Bob", "Alice", "Sam"]
# list[start:end:step]:
# start индекс элемента, начиная с которого надо копировать
# end  индекс элемента, до которого нужно копировать
# step - шаг, через который будут копироваться элементы из списка
num10 = list(range(10))
slice_1 = num10[:3]  # с 0 по 3
print(slice_1)
slice_2 = num10[1:3]  # с 1 по 3
print(slice_2)
slice_3 = num10[1:6:2]  # с 1 по 6 с шагом 2
print(slice_3)
# Соединение списков
users1 = ["Tom", "Bob", "Alice"]
users2 = ["Tom", "Sam", "Tim", "Bill"]
users3 = users1 + users2
print(users3)  # ["Tom", "Bob", "Alice", "Tom", "Sam", "Tim", "Bill"]
# вложенные списки
# users[0][1] - второй элемент первого вложенного списка
users = [
    ["Tom", 29],
    ["Alice", 33],
    ["Bob", 27]
]
print(users[0])  # ["Tom", 29]
print(users[0][0])  # Tom
print(users[0][1])  # 29
# создание вложенного списка
user = list()
user.append("Bill")
user.append(41)
# добавление вложенного списка
users.append(user)
print(users[-1])  # ["Bill", 41]
# добавление во вложенный список
users[-1].append("123")
print(users[-1])  # ["Bill", 41, "123"]
# удаление последнего элемента из вложенного списка
users[-1].pop()
print(users[-1])  # ["Bill", 41]
# удаление всего последнего вложенного списка
users.pop(-1)

# удаление с индексами в интервале [индекс 1:индекс N] т.е. исключая N
numbers = [20, 30, 40, 50, 60, 70, 80]
print(numbers)
del numbers[1:2]  # удалить индекс 1
print(numbers)
del numbers[2:4]  # удалить индексы 2 и 3
print(numbers)
del numbers[1:]  # удалить индекс 1 и все, что после него
print(numbers)

# изменение первого элемента
users[0] = ["Sam", 18]
print(users)  # [ ["Sam", 18], ["Alice", 33], ["Bob", 27]]
# перебор через вложенные циклы
for user in users:
    for item in user:
        print(item, end=" - ")