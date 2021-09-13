popular_sites = ['Google.com', 'Youtube.com', 'Facebook.com', 'Baidu.com', 'Wikipedia.org', 'Yahoo.com', 'Amazon.com']
for index, value in enumerate(popular_sites,  6):
    print(index, value)
print('########################################')
days = ['Monday', 'Tuesday', 'Wednesday']
fruits = ['coconut', 'lemon', 'mango']
drinks = ['coffee', 'tea', 'milk', 'juice']
desserts = ['marmalade', 'ice cream', 'pie', 'pudding']
for day, fruit, drink, dessert in zip(days, fruits,  drinks, desserts):
    print(day, ": drink", drink, "eat", fruit, "enjoy", dessert)
print('#####################################')
english = 'Monday', 'Tuesday', 'Wednesday'
french = 'Lundi', 'Mardi', 'Mercredi'
print(zip(english, french))
print(list(zip(english, french)))
print(dict(zip(english, french)))
print('###################################')
my_str_list = ['1', '2', '3', '4']
print('type =',type(my_str_list),';', 'my_str_list =',my_str_list)
print('------------------------------')
my_int_list = list(map(int, my_str_list))
print('type =',type(my_int_list),';', 'list(map(int, my_str_list)) =',my_int_list)
print('------------------------------')
my_float_list = list(map(float, my_str_list))
print('type =',type(my_float_list),';', 'list(map(float, my_str_list)) =',my_float_list)
print('------------------------------')
my_new_str_list = list(map(str, my_float_list))
print('type =',type(my_new_str_list),';', 'list(map(str, my_float_list)) =',my_new_str_list)
print('------------------------------')
my_tuple = tuple(map(int, my_str_list))
print('type =',type(my_tuple),';', 'tuple(map(int, my_str_list)) =',my_tuple)
print('------------------------------')
my_set = set(map(float, my_str_list))
print('type =',type(my_set),';', 'set(map(float, my_str_list)) =',my_set)
print('------------------------------')
my_newer_str_list = list(map(str, my_tuple))
print('type =',type(my_newer_str_list),';', 'list(map(str, my_tuple)) =',my_newer_str_list)
print('###############################')
#[вираз for елемент in ітеративний елемент]
number_list = [number for number in range(1, 6)]
print(number_list)
number_list = [number-1 for number in range(1, 6)]
print(number_list)
#[вираз for елемент in ітеративний елемент if умова]
a_list = [number for number in range(1, 6) if number % 2 == 1]
print(a_list)
print('#####################################')
a_list = []
for number in range(1, 6):
    if number % 2 == 1:
        a_list.append(number)
print(a_list)
print('#######################################')
#{ключ: значення for вираз in ітеративний елемент}
word = 'Antarctica'
letter_counts = {letter: word.count(letter) for letter in word}
print(letter_counts)
print('##########################################')
print(sum(range(1, 51)))
poem =   '''The mighty Dnieper roars bellows,
                    the wind in anger howls and raves, Down
                    to the ground it bends the willows,
                    And mountain-high lifts up the waves.'''
frecord = open('result.txt', 'w')
a = frecord.write(poem)
frecord.close()
print(a)
print('################################################')
import calendar
print(calendar.isleap(1900))
print(calendar.isleap(2000))
print('########################')
import datetime
from datetime import date
independence_day = date(2020, 8, 24)
print(independence_day)
datetime.date(2020, 8, 24)
print(independence_day.day)
print(independence_day.month)
print(independence_day.year)
print(independence_day.isoformat())
print('###########################')
from datetime import date
now = date.today()
print(now)
print('###########################')
from datetime import date
from datetime import timedelta
now = date.today()
print(now)
one_day = timedelta(days=1)
tomorrow = now + one_day
print(tomorrow)
after_days = now + 17 * one_day
print(after_days)
yesterday = now - one_day
print(yesterday)
import time
now = time.time()
print(now)
print(time.ctime(now))
print('############################')
import time
starttime = time.time()
for i in range(1000, 0, -1):
    print(i)
endtime = time.time()
print('The program has been running:', str(endtime - starttime), 'seconds.')
print('#############################')
import time
row_format = "It's %A, %B %d, %Y, local time %H:%M:%S"
t = time.localtime()
print(t)
print(time.strftime(row_format, t))

















