"""
task1
Вхідні дані – два цілих числа. Вивести перше число у степені другого числа
"""
# int_1 = 12
# int_2 = int(input('input second number: '))
# print(f' number {int_1} to the power of {int_2} will be: {int_1**int_2}')
# sdelat cherez for in range
"""
task_2
Вхідні дані – ціле число. Вивести «Fizz Buzz», якщо число ділиться націло на
3 і на 5, “Fizz” якщо націло лише на 3, “Buzz” якщо націло лише на 5.
"""
# number = int(input('input number: '))
# if not type(number) is int:
#     raise TypeError("Only integers are allowed")
# if number % 3 == 0 and number % 5 == 0:
#     print('Fizz Buzz')
# elif number % 3 == 0:
#     print('Fizz')
# elif number % 5 == 0:
#     print('Buzz')
# QUESTION - why '-3' is a bad input?

"""
task_3 
Здійснюємо ввід стрічки поки введена стрічка не буде словом «Test». (while)
"""
# option1
# while True:
#     str = input('input string: ')
#     if str == 'Test':
#         break
# option2
# while True:
#     try:
#         str = input('input word: ')
#         if str == 'Test':
#             break
#     except Exception as e:
#         print(e)
# Вопрос - пытался здесь вызвать эксепшин на ввод не строкового значения, как это сделать? Все вводы - строки
"""
Task_4
Дана частка тексту. Зберіть усі великі літери в одне слово в тому порядку як
вони зустрічаються в шматку тексту.
Тестовий зразок: “How are you? Eh, ok. Low or Lower? Ohhh.” – HELLO
"""
# str = """How are you? Eh, ok. Low or Lower? Ohhh."""
# for x in str:
#     if x.isupper():
#         print(x, end='')
"""
task_5
Задано додатне ціле число. Вам необхідно підрахувати добуток всіх цифр в
цьому числі, за винятком нулів.
"""
    # number = int(input('input number: '))
# a = number%10
# b = number//10
# # print(f'multiplication of number = {a*b} ')
# res = 1
# for i in range(len(chr(number))):
#     if i !=0:
#         res = a*b
# print(res)
# p = 1
# while number > 0:
#     p*=number%10
#     if p!=0:
#         number//=10
# print(p)
# double check

"""
15. Дані списки:
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89];
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13].
Створити список із елементів які спільні для цих двох списків.
"""
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []
for i in a:
    for j in b:
        if i==j:
            c.append(i)
            break
print(c)
