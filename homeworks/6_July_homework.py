import re
"""
6. Вводимо стрічку довільної довжини. Підрахувати: 1) кількість чисел 2)
кількість слів, які починаються з великої букви у даній стрічці.
"""
# str = input('Enter the row: ')
# count_numbers = 0
# for x in str:
#     if x.isdigit():
#         count_numbers += 1
#     # так не получилось, пришлось гуглить и делать через re
#     # if x.istitle():
#     #     count_CAPS += 1
#     #     print(x)
# digits_array = len(re.findall(r'[0-9]', str))
# caps_array = len(re.findall(r'\b[A-Z]', str))
# print(f'Количесво чисел = {count_numbers}, re:Количество чисел = {digits_array},'
#       f' Количество слов с большой буквы = {caps_array} ')
"""
7. Вводимо стрічку. Перевірити чи є стрічка паліндромом. Стрічка-паліндром –
це стрічка, яка пишеться одинаково з переду по кінець, та з кінця на перід – око, 121, тут
"""
# str = input('Enter row: ')
# reverse = str[::-1]
# rezult = print(f'Строка "{str}" - палиндром') if str.lower() == reverse.lower() else print(f'Строка "{str}" - NE палиндром')
"""
8. Організувати цикл від 1 до 1000. Якщо квадрат числа закінчується на 04 то
вивести його.
"""
# square = []
# for i in range(1,1001):
#     if ((i*i)%10) == 4:
#         square.append(i)
# print(*square)
"""
9. Реалізувати функцію, у яку передаємо 3 параметри – a, b, c. Параметри b і с по замовчуванню = 5 і 8, 
та не є обов’язковими. Повернути добуток a, b, c.
"""
# def mult(a,b=5,c=8):
#     print(a*b*c)
#
# mult(2)
"""
10. Написати довільну функцію, використовуючи формальний параметр *args.
"""
# def multiply(*args):
#     z = 1
#     for num in args:
#         z *= num
#     print(z)

# def add(*args):
#     z = 0
#     for num in args:
#         z+=num
#     print(z)
#
# нумерованный список
def print_everything(*args):
    for count, thing in enumerate(args):
        #print('{0}. {1}'.format(count, thing))
        print(f'{count}. {thing}')

print_everything('apple', 'banana', 'cabbage', 'pears')