# двоичные (бинарные) файлы
#
# модуль pickle
#
# pickle.dump - запись переменной
import pickle
FILENAME = "user1.dat"
name = "Tom"
age = 19
with open(FILENAME, "wb") as file:
    pickle.dump(name, file)
    pickle.dump(age, file)
#pickle.load - чтение переменной
with open(FILENAME, "rb") as file:
    name = pickle.load(file)
    age = pickle.load(file)
    print("Имя:", name, "\tВозраст:", age)
#
FILENAME = "user2.dat"
users = [
    ["Tom", 28, True],
    ["Alice", 23, False],
    ["Bob", 34, False]
]
with open(FILENAME, "wb") as file:
    pickle.dump(users, file)
with open(FILENAME, "rb") as file:
    users_from_file = pickle.load(file)
    for user in users_from_file:
        print("Имя:", user[0], "\tВозраст:", user[1], "\tЖенат(замужем):", user[2])
#
# модуль shelve
#
#open(путь_к_файлу[, flag="c"[, protocol=None[, writeback=False]]])
#flag = c: для чтения и записи (по умолчанию).
#Если файл не существует, то он создается.
#r: только для чтения.
#w: для записи
#n: для записи Если файл не существует, то он создается.
#Если он существует, то он перезаписывается
#
import shelve
FILENAME = "states2"
with shelve.open(FILENAME) as states:
    states["London"] = "Great Britain"
    states["Paris"] = "France"
    states["Berlin"] = "Germany"
    states["Madrid"] = "Spain"
with shelve.open(FILENAME) as states:
    print(states["London"])
    print(states["Madrid"])
    key = "Brussels"
    if key in states:
        print(states[key])#
#get(). Первый параметр - ключ, второй - значение по умолчанию,
# которое возвращается, если ключ не найден.
with shelve.open(FILENAME) as states:
    state = states.get("Brussels", "Undefined")
    print(state)
#цикл for
with shelve.open(FILENAME) as states:
    for key in states:
        print(key," - ", states[key])
#keys() возвращает все ключи из файла, values() - все значения
with shelve.open(FILENAME) as states:
    for city in states.keys():
        print(city, end=" ")        # London Paris Berlin Madrid
    print()
    for country in states.values():
        print(country, end=" ")     # Great Britain France Germany Spain
#items() возвращает набор кортежей - ключ и значение
with shelve.open(FILENAME) as states:
    for state in states.items():
        print(state)
#для изменения данных достаточно присвоить по ключу новое значение,
#а для добавления данных - определить новый ключ
with shelve.open(FILENAME) as states:
    states["London"] = "Great Britain"
    states["Paris"] = "France"
    states["Berlin"] = "Germany"
    states["Madrid"] = "Spain"
with shelve.open(FILENAME) as states:
    states["London"] = "United Kingdom"
    states["Brussels"] = "Belgium"
    for key in states:
        print(key, " - ", states[key])
#удаление с одновременным получением
with shelve.open(FILENAME) as states:
    state = states.pop("London", "NotFound")
    print(state)
#удаление по ключу
with shelve.open(FILENAME) as states:
    del states["Madrid"]
#удаление всех
with shelve.open(FILENAME) as states:
    states.clear()
#
#  модуль os
#
import os
# путь относительно текущего скрипта
os.mkdir("hello") #создает новую папку
# абсолютный путь
os.mkdir("e://somedir")
os.mkdir("e://somedir//hello")
# путь относительно текущего скрипта
os.rmdir("hello") #удаляет папку
# абсолютный путь
os.rmdir("e://somedir//hello")
#переименовывает файл
with open("e://SomeDir//old_file.txt", "wb") as file:
    pickle.dump("test", file )
os.rename("e://SomeDir//old_file.txt", "e://SomeDir//new_file.txt")
#удаляет файл
os.remove("e://SomeDir//new_file.txt")
#проверить, существует ли файл
filename = input("Введите путь к файлу: ")
if os.path.exists(filename):
    print("Указанный файл существует")
else:
    print("Файл не существует")

#Copy the contents of the file named src to a file named dst.
#If dst already exists, it will be replaced.
#from shutil import copyfile
#copyfile(src, dst) #агрументы strings
#copy(src, dst) #агрументы os.path
#import shutil
#shutil.copy2('/src/dir/file.ext', '/dst/dir/newname.ext') # complete target filename given
#shutil.copy2('/src/file.ext', '/dst/dir') # target filename is /dst/dir/file.ext
