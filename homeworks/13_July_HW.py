# https://smartiqa.ru/python-workbook/list
"""
1. Дан произвольный список, представьте его в обратном порядке
"""

# function_1
# def reverse_list_1(*list):
#     reverse_list = list[::-1]
#     print(f'reverse_list_1: {reverse_list}')
#
# reverse_list_1('Den', 'Margo', 'Elena', 'Victor')
#
# function_2
# def reverse_list_2(*list):
#     reverse_list = list[::-1]
#     return reverse_list
#
# print('reverse_list_2:',reverse_list_2('Den', 'Margo', 'Elena', 'Victor'))

# function_4
# def reverse_list_2(*list):
#     newlist = []
#     for i in range(1, len(list) + 1):
#         newlist.append(list[-1])
#     return newlist
#
# print(reverse_list_2('Den', 'Margo', 'Elena', 'Victor'))

# function_4
# number = int(input('Enter number: '))
# n = len(str(number))
# num_reverse = []
# while n > 0:
#     num_reverse.append(number % 10)
#     number //= 10
#     n -= 1
# print(*num_reverse)

"""
2. напишите функцию change(lst) которая принимает список и меняет местами его первый и последний элемент.
В исходном списке минимум 2 элемента
"""

# option_1
# def change(lst):
#     new_start, new_end = lst.pop(), lst.pop(0)  # можно и так
#     # new_start = lst.pop() #перенесли последний элемент в новую переменную
#     # new_end = lst.pop(0)  #перенесли первый элемент в новую переменную
#     lst.append(new_end)
#     lst.insert(0, new_start)
#     return lst
#
#
# print(change([1, 5, 8]))

# option_2
# def change(den):
#     den[-1], den[0] = den[0], den[-1]
#     return den
#
#
# print(change([1, 2, 3, 4]))

"""
3. Функция to_list() принимает неограниченное количество параметров. Обработайте их так, чтобы на выходе 
получить список из этих элементов.
"""
# def to_list(*args):
#     return list(args)
#
# print(to_list(2,0.5,'qwerty',True))
"""
4. Николай задумался о поиске «бесполезного» числа на основании списка. Суть оного в следующем: он берет произвольный 
список чисел, находит самое большое из них, а затем делит его на длину списка. 
Студент пока не придумал, где может пригодиться подобное значение, но ищет у вас помощи в реализации такой функции 
useless(s).
"""

# def useless(s):
#     return round(max(s) / len(s), 2)
#
#
# print(useless([2, 4, 8, 2.5, 10, 0]))

"""
5. Требуется создать функцию list_sort(lst), которая сортирует список чисел по убыванию их абсолютного значения.
Т.е. сортировка будет по модулю и числа будут отображаться с минусом, это норм"""


# def list_sort(lst):
#     lst.sort(key=lambda i: abs(i), reverse=True)
#     return lst
    
# не работает
# def list_sort_2(lst):
#     for i in lst:
#         i = abs(i)
#         lst.sort(reverse=True)
#     return lst
#
# print(list_sort_2([-3, 100, 8, -2]))

"""
Задачки на сортировки http://python-3.ru/page/sorted
1
a = [3, 2, 5 ,4, 7, 1]
2 Сортируем кортеж.
t = ('Zane', 'Bob', 'Janet')
3 Сортировка словаря.
d = {1:'a', 2:'b', 3:'c'}
4 Сортировка сложных структур с использованием ключа
class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
 
    def __repr__(self):
        return "" % (self.name, self.age)
Давайте сделаем список людей:
jack = Person('Jack', 19)
adam = Person('Adam', 43)
becky = Person('Becky', 11)
people = [jack, adam, becky]
Отсортировать список
5 Обратная сортировка
data = [3, 2, 5 ,4, 7, 1]
6 Сортировка с использованием функции attrgetter
7 Предварительное использование key в функции сортировки
8 Случайная сортировка
9 http://inphormatika.ru/programming/python/zadachi_python/vvod_dannyh_v_spisok_i_ego_sortirovka.html
10  https://tproger.ru/translations/python-sorting/
11 





"""


"""
6. На входе имеем список строк разной длины. Необходимо написать функцию all_eq(lst), которая вернет новый список 
из строк одинаковой длины. Длину итоговой строки определяем исходя из самой большой из них. 
Если конкретная строка короче самой длинной, дополнить ее нижними подчеркиваниями с правого края 
до требуемого количества символов.
"""
# with open('file.txt') as f:
#     line_count = 0
#     for i in f:
#         line_count += 1
#
# print(line_count)
