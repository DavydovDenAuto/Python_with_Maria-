"""
Напиши програму мовою Python для копіювання файлу. ( Підказка: треба відкрити файл, який хочеш скопіювати, прочитати його,
а тоді створити інший файл - копію).
Перевір, чи твоя програма працює, вивівши на екран (надрукувавши) вміст нового файлу.
"""
# import shutil
#
# def fileCopying(myfile,myfile_2):
#     with open(myfile, 'w', encoding='utf-8') as f_w:
#         f_w.write('Hello, lets go to the gym')
#     shutil.copy(f'D:\\Python\\python_with_Maria\\homeworks\\files\\{myfile}',
#                 f'D:\\Python\\python_with_Maria\\homeworks\\files\\{myfile_2}')
#     try:
#         with open(myfile_2, encoding='utf-8') as f_r:
#             content = f_r.read()
#     except FileNotFoundError:
#         print(f'Sorry, the file {myfile_2} is not found')
#     else:
#         print(content)
#
# myfile = 'myfile_1.txt'
# myfile2 ='myfile_2.txt'
# fileCopying(myfile,myfile2)

"""
2. Напишите программу на Python для чтения первых n строк файла.
"""
my_file = open('Task_2.txt', 'w+')
my_list = [x for x in range(10000) if x % 2 == 1]
my_string_list = """
В начале объявляется переменная my_file. После этого используются встроенные функции open и write для открытия и 
записи в файл. "w+" сообщает, что запись будет осуществляться в новый файл. Если он существует, 
то новое содержимое нужно записать поверх уже существующего. Если же вместо этого использовать параметр "w", 
тогда файл будет создан только в том случае, если он не существовал до этого.
"""
try:
    with open('Task_2.txt', 'w', encoding='utf-8') as f:
        f.write(my_string_list)
    with open('Task_2.txt', encoding='utf-8') as f:
        content = f.read()
except FileNotFoundError:
    print(f'file {my_file} has not been found')
else:
    print(content)

# numbers = [x for x in range(16) if x % 2 == 1]
# filename = 'numbers.json'
# with open(filename, 'w') as f:
#     json.dump(numbers,f)
"""
Напишите программу на Python для добавления текста в файл и отображения текста.
"""
"""
Напишите программу на Python для подсчета количества строк в текстовом файле.
"""
"""
Напишите программу на Python для записи списка в файл.
"""
