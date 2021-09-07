# a = [1, 2, 3]
# print(a)
# b = a
# print(b)
# a[0] = 'surprise'
# print(a)
# print(b)
# b[0] = 'I hate surprises'
# print(b)
# print(a)
# print("---------------------------------------")
# a = [1, 2, 3]
# b = a.copy()
# c = list(a)
# d = a[:]
# print(d)
# planets = ['Mercury', 'Jupiter', 'Earth', 'Mars', 'Venus']
# print(len(planets))
# print(list('sun'))
# mybirthday = '3:4:1981'
# mybirthday.split(':')
# print(mybirthday.split(':'))
# result = 'a|b||c|d||||e'
# result.split('|')
# print(result.split('|'))
planets = ['Mercury', 'Jupiter', 'Earth', 'Mars', 'Venus']
print(' - '.join(planets))
# cars = ['Alfa Romeo', 'Volvo', 'Lamborghini', 'BMW', 'Toyota']
# print(cars[1])
# print(cars[4])
# print(cars[0])
# print(cars[-1])
# print(cars[-2])
# planets = ['Mercury', 'Jupiter', 'Earth', 'Mars', 'Venus']
# print(planets.index('Earth'))
# text_editors = ['Atom', 'Sublime Text']
# programming_language = ['Python', 'C', 'JavaScript']
# programmers = ['Guido van Rossum', 'Dennis Ritchie', 'Brendan Eich']
# all_info = [text_editors, 'code', programming_language, programmers]
# print(all_info)
# print(all_info[0])
# print(all_info[2])
# planets = ['Mecury', 'Jupiter', 'Earth', 'Mars', 'Venus']
# planets.append('Zemlia')
# planets[2] = 'Saturn'
# print(planets)
# planets.append('Uranus')
# print(planets)
# planets = ['Earth', 'Mars']
# satellites = ['Moon', 'Deimos', 'Phobos']
# planets.extend(satellites)
# print(planets)
# fruits = ['blueberry', 'grape', 'orange', 'plum', 'pear', 'melon', 'pear']
# print(fruits.count('grape'))
# print(fruits.count('peach'))
# print(fruits.count('pear'))
# print(fruits.count('blueberry'))
# clothes = ['shirt', 'hat', 'jeans', 'trainers']
# sorted_clothes = sorted(clothes)
# print(sorted_clothes)
# print(clothes.sort())
# print(clothes)
#
numbers = [5, 3, 7, 0, 4]
numbers.sort()
print(numbers)
# numbers = [5, 3, 7, 0, 4]
# numbers.sort(reverse=True)
# print(numbers)
# cars = ['bmw', 'audi', 'toyota', 'subaru']
# print(cars)
# cars.reverse()
# print(cars)
# numbers = list(range(1, 6))
# print(numbers)
# even_numbers = list(range(2, 11, 2))
# print(even_numbers)
# print("--------------------------------------------")
# digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# print(min(digits))
# print(max(digits))
# print(sum(digits))
# empty_tuple = ()
# print(empty_tuple)
# empty_dict = {}
# print(empty_dict)


# mydog = {'name': 'Australian Shepherd', 'training': '5', 'intelligence': 5, 'type': 'Companion'}
# print(mydog)
# couple = [['a', 'b'], ['c', 'd'], ['e', 'f']]
# print(dict(couple))
# info = dict([('name', 'Alex'), ('age', 38)])
# print(info)
print('*********************************************************')
languages_programmers = {
    'JavaScript': 'Brendan Eich',
    'Python': 'Guido van Rossum',
    'Ruby': 'Yukihiro Matsumoto',
    'PHP': 'Rasmus Lerdorf',
    'Scala': 'Martin Odersky'
    }
print(languages_programmers)
languages_programmers['C'] = 'Dennis MacAlistair Ritchie'
print(languages_programmers)
# first = {'a': 10, 'b': 20}
# second = {'b': 'other'}
# first.update(second)
# print(first)
# x = {0, 1, 4, 5, 7, 9}
# y = {1, 2, 3, 6, 7, 8, 9}
# print(x)
# print(y)
# x.add(100)
# print(x)
# x.remove(100)
# print(x)
# print(x & y)
# print(x - y)
# sports_equipment = {
#     ('1500 metres', 'high jump', 'shot put'): 'Athletics',
#     ('goalkeeper', 'foul', 'corner'): 'Football',
#     ('handlebars', 'wheels', 'bicycle pump'): 'Cycling'
#     }
# print(sports_equipment)
# room = {'bookcase': 1, 'armchair': 3, 'table': 1, 'clock': True}
# print(room)
# one = True
# print(one)
# two = False
# print(two)