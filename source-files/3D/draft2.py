# список из енумерате
# 4 словаря в зип и вывести текст из них
# 2 тюпла в зип и вывести листом/словарем
"""
функцией мэп перевести строковый list с числами в интовый list /
 интовый в дробный / дробный в string / тюпл в дробный / дробный в список
"""
# list comprehension
#
#[вираз for елемент in ітеративний елемент]
# number_list = [number for number in range(1, 6)]
# print(number_list) #[1, 2, 3, 4, 5]
# number_list = [number-1 for number in range(1, 6)]
# print(number_list) #[0, 1, 2, 3, 4]
# #[вираз for елемент in ітеративний елемент if умова]
# a_list = [number for number in range(1, 6) if number % 2 == 1]
# print(a_list) #[1, 3, 5]
# print('#######################################')
#Return the number of times the value "cherry" appears in the fruits list
fruits = ['apple', 'banana', 'cherry']
x = fruits.count("cherry")
# #{ключ: значення for вираз in ітеративний елемент}
word = 'Antarctica'
letter_counts = {letter: word.count(letter) for letter in word}
print(letter_counts) #{'A': 1, 'n': 1, 't': 2, 'a': 2, 'r': 1, 'c': 2, 'i': 1}
print(word.count('letter'))
# print('##########################################')
#список x**2(mod 5)
list_x = [x**2 % 11 for x in range(1,101)]
print(list_x)
print(1%5)
# print(sum(range(1, 51))) #1275
# #task1: список состоящий из квадратов чисел от 0 до N-1
# list_a = [a**2 for a in range(10)]
# print(list_a) #[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
#
# #создадим список рэндомной длины
# import random
# n = random.randint(0,50)
# print(n) #21
# list_b = [a for a in range(n)]
# print(list_b) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
#
# #создадим список рэндомных элементов
# lst = [random.randint(0,10) for x in range(12)]
# print(lst) #[10, 7, 2, 7, 2, 0, 5, 10, 9, 4, 4, 10]
# list_A = [x ** 2 for x in range(10)]
# print(list_A) #[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
# N = 10
# list_A = [i ** 2 for i in range(N) if i % 2 == 0]
# print(list_A) #[0, 4, 16, 36, 64]
# # 3 Вывести список городов длины которых меньше семи
# cities = ['kyiv', 'kharkiv', 'bremen', 'paris', 'rome']
# A = [city.title() for city in cities if len(city) < 5]
# print(A) #['Kyiv', 'Rome']
list_22 = [1,3,5,6,0,205]
list_compr = [item+100 for item in list_22 if item%2==1]
print(list_compr)
list_33 = []
for i in list_22:
    i+=100
    if i%2 == 1:
        list_33.append(i)
print(list_33)
