# [вираз for елемент in ітеративний елемент]
number_list = [number for number in range(1, 6)]
print(number_list)  # [1, 2, 3, 4, 5]
number_list = [number - 1 for number in range(1, 6)]
print(number_list)  # [0, 1, 2, 3, 4]
# [вираз for елемент in ітеративний елемент if умова]
a_list = [number for number in range(1, 6) if number % 2 == 1]
print(a_list)  # [1, 3, 5]
print('#######################################')
# {ключ: значення for вираз in ітеративний елемент}
word = 'Antarctica'
letter_counts = {letter: word.count(letter) for letter in word}
print(letter_counts)  # {'A': 1, 'n': 1, 't': 2, 'a': 2, 'r': 1, 'c': 2, 'i': 1}
print('##########################################')
print(sum(range(1, 51)))  # 1275
# task1: список состоящий из квадратов чисел от 0 до N-1
list_a = [a ** 2 for a in range(10)]
print(list_a)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# создадим список рэндомной длины
import random

n = random.randint(0, 50)
print(n)  # 21
list_b = [a for a in range(n)]
print(list_b)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# создадим список рэндомных элементов
lst = [random.randint(0, 10) for x in range(12)]
print(lst)  # [10, 7, 2, 7, 2, 0, 5, 10, 9, 4, 4, 10]
list_A = [x ** 2 for x in range(10)]
print(list_A)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
N = 10
list_A = [i ** 2 for i in range(N) if i % 2 == 0]
print(list_A)  # [0, 4, 16, 36, 64]
# 3 Вывести список городов длины которых меньше семи
cities = ['kyiv', 'kharkiv', 'bremen', 'paris', 'rome']
A = [city.title() for city in cities if len(city) < 5]
print(A)  # ['Kyiv', 'Rome']
print('-------------------------------------------')
movies = [('The Shawshank Redemption', 1994), ('Forrest Gump', 1994),
          ('Toy Story', 1995), ('Ghost in the Shell', 1995),
          ('The English Patient', 1996), ('The White Tiger', 2021),
          ('The Florida Project', 2017), ('A Fantastic Woman', 2017)]
# task1 - find movies relesad before 2000
released_before2000 = [title for (title, year) in movies if year < 2000]
print(released_before2000)
# task2 вывести все вильмы начинающиеся на A
movies = [('The Shawshank Redemption'), ('Forrest Gump'),
          ('Toy Story'), ('Ghost in the Shell'),
          ('The English Patient'), ('The White Tiger'),
          ('The Florida Project'), ('A Fantastic Woman')]
A_list = []
for title in movies:
    if title.startswith('A'):
        A_list.append(title)
print('usual way = ', A_list)
A_list_compr = [title for title in movies if title.startswith('A')]
print('A_list_compr = ', A_list_compr)
# вывести все варианты пар совмещенного кортежа двух списков
A = [1, 2, 3, 4, 5]
B = [4, 5, 2, 1, 9]
cartesian_product = [(a, b) for a in A for b in B]
print(cartesian_product)  # [(1, 4), (1, 5), (1, 2), (1, 1),...
# вывести имена(значения) из списка состоящего из словарей
users = [{'name': 'Amigo', 'age': 25}, {'name': 'Denis', 'age': 39}, {'name': 'Petro', 'age': 19}]
user_name = [user['name'] for user in users]
user_age = [age['age'] for age in users]
user_age_more25 = [age['name'] for age in users if age['age'] > 25 and age['name'] == 'denis'.title()]
print('user_age_more25:', *user_age_more25)
print(user_name)
print(user_age)
# создадим список с вложенным списком из словарей
users_groups = [
    [
        {'name': 'Amigo', 'age': 25},
        {'name': 'Denis', 'age': 39}
    ],
    [
        {'name': 'Sarah', 'age': 23},
        {'name': 'Julie', 'age': 32}
    ],
]
# создадим список имен из этого вложенно списка, традиционно-нужен двойной цикл,но попробуем лист компрехеншион
# двойной лист компр для входа во вложенный список
person_name = [person['name'] for group in users_groups for person in group]
print(person_name)
person_age_less30 = [person['name'] for group in users_groups for person in group if person['age'] < 30]
print(person_age_less30)

qwer = {'Legacy Educator': {'User': 'legacy_educator_subscr@gmail.com', 'Password': 'Sepultura1@#'}}
print(qwer)
list_qwer = [q for person in qwer for person['password'.lower()] in person]
print(list_qwer)
