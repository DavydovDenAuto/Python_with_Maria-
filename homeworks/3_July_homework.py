"""
task1
Вхідні дані – два цілих числа. Вивести перше число у степені другого числа
"""
# int_1 = 12
# num1 = int(input('input 1st number: '))
# num2 = int(input('input 2nd number: '))
# result = 1
# for i in range(num2):
#     result*=num1
# print(result)

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

"""
task_3 
Здійснюємо ввід стрічки поки введена стрічка не буде словом «Test». (while)
"""
# while str !='Test':
#     str = input('Enter word: ')
"""
Task_4
Дана частка тексту. Зберіть усі великі літери в одне слово в тому порядку як
вони зустрічаються в шматку тексту.
Тестовий зразок: “How are you? Eh, ok. Low or Lower? Ohhh.” – HELLO
"""
# str = """How are you? Eh, ok. Low or Lower? Ohhh."""
# word_array  = ''
# for x in str:
#     if x.isupper():
#         word_array+=x
# print(word_array)


"""
task_5
Задано додатне ціле число. Вам необхідно підрахувати добуток всіх цифр в
цьому числі, за винятком нулів.
"""
# number = int(input('Enter number: '))
# p = 1
# while number > 0:
#     n = number % 10
#     if n != 0:
#         p *= n
#     number//=10
# print(p)

"""
15. Дані списки:
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89];
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13].
Створити список із елементів які спільні для цих двох списків.
"""
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# c = []
# for i in a:
#     for j in b:
#         if i==j:
#             c.append(i)
#             break
# print(c)
