# list comprehensions - генераторы списков - задает правила формирования списков

# task1: список состоящий из квадратов чисел от 0 до N-1
list_1 = []
n = 10
for i in range(n):  # n у нас меняется от 0 до N-1 благодаря функции range
    list_1.append(i ** 2)

print(list_1)

# 1_2

N = 10
list_A = [x ** 2 for x in range(10)]

print(list_A)

# 2 Создадим список из квадратов четных чисел от 0 до N-1

N = 10
list_A = []
for i in range(N):
    if i % 2 == 0:
        list_A.append(i ** 2)
print(list_A)
# 2_2
N = 10
list_A = [i ** 2 for i in range(N) if i % 2 == 0]
# Если число четное, то мы добавим его квадрат в диапазоне 0-9
# После списка можем записать любое условие
print(list_A)

# 3 Вывести список городов длины которых меньше семи
cities = ['kyiv', 'kharkiv', 'bremen', 'paris', 'rome']
A = [city.title() for city in cities if len(city) < 5]
# print([city.title() for city in cities if len(city)<5])
print(A)
"""
Алгоритм разбивающий целое положительное число по цифрам
Шаг1:
432%10 = 2
43//10 = 43
Шаг2:
43%10 = 3
43//10 = 4
Шаг3
4%10 = 4
4//10 = 0
"""
# 3_2
# x = int(input('Enter the number: '))
# digit = []
# while x:
#     digit.append(x % 10)
#     x //= 10
# print(digit)

# 3_3 reverse: Программа меняющая порядок следования элементов в списке
N = 11
A = list(range(N))
print(A)
for i in range(N // 2):
    A[i], A[N - i - 1] = A[N - i - 1], A[i]
print(A)

# 4 Сортировка методом выбора
A = [1, -5, 54, 100, 0, -45, 24]
N = len(A)
for i in range(N-1): # Этот фор отвечает за положение желтой стрелки
    for j in range(i+1,N): # этот фор отвечает за положение синей стрелки
        if A[i]>A[j]:
            A[i],A[j] = A[j],A[i]
print(A)