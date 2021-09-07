# with open('myfile.txt','a') as my_file:
#     my_file.write('\nI love')
#
# file_name = 'myfile.txt'
# with open(file_name,'a') as file_objects:
#     file_objects.write('am.\n')

# try:
#     print(5/0)
# except: ZeroDivisionError
# print('you cant divide by zero')

# while True:
#     first_num = input('input first num: ')
#     if first_num=='q' or first_num=='Q':
#         break
#     sec_num = input('input sec num: ')
#     if sec_num=='q' or sec_num=='Q':
#         break
#     else:
#         try:
#             result = int(first_num) / int(sec_num)
#         except ZeroDivisionError:
#             print('you cant divide by zero')
#         else:
#             print(result)

# file_name = 'myfile.txt'
# try:
#     with open(file_name,encoding='utf-8') as f:
#         contents = f.read()
# except FileNotFoundError:
#     print(f'Sorry, the file "{file_name}" is not found')
# else:
#     words = contents.split()
#     num_words = len(words)
#     print(f'file has about {num_words} words')

# def count_words(filename):
#     try:
#         with open(filename,encoding='utf-8') as f:
#             contents = f.read()
#         with open(filename,'a', encoding='utf-8') as f:
#             f.write('\tmama mila ramu')
#     except FileNotFoundError:
#         print(f'Sorry, the file "{filename}" is not found')
#     else:
#         words = contents.split() #создали список слов
#         num_words = len(words) # вывели длину списка
#         print(f'file {filename} has about {num_words} words')
#
# filename = 'myfile.txt'
# count_words(filename)

# line = 'Row, row, row your boat'
# count = line.lower().count('row')  # 3
# print(count)

import json

# numbers = [x for x in range(16) if x % 2 == 1]
# filename = 'numbers.json'
# with open(filename, 'w') as f:
#     json.dump(numbers,f)        #создало файл с жсоном


with open('numbers.json') as file_object:
    contents = file_object.read()
print(contents)

filename = 'numbers.json'

with open(filename) as file_object:
    for line in file_object:
        print(line)

