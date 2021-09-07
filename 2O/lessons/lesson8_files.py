"""
4.2. Найдите максимальный элемент массива. Выведите его значение
и индексы всех элементов, которые ему равны.
"""
import random

# res = []
# list_1 = []
# for i in range(11):
#     list_1.append(random.randint(5,10))
# print(list_1)
# max_1 = max(list_1)
# for i in range(len(list_1)):
#     if list_1[i] == max_1:
#         res.append(i)
# print(res)

"""
4.3. Заполните массив из 10 элементов разными натуральными случайными числами от 0 до 20. 
Совпадения не допускаются.
"""
# list_uniq = []
# for i in range(10):
#     found = True
#     while found == True:
#         found = False
#         x = random.randint(0,20)
#         if x in list_uniq:
#             found = True
#     list_uniq.append(x)
# print(list_uniq)

"""
4.4. Попросите пользователя ввести с клавиатуры массив из 5 элементов, которые деляться на 3.
"""
# for i in range(int(input())): # первой итерацией указывем длину будущего списка
# Solution 1
a = []
# for i in range(5):
#     found = False
#     while found == False:
#         k = int(input('Input a multiple of three list item: '))
#         if k % 3 == 0:
#             a.append(k)
#             found = True # or break
#         else:
#             print('Input a correct number')
# print(f'list a = {a}')


# Solution 2
#for i in range(random.randint(0, 100)):
# while len(a)<5:
#     k = int(input('Input a multiple of three list item and not null: '))
#     if k!=0 and k % 3 == 0:
#         a.append(k)
#     else:
#         print('Input a correct number')
# print(f'list a = {a}')

"""
4.6. Запишите элементы массива в обратном порядке в тот же массив.
Проверьте случаи четного и нечетного количества элементов. 
"""
# list_2.reverse()
# print(list_2)
# a = list_2[0:len(list_2)//2]
# b = a[::-1]
# print(b)
"""
4.7. С клавиатуры по очереди вводятся номера спортсменов и их результаты 
в соревнованиях по прыжкам в высоту. 
Выведите лучший результат после выступления каждого очередного спортсмена. 
После окончания соревнования выведите итоговое сообщение о трех лучших спортсменах.
"""
# a = 1, 180
# b = 2, 190
# c = 3, 150
# d = [a, b, c]
# print(d)
# sorted_d = sorted(d, key=lambda x: x[1])
# print(sorted_d[-1])
#
# for i in range(len(sorted_d)):
#     print(i, end=' ')
# print('\n************')
# d = []
# for i in range(10):
#     d.append((i+1,random.randint(150,230)))
#     sorted_d = sorted(d, key=lambda x: x[1])
#     print(sorted_d[-1], end=' лучший из ')
#     for j in range(len(sorted_d)):
#         print(sorted_d[j][0], end=' ')
#     print()
# print(d)
# print(sorted_d)

"""
5.9. Определите сумму и количество элементов прямоугольного массива, 
попадающих в заданный с клавиатуры диапазон (включительно с его границами).
"""

# n = 5
# m = 7
# a = []
# for i in range(n):
#     a.append([])
#     for j in range(m):
#         a[i].append(random.randint(-10, 10))
#         print(a[i][j], end='  ')
#     print()
#
# sum = 0
# amount = 0
# for i in range(n):
#     for j in range(0, m):
#         if 3 <= a[i][j] <= 5:
#             amount += 1
#             sum += a[i][j]
# print(f'amount = {amount}, sum = {sum}')
"""
5.10. Заполните прямоугольный массив случайными числами от 1 до 5 (включительно).
Простое задание: Если в какой-нибудь строке стоит подряд 3 одинаковых числа, замените их 0.
Сложное задание:
Если в каком-нибудь столбце или строке стоит подряд 3 одинаковых числа, замените их 0. 
Чтобы учесть вариант, когда одно число принадлежит тройке и по горизонтали, и по вертикали,
разрешается использовать дополнительный массив.
"""
# n = 5
# m = 7
# a = []
# b = []
# for i in range(n):
#     a.append([])
#     b.append([])
#     for j in range(0, m):
#         a[i].append(random.randint(1, 3))
#         b[i].append(0)
#         print(a[i][j], end='  ')
#     print()
# print()
# for i in range(n):
#     for j in range(0, m - 2):
#         if a[i][j] == a[i][j + 1] and a[i][j] == a[i][j + 2]:
#             b[i][j] += 1
#             b[i][j + 1] += 1
#             b[i][j + 2] += 1
# for k in b:
#     print(k)
print()
# print(b)

# цикл по побочной диагонали навыворот

# for i in range(n - 2):
#     for j in range(2, m):
#         if a[i][j] == a[i + 1][j - 1] and a[i][j] == a[i + 2][j - 2]:
#             b[i][j] += 1
#             b[i + 1][j - 1] += 1
#             b[i + 2][j - 2] += 1
# for k in b:
#     print(k)


# 5.7. Найдите сумму двух прямоугольных матриц (размеры должны совпадать).
# сложение векторов - сложение координат отдельно
# 3-5 задач одномерные и несколько на двумерные
"""
4.18. В старояпонском календаре был принят 60-летний цикл, 
состоявший из пяти 12 летних подциклов. Подциклы обозначались названиями цвета: 
зеленый, красный, желтый, белый и черный. 
Внутри каждого подцикла годы носили названия животных: 
крысы, коровы, тигра, зайца, дракона, змеи, лошади, овцы, обезьяны, курицы, собаки и свиньи. 
1984г. – год зеленой крысы – был началом очередного цикла. 
Напишите программу, которая вводит номер некоторого года нашей эры 
и печатает его название по старояпонскому календарю.

4.19. Выведите название дня недели по его номеру (1- понедельник и т.д.).
"""
